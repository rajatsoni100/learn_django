from django.shortcuts import render

# Create your views here.

def index(request):
	template='index.html'
	name = "RAJAt"
	#new_dict = {'var_first_name':name,'var_last_name':'SONI'}
	return render(request, template, {'var_first_name':name,'var_last_name':'SONI'})
