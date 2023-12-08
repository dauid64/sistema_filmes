from django.views.generic import View, CreateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(
            request,
            'authentication/pages/login.html',
            context={
                'form': login_form
            }
        )

    def post(self, request):
        POST = request.POST
        login_form = LoginForm(POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data.get('username', ''),
                password=login_form.cleaned_data.get('password', '')
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Logado com sucesso!')
            else:
                messages.warning(request, 'Credenciais Inválidas')
        else:
            messages.warning(request, 'Usuário ou senha inválidas')
        return redirect(
            reverse('core:home')
        )


class CreateUserView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('authentication:login')
    template_name = 'authentication/pages/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()    
        return super().form_valid(form)


class LogoutView(View):
    def post(self, request):
        if request.POST.get('username') != request.user.username:
            messages.error(request, 'Usuário de Logout inválido')
            return redirect(reverse('authentication:login'))
        messages.success(request, 'Deslogado com sucesso!')
        logout(request)
        return redirect(reverse('authentication:login'))
