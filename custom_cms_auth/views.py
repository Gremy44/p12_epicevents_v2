from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from .forms import LoginForm, UserForm
from .models import User
from django.db.models import Q
from django.contrib.auth.models import Group


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


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'custom_cms_auth/home.html'


class StaffDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'staff/staff_detail.html'
    context_object_name = 'staff'
    permission_required = 'custom_csm_user.view_user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff = self.get_object()  # Récupère l'objet Contract pour accéder à ses attributs
        context['staff'] = staff
        return context

 
class StaffListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'staff/staff_tab.html'
    context_object_name = 'staff'
    paginate_by = 10
    permission_required = 'custom_csm_user.view_user'
    
    #protection contre l'autosuppression et suppression de l'admin
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.exclude(Q(username=user.username) | Q(username='admin'))


class StaffCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    template_name = 'staff/staff_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['username', 'first_name', 'last_name', 'password', 'email', 'role']  # Champs à inclure dans le formulaire
    permission_required = 'custom_csm_user.add_user'
    
    def get_success_url(self):
        return reverse_lazy('staff')  # Redirige vers la liste du personnel après la mise à jour réussie
    
    def form_valid(self, form): # associe le groupe au role
        response = super().form_valid(form)
        role = form.cleaned_data['role']
        group_name = 'group_' + str(role)
        group, created = Group.objects.get_or_create(name=group_name)
        self.object.groups.add(group)
        return response
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["add_or_update"] = False
        return context

class StaffUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    template_name = 'staff/staff_add_update_form.html'  # Spécifiez le modèle pour le rendu du formulaire
    fields = ['username', 'first_name', 'last_name', 'password', 'email', 'role']  # Champs à inclure dans le formulaire
    permission_required = 'custom_csm_user.change_user'
    
    def get_success_url(self):
        return reverse_lazy('staff')  # Redirige vers la liste du personnel après la mise à jour réussie
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["add_or_update"] = True
        return context 
    
class StaffDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'staff_delete.html'  # Spécifiez le modèle pour le rendu de la confirmation
    success_url = '/staff'  # URL de redirection après la suppression réussie d'un objet Staff
    permission_required = 'custom_csm_user.delete_user'
    
