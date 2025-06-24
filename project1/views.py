from django.shortcuts import render
from django.http import HttpResponse

# def view_prueba(request):
#     context = {
#         'titulo': 'Easy Learning',
#         'mensaje': 'Bienvenido(a) a Easy Learning, proximamente...'
#     }
#     return render(request, 'templates/inicio.html',context)

def mi_vista(request):
    return HttpResponse("Bienvenidos a Easy Learning, proximamente...")
