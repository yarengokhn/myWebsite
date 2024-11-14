from django.contrib import admin
from home.models import ContactFormMessage, Settings

# Register your models here.
admin.site.register(Settings)

admin.site.register(ContactFormMessage)