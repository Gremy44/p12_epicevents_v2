from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

'''def get_staff(request):
    staff = User.objects.all()
    return render(request,
                  'staff/staff_tab.html',
                  context={'staff': staff},)'''


class StaffDetailView(DetailView):
    model = User
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff'
    
class StaffListView(ListView):
    model = User
    template_name = 'staff/staff_tab.html'
    context_object_name = 'staff'
    paginate_by = 10

class StaffCreateView(CreateView):
    model = User
    template_name = 'staff/staff_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['username', 'first_name', 'last_name', 'email', 'role']  # Champs à inclure dans le formulaire

    def get_success_url(self):
        return reverse_lazy('add_customers')  # Redirige vers la liste du personnel après la mise à jour réussie
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["add_or_update"] = False
        return context


class StaffUpdateView(UpdateView):
    model = User
    template_name = 'staff/staff_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['username', 'first_name', 'last_name', 'email', 'role']  # Champs à inclure dans le formulaire

    def get_success_url(self):
        return reverse_lazy('staff')  # Redirige vers la liste du personnel après la mise à jour réussie
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["add_or_update"] = True
        return context 
    

class StaffDeleteView(DeleteView):
    model = User
    template_name = 'staff_delete.html'  # Spécifiez le modèle pour le rendu de la confirmation
    success_url = '/staff'  # URL de redirection après la suppression réussie d'un objet Staff

    
'''def add_update_staff(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, id=user_id)
        add_or_update = True
    else:
        user = None
        add_or_update = False

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff')  # Redirige vers la liste des utilisateurs du staff après l'ajout ou la mise à jour
    else:
        form = UserForm(instance=user)

    return render(request, 'staff/staff_add_update_form.html', {'form': form, 'user': user, 'add_or_update': add_or_update})

def delete_staff(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('staff')
'''