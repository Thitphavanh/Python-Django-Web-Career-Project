from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('portal/', portal, name='portal'),
    path('register/', register, name='register'),
    # path('login/', login_user, name='login'),
    path('add-article/', add_article, name='add-article'),
    path('edit-article/<int:id>', edit_article, name='edit-article'),
    path('booking/', booking),
    path('about/', about),

]
