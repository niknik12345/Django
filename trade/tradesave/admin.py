from django.contrib import admin

# Register your models here.

from .models import *


#admin.site.register(Lot)

#admin.site.register(Сategory)

#admin.site.register(Status)

#admin.site.register(Types)

###############################################
class TypesAdmin(admin.ModelAdmin):
    list_display = ('id','types_name',)
    list_display_links = ('id','types_name',)
    search_fields = ('types_name',)

class СategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name',)
    list_display_links = ('id','category_name',)
    search_fields = ('category_name',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','status_name',)
    list_display_links = ('id','status_name',)
    search_fields = ('status_name',)


class LotAdmin(admin.ModelAdmin):
    list_display = ('id','lot_name','types','status','lot_price','lot_quantity','category',)
    #list_display = ('id','lot_name','types_name','status','lot_price','lot_quantity','category',)
    list_display_links = ('id','lot_name','types','status','lot_price','lot_quantity','category',)
    search_fields = ('lot_name',)

#############################################################
admin.site.register(Сategory, СategoryAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Types, TypesAdmin)