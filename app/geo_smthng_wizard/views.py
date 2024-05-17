from rest_framework import generics
from .models import Country, City, Capital
from .serializers import CountrySerializer, CitySerializer, CapitalSerializer
from django.contrib.gis.geos import Polygon
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
    
class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class AllCountriesListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class CountryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    partial = True
    
    
class CountryDeleteView(generics.DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Country"))
    
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
    
class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class AllCitiesListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class CityUpdateView(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    partial = True
    
    
class CityDeleteView(generics.DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete City"))
    
class CapitalListCreateView(generics.ListCreateAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    
    
class CapitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    
class AllCapitalsListView(generics.ListAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    
class CapitalUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer
    partial = True
    
    
class CapitalDeleteView(generics.DestroyAPIView):
    queryset = Capital.objects.all()
    serializer_class = CapitalSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Capital"))
    
class ObjectsWithinBboxView(APIView):
    def get(self, request):
        bbox_param = request.GET.get('bbox')
        bbox = list(map(float, bbox_param.split(','))) if bbox_param else None
        
        if bbox:
            polygon = Polygon.from_bbox(bbox)
            cities_in_bbox = City.objects.filter(geom__within=polygon)
            capitals_in_bbox = Capital.objects.filter(geom__within=polygon)
            
            cities_data = [{'name': city.name, 'geom': city.geom.coords} for city in cities_in_bbox]
            capitals_data = [{'name': capital.name, 'geom': capital.geom.coords} for capital in capitals_in_bbox]
            
            return Response({'cities': cities_data, 'capitals': capitals_data})
        else:
            return Response({'error': 'Please provide bbox parameter'})
