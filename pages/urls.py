from django.urls import path
from . import views

from .views import AboutUsView, ContactForm, HomePageView, LoginView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact/', ContactForm.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
]