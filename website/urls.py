from . import views

from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   #path('',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register_user,name='register'),
  # path('record/<int:pk>',views.customer_record,name='record')
]
