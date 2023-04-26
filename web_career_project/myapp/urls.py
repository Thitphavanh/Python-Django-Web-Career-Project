from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('portal/', portal, name='portal'),
    path('login/', login, name='login'),
    path('add-article/', add_article, name='add-article'),
    path('edit-article/<int:id>', edit_article, name='edit-article'),
    path('about/', about),

]
