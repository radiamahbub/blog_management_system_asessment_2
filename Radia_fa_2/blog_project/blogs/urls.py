from django.urls import path
from blogs.views import *

urlpatterns = [
    path('', home, name='home'), 


    path('blog/', blog_add, name='blog'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog_update/<str:b_id>/', blog_update, name='blog_update'),
    path('blog_delete/<str:b_id>/', blog_delete, name='blog_delete'),


    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]
