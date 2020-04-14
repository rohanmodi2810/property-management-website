from django.contrib import admin

from . models import Customer
from . models import owner
from . models import property
from . models import sales
from .models import requirement
from .models import curr

admin.site.register(Customer)
admin.site.register(owner)
admin.site.register(property)
admin.site.register(sales)
admin.site.register(curr)
admin.site.register(requirement)
