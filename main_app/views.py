from datetime import datetime, timezone
from django.shortcuts import render
from django.views import View
from .models import Profile, Post
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        # ordering = ['-date_posted']
        # context["posts"] = Post.objects.filter(user=self.request.user)
        return context

class About(TemplateView):
    template_name = "about.html"

class DancerList(TemplateView):
    template_name = "dancer_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["users"] = User.objects.all()
        # return context
        name = self.request.GET.get("username")

        if name != None:
            # context["dancers"] = Dancer.objects.filter(name=name, user=self.request.user)
            context["users"] = User.objects.filter(username=name)
            context["header"] = f"Searching for {name}"
        else:
            # context["dancers"] = Dancer.objects.filter(user=self.request.user)
            context["users"] = User.objects.all()
            context["header"] = "Dancers"
        return context

class PostCreate(View):
    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")
        date_posted = datetime.now(timezone.utc)
        Post.objects.create(title=title, content=content, date_posted=date_posted, user=self.request.user)
        return redirect('home')

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["playlists"] = Playlist.objects.all()
        return context

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_update.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDelete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/"

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