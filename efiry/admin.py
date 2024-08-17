from django.contrib import admin


from efiry.models import Efir



@admin.register(Efir)
class EfirsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}