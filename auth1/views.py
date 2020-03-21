from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import QueryDict
from .models import UserForm,UserProfileChange
from Todo_list.decorators import login_check
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import update_session_auth_hash

@login_check
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/auth1/signin/')
    form = UserForm()
    return render(request,'auth1/signup.html',{'form':form})

@login_check
def signin(request):
    if request.method == 'POST':
        q_string = request.META['QUERY_STRING']
        q_dict = QueryDict(q_string)
        next = q_dict.get('next') or '/'
        try:
            username = request.POST['username']
            user = auth.authenticate(username=username,password=request.POST['password'])
            auth.login(request,user)
            request.session['login_check'] = 'Successfully Logged in!'
            return redirect('/')
        except:
            return render(request, 'auth1/signin.html',{'message':'Username or Password is not correct'})

    return render(request, 'auth1/signin.html')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/auth1/signin')

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileChange(request.POST,instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/auth1/edit_profile')
    user_form = UserProfileChange(instance=request.user)
    return render(request,'auth1/profile.html',{'user':request.user,'user_form':user_form})