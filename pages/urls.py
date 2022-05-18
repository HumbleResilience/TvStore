from django.urls import path
from.views import AboutPageView, ContactPageView, HomePageView,LogoutPageView, PasswordChangePageView



urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name= "about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('logged_out/', LogoutPageView.as_view(), name="logout"),
    path('password_change/', PasswordChangePageView.as_view(), name="password_change"),
]
