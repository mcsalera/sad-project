from django.urls import path
from .views import (
    # ListingListView,
    ListingDetailView,
    ListingCreateView,
    ListingUpdateView,
    ListingDeleteView
)
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name="homepage"),
    # path('search', ListingListView.as_view(), name='search'),
    path('search', views.searchpage, name='search'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
    path('listing/new/', ListingCreateView.as_view(), name='listing-create'),
    path('listing/<int:pk>/update/',
         ListingUpdateView.as_view(), name='listing-update'),
    path('listing/<int:pk>/delete/',
         ListingDeleteView.as_view(), name='listing-delete'),
    path('about/', views.about, name='booking-about'),
]
