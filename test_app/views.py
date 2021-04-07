from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect('/all-member')

        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        
        username = request.POST['uname']
        password = request.POST['pass']
        print(username)
        print(password)
        confirm_password = request.POST['re_type']
        if password == confirm_password:
            name = request.POST['name']
            blood_group = request.POST['bgroup']
            phone = request.POST['phone']
            user = User.objects.create_user(username = username, password = password)
            blood_donar = BloodDonar.objects.create(user = user, name = name, blood_group = blood_group, phone = phone)

            return redirect('/all-member')


    else:
        return render(request, 'signup.html')




def all_member(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        donar = BloodDonar.objects.all().filter(blood_group = search)
        context = {'donar':donar}
        return render(request, 'all_member.html', context)

    else:
        donar = BloodDonar.objects.all()
        context = {'donar':donar}
        return render(request, 'all_member.html', context)


def user_logout(request):
    logout(request)
    return redirect('/')


