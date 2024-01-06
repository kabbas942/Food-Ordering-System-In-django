from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper(request,*args, **kwargs):
            group=None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
                if group in allowed_roles:
                    print(group)
                    return view_func(request,*args, **kwargs)
                else:
                    return HttpResponse('None')
        return wrapper
    return decorators
