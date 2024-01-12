from django.contrib import admin
from .models import Company, Unit , Branch, Department, Division, Position, User, Employee, Prefix

admin.site.register(Company)
admin.site.register(Unit)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Position)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Prefix)

# Register your models here.
