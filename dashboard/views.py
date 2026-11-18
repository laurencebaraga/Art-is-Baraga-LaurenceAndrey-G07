from functools import wraps
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def role_required(role):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.role != role:
                raise PermissionDenied
            return view(request, *args, **kwargs)
        return wrapper
    return decorator


@login_required
def dashboard_redirect(request):
    if request.user.role == 'ADMIN':
        return redirect('admin_dashboard')
    return redirect('artist_dashboard')


@role_required('ADMIN')
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


@role_required('ARTIST')
def artist_dashboard(request):
    return render(request, 'dashboard/artist_dashboard.html')