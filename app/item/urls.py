from django.urls import path,include

from . import views
app_name='x'

urlpatterns = [
    path('<int:pk>/',views.detail,name='detail'),
    
]

