from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginv,name='login'),
    path('register',views.signup,name='signup'),
    path('logout',views.logout_view,name='logout')
  
]