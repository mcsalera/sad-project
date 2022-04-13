from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from .models import Listing
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)

from .forms import SearchForm


def home(request):
    context = {
        'listings': Listing.objects.all()
    }
    return render(request, 'booking/home.html', context)


def homepage(request):
    form = SearchForm()
    if request.method == 'GET':
        print("This is awesome")
    
    return render(request, 'booking/homepage.html', {'form': form})


class ListingListView(ListView):
    model = Listing
    template_name = 'booking/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'listings'
    ordering = ['-date_listed']


class ListingDetailView(DetailView):
    model = Listing


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Listing
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.owner:
            return True
        return False


class ListingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Listing
    success_url = '/'

    def test_func(self):
        listing = self.get_object()
        if self.request.user == listing.owner:
            return True
        return False


def about(request):
    return render(request, 'booking/about.html', {'title': 'About'})
# Create your views here.
