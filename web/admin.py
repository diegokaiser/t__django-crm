from django.contrib import admin
from .models import (Client, Brand, Product, Reason, BannerDestacado, BannerA, TipoVia, JobTitle, PaymentMethod,
                     CurrencyType, BankAccount, MenuCategory, MenuSubcategory, System, Subsystem)

# Register your models here.
admin.site.register(Client)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Reason)
admin.site.register(BannerDestacado)
admin.site.register(BannerA)
admin.site.register(TipoVia)
admin.site.register(JobTitle)
admin.site.register(PaymentMethod)
admin.site.register(CurrencyType)
admin.site.register(BankAccount)
admin.site.register(MenuCategory)
admin.site.register(MenuSubcategory)
admin.site.register(System)
admin.site.register(Subsystem)
