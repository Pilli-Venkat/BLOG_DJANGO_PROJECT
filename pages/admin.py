from django.contrib import admin
from . models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_editable = ('is_resolved',)
    list_display = ('name','email','is_resolved','contacted_at','subject','message')
    list_filter = ('is_resolved','contacted_at')



# Register your models here.
admin.site.register(Contact,ContactAdmin)