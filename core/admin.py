from django.contrib import admin

from .models import Request, Donation

admin.site.register(Request)
admin.site.register(Donation)