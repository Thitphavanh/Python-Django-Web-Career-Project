from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myapp.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='webcareer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='webcareer/logout.html'), name='logout'),
]
