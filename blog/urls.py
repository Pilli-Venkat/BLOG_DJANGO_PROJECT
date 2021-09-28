from django.urls import path
from . import views
urlpatterns = [
    path('',views.blog,name='home'),
    path('post/<str:title>/',views.post,name='post'),
    path('comment',views.post_comment,name='comment'),
    path('search',views.search_view,name='search'),
    path('category/<str:cat>/',views.get_category,name='category'),
  

]
