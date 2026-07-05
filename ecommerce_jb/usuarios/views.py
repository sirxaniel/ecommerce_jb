from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('tienda:catalogo')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.username}!')
            return redirect(request.GET.get('next', 'tienda:catalogo'))
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('tienda:catalogo')

def registro(request):
    if request.user.is_authenticated:
        return redirect('tienda:catalogo')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.username}! Cuenta creada.')
            return redirect('tienda:catalogo')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})
