from django.contrib import admin
from .models import (
    People1399,
    People1400,
    Family1399,
    Family1400,
    SamePeople,
    SameFamilies,
)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ["ID", "GenderId", "BirthDate"]


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["ParentID", "MembersID"]


class SamePeopleAdmin(admin.ModelAdmin):
    list_display = ["id_1399", "id_1400"]


class SameFamiliesAdmin(admin.ModelAdmin):
    list_display = ["parentid_1399", "parentid_1400"]


admin.site.register(People1399, PeopleAdmin)
admin.site.register(People1400, PeopleAdmin)
admin.site.register(Family1399, FamilyAdmin)
admin.site.register(Family1400, FamilyAdmin)

admin.site.register(SamePeople, SamePeopleAdmin)
admin.site.register(SameFamilies, SameFamiliesAdmin)
