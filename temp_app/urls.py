from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("welcome.urls")),
    path("accounts/", include("accounts.urls")),
    path("home/", include("home.urls")),
]
