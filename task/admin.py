from django.contrib import admin
from . models import AuthUser, Product, Agency, Secure, Renew, Cliente

class AuthUserAdmin(admin.ModelAdmin):
    fields = ('name_complet','name_user','photo',)
    list_display = ('name_complet','name_user','photo')


class ProductAdmin(admin.ModelAdmin):
    fields = ('name_product','comments',)
    list_display = ('name_product','comments','update_at')
    

class AgencyAdmin(admin.ModelAdmin):
    fields = ('name_agency','comments',)
    list_display = ('name_agency','comments','update_at')


class SecureAdmin(admin.ModelAdmin):
    fields = ('name_secure','comments',)
    list_display = ('name_secure','comments','update_at')


class RenewAdmin(admin.ModelAdmin):
    fields = ('name_renew','comments',)
    list_display = ('name_renew','comments','update_at')


class ClienteAdmin(admin.ModelAdmin):
    fields = ('name','renew','cpf','cnpj','prod','agency','secure','conta','gerency','policy','amount_paid','tel1','tel2','cel1','cel2','email','comments','date_contract',)
    list_display = ('name','renew','cpf','cnpj','prod','agency','secure','gerency','conta','policy','amount_paid','tel1','tel2','cel1','cel2','email','comments','date_contract',)


admin.site.register(AuthUser, AuthUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Secure, SecureAdmin)
admin.site.register(Renew, RenewAdmin)
admin.site.register(Cliente, ClienteAdmin)
