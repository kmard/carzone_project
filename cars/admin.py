from django.contrib import admin
from .models import*
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('car_title', 'thumbnail', 'state', 'vin_no','is_featured')
    list_display_links = ('car_title', 'thumbnail', 'state', 'vin_no')
    search_fields = ('car_title', 'state', 'vin_no')
    list_filter = ('car_title', 'state', 'vin_no')
    list_editable = ('is_featured',)


# Register your models here.
admin.site.register(Car,CarAdmin)