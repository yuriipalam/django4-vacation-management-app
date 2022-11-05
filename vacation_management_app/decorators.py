import functools
from .models import Account
from django.shortcuts import render, get_object_or_404


def status_validator(function):
    @functools.wraps(function)
    def wrapper(request, *args, **kwargs):
        account = get_object_or_404(Account, user_id=request.user.id)
        if account.status is None:
            return render(request, 'vacation_management_app/no_permission.html')
        return function(request, *args, **kwargs)
    return wrapper
