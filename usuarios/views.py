from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirige según el rol del usuario
            if user.cargo and user.cargo.nombre == 'Administrador':
                return redirect('admin_dashboard')
            elif user.cargo and user.cargo.nombre == 'Inspector':
                return redirect('inspector_dashboard')
            else:
                return redirect('home')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'usuarios/login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'usuarios/admin_dashboard.html')

@login_required
def inspector_dashboard(request):
    return render(request, 'usuarios/inspector_dashboard.html')
