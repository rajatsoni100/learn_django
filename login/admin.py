from django.contrib import admin
from .models import NewUser

class NewUserAdmin(admin.ModelAdmin):
	list_display = ['pk','name','email','password','timestamp']
	class Meta:
		model = NewUser

admin.site.register(NewUser, NewUserAdmin)