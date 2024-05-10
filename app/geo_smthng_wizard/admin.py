from django.contrib.gis import admin
from .models import Country, City, Capital

# Register your models here.
admin.site.register(Country, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
admin.site.register(Capital, admin.ModelAdmin)