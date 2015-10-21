from django.shortcuts import render
from .models import NewUser
# Create your views here.

def index(request):
	template='index.html'
	name = "RAJAt"
	
	# users = NewUser.objects.all()
	user = NewUser.objects.get(pk=4)
	#new_dict = {'var_first_name':name,'var_last_name':'SONI'}
	
	return render(request, template, {'user':user})
