from django.contrib import admin


from practicums.models import Practicums



@admin.register(Practicums)
class PracticumsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}






