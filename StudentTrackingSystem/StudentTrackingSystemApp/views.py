from django.shortcuts import render

def loginPage(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		print(f'{email} : {password}')
		
	context = {}
	return render(request, 'StudentTrackingSystemApp/login.html', context)

def registerPage(request):
	context = {}
	return render(request, 'StudentTrackingSystemApp/register.html', context)
