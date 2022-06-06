from struct import unpack_from
from django.shortcuts import render
from django.views import View
from .models import Profile, Post
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        # context["posts"] = Post.objects.filter(user=self.request.user)
        return context

class About(TemplateView):
    template_name = "about.html"

class DancerList(TemplateView):
    template_name = "dancer_list.html"

@method_decorator(login_required,name='dispatch')
class Profile(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        u_form = UserUpdateForm(instance=self.request.user)
        p_form = ProfileUpdateForm(instance=self.request.user.profile)

        context = super().get_context_data(**kwargs)
        context["profile"] = Profile
        context["u_form"] = u_form
        context["p_form"] = p_form
        return context

    def post(self, request, *args, **kwargs):
        u_form= UserUpdateForm(self.request.POST, instance=self.request.user)
        p_form = ProfileUpdateForm(self.request.POST, self.request.FILES, instance=self.request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("profile")

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserRegisterForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)