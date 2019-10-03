from django.contrib import admin
from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    pass
