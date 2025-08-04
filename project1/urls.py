from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from school import views

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', views.loginUser, name='login'),
    path('admin/', admin.site.urls),
    path('index/', views.indexHome, name='index'),
]
