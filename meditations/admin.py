from django.contrib import admin


from meditations.models import Meditation



@admin.register(Meditation)
class MeditationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}






