from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_exists = User.objects.filter(username=username).exists()

        if not user_exists:
            return render(request,
                  'login.html',
                  {'form': AuthenticationForm,
                   'error': 'El usuario no existe'})
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            #login(request, user)
            return redirect('index')
        else:
            return render(request,
                  'login.html',
                  {'form': AuthenticationForm,
                   'error': 'Usuario y/o contraseña incorrecta'})
    else:
        return render(request,
                  'login.html',
                  {'form': AuthenticationForm,
                   'error':''})
        

def indexHome(request):
    return render(request,'index.html')