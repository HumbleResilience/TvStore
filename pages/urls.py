from django.urls import path
from.views import AboutPageView, ContactPageView, HomePageView, LoginPageView, LogoutPageView



urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name= "about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('registration/login/', LoginPageView.as_view(), name="login" ),
    path('logged_out/', LogoutPageView.as_view(), name="logout"),
    

    
    
   
]
