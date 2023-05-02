from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
   # path('about/',views.about,name="about"),
   # path('contact/',views.contact,name="contact"),
  #  path('viewpass/',views.viewpassing,name='viewpass'),
   # path('operations/',views.operations,name='operation')
]