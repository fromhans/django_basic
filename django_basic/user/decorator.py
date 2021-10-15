from django.shortcuts import redirect
from .models import User


def login_required(function):
    # class view의 dispatch에 wrapping되는 것이기 때문에 아규먼트를 맞춰주기위해 3가지 인자값을 추가해줌.
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        print("login_required!")
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            print("login required")
            return redirect('/login/')
        user = User.objects.get(email=user)
        if user.level != 'admin':
            print("admin level required")
            return redirect('/login/')
        return function(request, *args, **kwargs)
    return wrap
