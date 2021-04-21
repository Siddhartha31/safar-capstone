from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'Account':
                    return redirect('causes')
                elif group == 'Admin':
                    return redirect('Admin')
            else:
                return redirect('Signout')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                elif group == 'Account':
                    params = {
                        'msg': group,
                        'way': 'causes'
                    }
                    return render(request, 'fund/access-deny.html', params)
                elif group == 'Admin':
                    params = {
                        'msg': group,
                        'way': 'Admin'
                    }
                    return render(request, 'fund/access-deny.html', params)
        return wrapper_func
    return decorator
