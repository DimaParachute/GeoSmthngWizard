from django.urls import path
from .views import CountryListCreateView, CountryDetailView, AllCountriesListView, CountryDeleteView, CountryUpdateView, CityListCreateView, CityDetailView, AllCitiesListView, CityDeleteView, CityUpdateView, CapitalListCreateView, CapitalDetailView, AllCapitalsListView, CapitalDeleteView, CapitalUpdateView

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('countries/all/', AllCountriesListView.as_view(), name='all-countries-list'),
    path('countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='country-delete'),
    path('countries/update/<int:pk>/', CountryUpdateView.as_view(), name='country-update'),
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),
    path('cities/all/', AllCitiesListView.as_view(), name='all-cities-list'),
    path('cities/delete/<int:pk>/', CityDeleteView.as_view(), name='city-delete'),
    path('cities/update/<int:pk>/', CityUpdateView.as_view(), name='city-update'),
    path('capitals/', CapitalListCreateView.as_view(), name='capital-list-create'),
    path('capitals/<int:pk>/', CapitalDetailView.as_view(), name='capital-detail'),
    path('capitals/all/', AllCapitalsListView.as_view(), name='all-capitals-list'),
    path('capitals/delete/<int:pk>/', CapitalDeleteView.as_view(), name='capital-delete'),
    path('capitals/update/<int:pk>/', CapitalUpdateView.as_view(), name='capital-update'),
]