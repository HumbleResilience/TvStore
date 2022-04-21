from django.urls import path
from .views import SignUpView, ManageAccountView, PasswordChangePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('manage_account/', ManageAccountView.as_view(), name='manage'),
    path('password/', PasswordChangePageView.as_view(), name="change-password"),
]