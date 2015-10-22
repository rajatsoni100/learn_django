from django.contrib import admin
from .models import NewUser, Branch, Advertisement

class NewUserAdmin(admin.ModelAdmin):
	list_display = ['pk','name','branch','email','password','timestamp']
	class Meta:
		model = NewUser

class BranchAdmin(admin.ModelAdmin):
	list_display = ['code','name','section']
	class Meta:
		model = Branch

class AdvertisementAdmin(admin.ModelAdmin):
	list_display = ['title','description','user']
	class Meta:
		model = Advertisement

admin.site.register(NewUser, NewUserAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)