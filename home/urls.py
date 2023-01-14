from django.urls import path
from .views import postView

app_name = 'home'
urlpatterns = [
    path("post/",postView.as_view(), name="post"),
]