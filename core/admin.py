from django.contrib import admin

from .models import Request, Donation, ClosedRequest

admin.site.register(Request)
admin.site.register(Donation)
admin.site.register(ClosedRequest)
