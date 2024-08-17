from django.contrib import admin


from club.models import Schedule



@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}