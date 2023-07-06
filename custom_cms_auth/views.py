from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
from .models import User

def login_page(request):
    message = ''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'custom_cms_auth/login.html', context={'form': form, 'message': message})

def logout_user(request):
    
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'custom_cms_auth/home.html')

def get_staff(request):
    staff = User.objects.all()
    return render(request,
                  'staff/staff_tab.html',
                  context={'staff': staff},)
    
def update_staff(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'staff/staff_update.html', {'form': form, 'user': user})