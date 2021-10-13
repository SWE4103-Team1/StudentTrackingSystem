from django.shortcuts import render
from users.managers import UserManager
from django.contrib.auth.forms import UserCreationForm
from users.roles import UserRole
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, logout

def createAccountPage(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('psw')
		username = request.POST.get('username')
		try:
			User = get_user_model()
			user = User.objects.create_user(
				email=email,
				password=password,
				username=username,
				role=UserRole.ProgramAdvisor,
			)
			context = {}
			return render(request, 'StudentTrackingSystemApp/login.html', context)
		except ValueError:
			print("Error")
	form = UserCreationForm()	
	context = {'form':form}
	return render(request, 'StudentTrackingSystemApp/createAccount.html', context)


def loginPage(request):
	context = {}
	if request.method == 'POST':
		
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = authenticate(request, username=username, password=password)
			if user is not None:
				print(user)
				print("loginSuccessful")
				return render(request, 'StudentTrackingSystemApp/createAccount.html', context)
			else:
				return render(request, 'StudentTrackingSystemApp/login.html', context)
		except:
			print("error")
		print(f'{username} : {password}')		
	
	return render(request, 'StudentTrackingSystemApp/login.html', context)

