from django.contrib import admin
from .models import People1399, People1400


class PeopleAdmin(admin.ModelAdmin):
    list_display = ["ID", "GenderId", "BirthDate"]


admin.site.register(People1399, PeopleAdmin)
admin.site.register(People1400, PeopleAdmin)
