from django.urls import path
<<<<<<< HEAD
from.views import AboutPageView, CheckoutPageView, ContactPageView, HomePageView, SupportPageView, LoginPageView,LogoutPageView, PasswordChangePageView, CatalogPageView, CheckoutPageView
=======
from.views import AboutPageView, ContactPageView, HomePageView, LoginPageView, LogoutPageView
>>>>>>> 90239469875d972b222030f9e9e3a4b899ca6418



urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name= "about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('registration/login/', LoginPageView.as_view(), name="login" ),
    path('logged_out/', LogoutPageView.as_view(), name="logout"),
<<<<<<< HEAD
    path('password_change/', PasswordChangePageView.as_view(), name="password_change"),
    path('catalog/', CatalogPageView.as_view(), name="catalog"),
    path('cart/', CheckoutPageView.as_view(), name="checkout"),
=======
    

    
    
   
>>>>>>> 90239469875d972b222030f9e9e3a4b899ca6418
]
