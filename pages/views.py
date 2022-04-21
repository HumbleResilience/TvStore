

from re import template
from django.views.generic import TemplateView



class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class LogoutPageView(TemplateView):
    template_name = "registration/logged_out.html"


class CatalogPageView(TemplateView):
    template_name = "catalog.html"

class CheckoutPageView(TemplateView):
    template_name = "checkout.html"




        