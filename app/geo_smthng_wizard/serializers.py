from rest_framework import serializers
from .models import Country, City, Capital

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'