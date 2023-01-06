from django.views.generic import TemplateView


class welcomeView(TemplateView):
    template_name="welcome/welcome.html"
