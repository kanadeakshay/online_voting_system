from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Region)
admin.site.register(Admin)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Election)
admin.site.register(History)