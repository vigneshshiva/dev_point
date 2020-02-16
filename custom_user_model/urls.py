from django.urls import path,include
from .import views
urlpatterns = [
    path('signup',views.register,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('login',views.login_view),


]
