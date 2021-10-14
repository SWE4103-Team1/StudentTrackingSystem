from dataloader.load_extract import _uploadAllFiles
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
    return render(request, 'StudentTrackingSystemApp/student_data.html', context)

def course_data(request):
    from datamodel.models import Course

    all_entries = Course.objects.all()
    print(all_entries)
    context = {
        "object_list": all_entries
    }
    return render(request, 'StudentTrackingSystemApp/course_data.html', context)

def enrolment_data(request):
    from datamodel.models import Enrolment

    all_entries = Enrolment.objects.all()
    print(all_entries)
    context = {
        "object_list": all_entries
    }
    return render(request, 'StudentTrackingSystemApp/Enrolment_data.html', context)
    