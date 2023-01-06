from django.urls import path
 
from .views import welcomeView

urlpatterns = [
    path('', welcomeView.as_view(), name="welcome"),
]