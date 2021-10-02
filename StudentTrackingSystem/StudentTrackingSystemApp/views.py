from django.shortcuts import render

def loginPage(request):
	# Reminds: context is a dictionary mapping template variable names to Python objects.
	context = {}
	return render(request, 'StudentTrackingSystemApp/login.html', context)