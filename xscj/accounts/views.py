from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def signupaccount(request) :
    if request.method == 'GET':
        return render(request,'signupaccount.html',{'form':UserCreateForm})
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')

        if password1 and password2 and password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('musichome')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': '用户已存在'})

        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm(), 'error': '输入的密码不一致'})

@login_required
def logoutaccount(request):
    logout(request)
    return redirect('musichome')

def loginaccount(request) :
    if request. method == 'GET' :
        return render(request, 'loginaccount.html', {'form':AuthenticationForm})
    else:
        user = authenticate(request,
        username=request.POST['username'] ,
        password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form':AuthenticationForm, 'error':'用户名或密码错误' })
        else:
            login(request, user)

