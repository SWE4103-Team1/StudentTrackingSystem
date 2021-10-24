from django.contrib.auth import authenticate, get_user_model, logout, login
from django.shortcuts import redirect, render
from users.managers import UserManager
from users.roles import UserRole
from dataloader.load_extract import _uploadAllFiles


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
	context = {'error': ""}
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user = authenticate(request, username=email, password=password)
			if user is not None:
				print(f'Successfully logged in user: {user}')
				login(request, user)
				# Here is where we need to redirect the user to landing page
				return redirect('homepage')
			else:
				print(f'{user} does not exist')
				context = {'error': "Invalid login credentials. Please try again."}
				return  render(request, 'StudentTrackingSystemApp/login.html', context)
		except Exception as e:
			print(f'ERROR: {e}')
	
	return render(request, 'StudentTrackingSystemApp/login.html', context)

def logout_view(request):
	context = {'error': "Logged out successfully"}

	logout(request)
			
	return redirect('loginPage')

#able to read in files
def homePage(request):

    if request.method == 'POST':
		# files will hold all the files that are read in
        files = request.FILES.getlist('input_files')
        for f in files:
            if f.name == 'personData.txt':
                personData = f
            elif f.name == 'courseData.txt':
                courseData = f
            elif f.name == 'transferData.txt':
                transferData = f
	
        _uploadAllFiles(personData, courseData, transferData)

    context = {}
    return render(request, 'StudentTrackingSystemApp/homepage.html', context)


def student_data(request):
    from datamodel.models import Student

    all_entries = Student.objects.all()
    print(all_entries)
    context = {
        "object_list": all_entries

    }
    return render(request, 'StudentTrackingSystemApp/Student_data.html', context)

def course_data(request):
    from datamodel.models import Course

    all_entries = Course.objects.all()
    print(all_entries)
    context = {
        "object_list": all_entries
    }
    return render(request, 'StudentTrackingSystemApp/Course_data.html', context)

def enrolment_data(request):
    from datamodel.models import Enrolment

    all_entries = Enrolment.objects.all()
    # students_list_student_number = all_entries.values('student__student_number')
    # course_list_course_code = all_entries.values('course__course_code')
    # course_list_course_name = all_entries.values('course__name')

    # student_number_list = []
    # course_code_list = []
    # course_name_list = []
	
    # for s in students_list_student_number:
	#     student_number_list.append((s.get('student__student_number')))


    # for c in course_list_course_code:
	#     course_code_list.append((c.get('course__course_code')))

    # for c in course_list_course_name:
	#     course_code_list.append((c.get('course__course_name')))

    print(all_entries)
	
    context = {
		"all_objects" : all_entries,
		# "student_numbers" : student_number_list,
		# "course_code" : course_code_list,
		# "course_name" : course_name_list
    }
    return render(request, 'StudentTrackingSystemApp/enrolment_data.html', context)
    


