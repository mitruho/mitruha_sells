from django.contrib import admin
from .models import Item
from .models import AboutPage
from .forms import AboutPageAdminForm
@admin.register(Item)

class AboutPageAdmin(admin.ModelAdmin):
    form = AboutPageAdminForm

admin.site.register(AboutPage, AboutPageAdmin)
