from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('show_categories/<slug:cat_slug>/', show_categories, name='cats'),
    path('basket/', basket, name='basket'),
    path('post/<slug:post_slug>/', show_post, name='show_post'),

    path('login/', login, name='login'),
    path('register/', RegisterUesr.as_view(), name='register')

]
