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

    context = {}
    return render(request, 'StudentTrackingSystemApp/homepage.html', context)
