from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ManageAccountView, PasswordChangePageView, RegisterView, CustomLoginView
from accounts.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('manage_account/', ManageAccountView.as_view(), name='manage'),
    path('password/', PasswordChangePageView.as_view(), name="change-password"),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name = 'registration/login.html'))
] 



