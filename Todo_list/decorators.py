from django.shortcuts import HttpResponseRedirect

def login_check(func):
    def decorator(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return func(request)
    return decorator