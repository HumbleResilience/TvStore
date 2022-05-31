from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from accounts.forms import ImageForm, RegisterForm, LoginForm, EditProfileForm
from django.views import generic

from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User


 
 

#  -------------Signup View---------------------------
# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

# ----------------Profile view------------------
class ManageAccountView(generic.UpdateView):
    model = Profile
    template_name = 'registration/manage_account.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

# ------------------Password Change-----------------------
class PasswordChangePageView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('manage')
    template_name = "registration/change-password.html"


# -----------------profile image ---------------
  
# Create your views here.

def profile_image_view(self, request):
    user = User.get_username(self)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            print("it worked")
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'registration/profile-image.html', {'form' : form}, {'user': user})
  
  
def success(request):
    return HttpResponse('successfully uploaded')



# ---------------------Register--------------------


class RegisterView(View):

    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# --------------Login View----------------------------

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            # -- set session to force data updates/cookie to be saved
            self.request.session.modified = True

        # ----else, browser session will be as long as the session cookie time
            return super(CustomLoginView, self).form_valid(form)

# ----------------Edit Profile--------------------------->


# ----------------Edit Profile--------------------------->


