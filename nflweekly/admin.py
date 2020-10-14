from django.contrib import admin
from nflweekly.models import Week

# Register your models here.
class WeekAdmin(admin.ModelAdmin):
    pass

admin.site.register(Week, WeekAdmin)
