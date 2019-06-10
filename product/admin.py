from django.contrib import admin
from .models import Product, Category, City, Company, Country,Brand
from django.utils import timezone
from django.utils.safestring import mark_safe


# Register your models here.
def deactivate_status(modeladmin, request, queryset):
    queryset.update(
        status=0,
        lastupdateddate=timezone.now()
    )
deactivate_status.short_description = 'Deactivate' # at admin page


def activate_status(modeladmin, request, queryset):
    queryset.update(
        status=1,
        lastupdateddate=timezone.now()
    )
activate_status.short_description = 'Activate' # at admin page

# By Using decorotor
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Product._meta.get_fields()]
    list_display = ['__str__','brand_name','category_name','addeddate','lastupdateddate','status']
    fields = ('productname','brandid','categoryid','status')
    list_editable = ['status']
    list_per_page = 20
    ordering = ['addeddate']
    search_fields = ['productname']
    actions = [activate_status,deactivate_status]

    list_select_related = ['categoryid','brandid']
    # list_filter = ['productname']
    # empty_value_display = '-empty-'
    # exclude = ('birth_date',)
    
    # pass
    def brand_name(self, obj):
        # in this context, obj is the Manager instance for this line item
        return obj.brandid


admin.site.register(Category)

# admin.site.register(Brand)
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['__str__','admin_image','company','addeddate','lastupdateddate','status']
    list_editable = ['status']
    actions = [activate_status,deactivate_status]
    list_select_related = ['companyid']

    def company(self,obj):
        return obj.companyid


    # def showimage(self,obj):
    #     # return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #     #     url = obj.brandlogo,
    #     #     width=obj.brandlogo,
    #     #     height=obj.brandlogo,
    #     #     ))
    #     return '<img src={} style="height: 100px;"/>'.format(obj.brandlogo)            
    # showimage.short_description = 'Logo' # at admin page
    # showimage.allow_tags = True # at admin page

    def admin_image(self,obj):
        return mark_safe('<img src="{}" width="150" height="150" / />'.format( obj.brandlogo))
    # admin_image.allow_tags = True        
    admin_image.short_description = 'Logo' 


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # empty_value_display = '-empty-'
#     # exclude = ('')
#     pass


#admin.site.register(Product,ProductAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['cityname','citycode','stateid','status','addeddate','lastupdateddate']
    list_display = ['cityid','__str__','citycode','stateid','addeddate','lastupdateddate','status']
    list_editable = ['status']
    actions = [activate_status,deactivate_status]
    # pass
    # def __init__(self,*args,**kwargs):
    #     super(CityAdmin, self).__init__(*args, **kwargs)
    #     self.list_display_links = (None, )
    


