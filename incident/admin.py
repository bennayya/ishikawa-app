"""from django.contrib import admin
#from .models import incident 
#admin.site.register(incident)

# Register your models here.
from .models import Incident
admin.site.register(Incident)
"""

from django.contrib import admin
from .models import Incident
admin.site.register(Incident)
