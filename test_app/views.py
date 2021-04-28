from django.shortcuts import render
from .models import *
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import *
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
            image = request.POST['img']
            name = request.POST['name']
            blood_group = request.POST['bgroup']
            phone = request.POST['phone']
            user = User.objects.create_user(username = username, password = password)
            blood_donar = BloodDonar.objects.create(user = user, name = name, blood_group = blood_group, phone = phone, image = image)

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


def user_profile(request, id):
    profile = BloodDonar.objects.get(pk = id)
    context = {'profile':profile}
    return render(request, 'userprofile.html', context)

def my_profile(request):
    user = request.user
    userprofile = BloodDonar.objects.get(user = user)
    context = {'userprofile':userprofile}
    return render(request,'my_profile.html', context)

def upload_image(request):
    user = request.user
    form = BloodDonarForm(instance = user)
    if request.method == 'POST':
        form = BloodDonarForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, "upload_image.html", context)





