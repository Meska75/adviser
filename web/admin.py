from django.contrib import admin
from web.models import Contact

# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    date_hierarchy = "create_date"
    list_display = ("name" , "subject" , "email" , "create_date")
    ordering = ('create_date',)
    search_fields = ('subject','name','email',)

admin.site.register(Contact,ContactAdmin)
