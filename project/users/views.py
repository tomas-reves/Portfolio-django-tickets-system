from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, DepartmentsUpdateForm, PositionsUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import Profile, Department, Position


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('id')
            u = User.objects.last()
            profile = Profile(user=u)
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created. Please log in to your account. ')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@ login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Updates")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

    return render(request, 'users/profile.html', context=context)

@staff_member_required
def customize_departments_positions(request):

    if request.method == "POST":
        departments_form = DepartmentsUpdateForm(request.POST)
        if departments_form.is_valid():
            departments_form.save()
        return redirect('/administration')
    else:
        departments_form = DepartmentsUpdateForm

    if request.method == "POST":
        positions_form = PositionsUpdateForm(request.POST)
        if positions_form.is_valid():
            positions_form.save()
        return redirect('/administration')
    else:
        positions_form = PositionsUpdateForm

    all_departments = Department.objects.all()
    all_positions = Position.objects.all()

    return render(request, 'users/administration.html', {'department_form': departments_form,
                        'positions_form': positions_form, 'all_departments': all_departments, 'all_positions': all_positions  })

