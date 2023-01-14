from django.urls import path
from .views import UserSignupView 

app_name="accounts"
urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="signup"),
]