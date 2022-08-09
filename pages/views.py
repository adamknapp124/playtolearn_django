from django.views.generic import TemplateView

# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class LoginView(TemplateView):
    template_name = 'pages/login.html'


