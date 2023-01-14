from django.urls import path, include
 
from .views import welcomeView

app_name="welcome"
urlpatterns = [
    path("", welcomeView.as_view(), name="welcome"),
    path("accounts/", include("accounts.urls")),
    path("home/", include("home.urls")),
]