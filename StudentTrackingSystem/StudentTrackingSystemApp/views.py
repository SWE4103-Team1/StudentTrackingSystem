from django.shortcuts import render
from dataloader.load_extract import _uploadAllFiles

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
