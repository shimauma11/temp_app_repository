from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate

from .form import SignupForm


class UserSignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('/')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response
