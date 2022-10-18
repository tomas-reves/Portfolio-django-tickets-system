from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileCreation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created. Please log in to your account. ')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def profile_creation(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserProfileCreation()
    return render(request, 'users/edit_profile.html', {'form':form})


@login_required
def user_view(request):
    object_list = User.objects.filter(username=request.user)
    return render(request, 'users/profile.html', {'object_list':object_list})

# def user_change_view(request):
#     if request.method == 'POST':
#         form = UserUpdateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#
#     else:
#         form = UserUpdateForm()
#     return render(request, 'users/edit_profile.html', {'form': form})

