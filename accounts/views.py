from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
            )
            return redirect('read_blog_list')
        else:
            return render(request, 'accounts/signup.html')

    else:
        return render(request, 'accounts/signup.html')
    #redirect가 아니고 render인 이유: request인자를 받아야하는 동작이기 때문
    #redirect는 url을 띄워줌 render는 temaplates를 띄워준다.
    #그래서 redirect를 하면 계속 signup의 url과 views의 signup이 서로를 계속 호출하며 무한루프가 형성되어 오류가 뜬다.

def signin(request):
    #authenticate
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #login 성공
        if user is not None:
            login(request, user)
            return redirect('read_blog_list')
        #login 실패시 다시 login 화면으로
        else:
            return render(request, 'accounts/signin.html', {'error':'incorrect ID or password'})
    else:
        return render(request, 'accounts/signin.html')

def signout(request):
    logout(request)
    return redirect('read_blog_list')