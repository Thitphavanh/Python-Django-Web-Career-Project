from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('portal', portal),
    path('main', main),
    path('information', information),
    path('edit-information', edit_information),
    # path('about', about),

]
