from django.contrib import admin
from .models import People1399, People1400, Family1399, Family1400


class PeopleAdmin(admin.ModelAdmin):
    list_display = ["ID", "GenderId", "BirthDate"]


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["ParentID", "MembersID"]


admin.site.register(People1399, PeopleAdmin)
admin.site.register(People1400, PeopleAdmin)
admin.site.register(Family1399, FamilyAdmin)
admin.site.register(Family1400, FamilyAdmin)
