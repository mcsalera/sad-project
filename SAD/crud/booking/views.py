from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from .models import Listing
from django.views.generic import (
    # ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.http import Http404

from .forms import SearchForm


def searchpage(request):
    context = {
        'listings': Listing.objects.all()
    }
    if 'country' and 'city' in request.GET:
        if request.GET.get('city') != '':
            context = {
                'listings': Listing.objects.filter(country__icontains=request.GET.get('country')).filter(city__icontains=request.GET.get('city')).filter(price__lte=request.GET.get('price'))
            }
        else:
            context = {
                'listings': Listing.objects.filter(country__icontains=request.GET.get('country')).filter(price__lte=request.GET.get('price'))
            }
    return render(request, 'booking/search.html', context)


def homepage(request):
    form = SearchForm()
    
    return render(request, 'booking/homepage.html', {'form': form})


# class ListingListView(ListView):
#     model = Listing
#     template_name = 'booking/search.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'listings'
#     ordering = ['-date_listed']


class ListingDetailView(DetailView):
    model = Listing


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['title', 'description', 'country', 'city','price', 'facility_image']

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
    raise Exception('error !!!!')
    raise Http404("sorry 404")
    return render(request, 'booking/about.html', {'title': 'About'})
# Create your views here.
