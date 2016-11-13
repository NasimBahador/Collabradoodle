from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Doodle

def session_check(request):
    pass

def index(request):
    return render(request,'index.html')

def login_reg(request):
    if request.POST['action'] == 'register':
        result = User.objects.validate_reg(request)

    elif request.POST['action'] == 'login':
        result = User.objects.validate_login(request)

    if result[0] == False:
        print_errors(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])


def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def log_user_in(request, user):
    return redirect('wall')

def doodle(request):
    pass

def wall(request):
    return render(request, 'wall.html')

def logout(request):
    pass
