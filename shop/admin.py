from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (Item,
        OrderItem,
        Order,
        Payment,
        Coupon,
        Refund,
        Item,
        ProductCategory,
        ProductImage,
        Colors,
        Tags,
        Fashioninsta,
        )


class ColorsInline(admin.TabularInline):
    extra = 1
    model = Colors.products.through

class TagsInline(admin.TabularInline):
    extra = 1
    model = Tags.products.through


class ProductImageInline(admin.TabularInline):
    extra = 1
    model = ProductImage

class CategoryInline(admin.TabularInline):
    extra = 0
    model = ProductCategory.products.through

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, CategoryInline, ColorsInline, TagsInline]
    list_display = ["__str__","description", "price", "get_price",]
    search_fields = ["description","title",]
    list_filter = ["price","category", "timestamp","updated", ]
    list_editable =["price"]
    prepopulated_fields = {"slug":("title",)}
    readonly_fields = ["timestamp","updated",]

    class Meta:
        model = Item

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
       'user__user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference', 'timestamp', 'status', 'success']
    search_fields = ['transaction_id', 'uid', 'reference', 'status', 'timestamp', 'user__user__username',]
    list_filter  = ['status', 'success',  'timestamp', 'user',]


class FashioninstaResource(resources.ModelResource):
    class Meta:
        model = Fashioninsta
        fields = [
    'user', 'slug', 'product', 'neck', 'shoulder', 'chest', 'tommy', 'sleeve', 'biceps', 'round_sleeve', 'wrist', 'shirt',
    'trouser_waist', 'trouser_lenght', 'hip', 'laps', 'knee', 'calf', 'ankle', 'description', 'timestamp', 'updated', 'done'
    ]
        # export_order = ('name', 'uid', 'email', 'subject', 'phone', 'message', 'date_submitted',)


class FashioninstaAdmin(ImportExportModelAdmin):
    resource_class = FashioninstaResource
    list_display = ['slug', 'user', 'product', 'timestamp', 'done',]
    search_fields = ['slug', 'product', 'timestamp', 'user__user__username',]
    list_filter  = ['product', 'done',  'timestamp', 'user',]


# Register your models here.
admin.site.register(Item, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(ProductCategory)
admin.site.register(Colors)
admin.site.register(Tags)
admin.site.register(Fashioninsta, FashioninstaAdmin)