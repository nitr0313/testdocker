from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('entrance', 'number', 'person', 'active', 'sqare')
    list_display_links = ('number', 'person')
    list_filter = ('entrance', 'active')
    search_fields = ('person__fullname',)
    list_per_page = 20
    ordering = ('number',)
    # list_order_by = ('number')
    # class Meta:
    #     model = models.Flat


@admin.register(models.Person)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('fullname',)
    list_display_links = ('fullname',)
    search_fields = ('fullname',)
    ordering = ('fullname',)
# admin.site.register(models.Flat)


admin.site.register(models.Street)
admin.site.register(models.Address)
