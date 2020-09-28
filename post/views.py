from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def read_blog_list(request):
    blogs = Blog.objects.all()
    #pagination : 몇 개씩 볼것이냐?
    paginator = Paginator(blogs, 5)
    #지금 보려는 페이지는?
    page = request.GET.get('page')
    #새로 담아서 보내주자
    posts = paginator.get_page(page)
    return render(request, 'post/blog_list.html', {'posts':posts})

def read_blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'post/blog_detail.html', {'blog':blog})

def blog_new(request):
    return render(request, 'post/blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('read_blog_list')

def delete_blog(request, blog_id):#url, html에서도 넘겨줘야함
    #객체 탐색
    blog = get_object_or_404(Blog, pk = blog_id)
    #삭제
    blog.delete()
    #리스트 페이지로 넘어가기
    return redirect('read_blog_list')

def update_blog(request, blog_id):
    #객체 탐색
    blog = get_object_or_404(Blog, pk=blog_id)
    #데이터 입력
    if request.method == "POST":
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        #데이터 저장
        blog.save()

        return redirect('read_blog_detail', blog_id)
    else:
        return render(request, 'post/blog_edit.html', {'blog' : blog})