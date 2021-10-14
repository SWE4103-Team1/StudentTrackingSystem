from django.shortcuts import render, redirect
from users.managers import UserManager
from users.roles import UserRole
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, logout

def registerPage(request):
	context = {}
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('psw')
		try:
			# This is most likely temporary as we will 
			# use Justen's models I assume?
			User = get_user_model()
			user = User.objects.create_user(
				email=email,
				username=email,
				password=password,
				role=UserRole.ProgramAdvisor,
			)
			return redirect('loginPage')
		except Exception as e:
			print(f'ERROR: {e}')

	return render(request, 'StudentTrackingSystemApp/register.html', context)


def loginPage(request):
	context = {}
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = authenticate(request, username=email, password=password)
			if user is not None:
				print(f'Successfully logged in user: {user}')
				# Here is where we need to redirect the user to landing page
			else:
				print(f'{user} does not exist')
				return redirect('registerPage')
		except Exception as e:
			print(f'ERROR: {e}')
	
	return render(request, 'StudentTrackingSystemApp/login.html', context)

