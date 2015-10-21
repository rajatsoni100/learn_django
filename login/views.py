from django.shortcuts import render

# Create your views here.

def index(request):
	template='index.html'
	print request.method
	return render(request, template)
