from dataloader.load_extract import DataFileExtractor
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from users.roles import UserRole
from StudentTrackingSystemApp import configfuncs, rankings
from django.utils.datastructures import MultiValueDictKeyError
from datamodel.models import Student
from django.views.decorators.csrf import csrf_exempt


def registerPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("psw")
        try:
            User = get_user_model()
            user = User.objects.create_user(
                email=email,
                username=email,
                password=password,
                role=UserRole.ProgramAdvisor,
            )
            return redirect("loginPage")
        except Exception as e:
            print(f"ERROR: {e}")
            context = {
                "error": "An account with that email already exists. Please create another account."
            }
            return render(request, "StudentTrackingSystemApp/register.html", context)

    context = {"error": ""}
    return render(request, "StudentTrackingSystemApp/register.html", context)


def loginPage(request):
    context = {"error": ""}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                print(f"Successfully logged in user: {user}")
                login(request, user)
                # Here is where we need to redirect the user to landing page
                return redirect("dashboard")
            else:
                print(f"{user} does not exist")
                context = {"error": "Invalid login credentials. Please try again."}
                return render(request, "StudentTrackingSystemApp/login.html", context)
        except Exception as e:
            print(f"ERROR: {e}")

    return render(request, "StudentTrackingSystemApp/login.html", context)


def logout_view(request):
    context = {"error": "Logged out successfully"}

    logout(request)

    return redirect("loginPage")


def redirectLogin(request):
    context = {}
    return redirect("loginPage")


# able to read in files
def settings(request):
    if request.method == "POST":

        personData, courseData, transferData = None, None, None

        # files will hold all the data files that are read in
        data_files = request.FILES.getlist("data_files")
        if data_files:
            if not configfuncs.config_file_exist():
                print(f"Can't Submit Data Files without Config Files")
                context = {
                    "DataError": "No Configuration File Found: Must Upload Configuration Files Before Data Files"
                }
                return render(
                    request, "StudentTrackingSystemApp/settings.html", context
                )
            elif not rankings.prereq_exist():
                print(f"Can't Submit Data Files without Pre-Reqs Files")
                context = {
                    "DataError": "No Prerequisites File Found: Must Upload Prerequisites Files Before Data Files"
                }
                return render(
                    request, "StudentTrackingSystemApp/settings.html", context
                )
            else:
                for f in data_files:
                    if f.name == "personData.txt":
                        personData = f
                    elif f.name == "courseData.txt":
                        courseData = f
                    elif f.name == "transferData.txt":
                        transferData = f

                if not personData or not courseData or not transferData:
                    context = {
                        "DataError": "No Data File Found: Must upload 'personData.txt', 'courseData.txt' and 'transferData.txt' together"
                    }
                    return render(
                        request, "StudentTrackingSystemApp/settings.html", context
                    )

                uploader = DataFileExtractor()
                uploader.uploadAllFiles(personData, courseData, transferData)

        # config file holds a single config excel file
        try:
            config_file = request.FILES["config_file"]
            if config_file:
                configfuncs.set_config_file(config_file)
        except MultiValueDictKeyError:
            pass

        # pre-req files holds a single prereq config excel file
        try:
            prereq_file = request.FILES["prereq_file"]
            if prereq_file:
                rankings.set_prereq_file(prereq_file)
        except MultiValueDictKeyError:
            pass

    context = {}
    return render(request, "StudentTrackingSystemApp/settings.html", context)


@csrf_exempt
def dashboard(request):
    context = {}
    return render(request, "StudentTrackingSystemApp/Dashboard/index.html", context)


def student_data(request):
    from datamodel.models import Student

    all_entries = Student.objects.all()
    context = {"object_list": all_entries}
    return render(request, "StudentTrackingSystemApp/Student_Data.html", context)


def course_data(request):
    from datamodel.models import Course

    all_entries = Course.objects.all()
    context = {"object_list": all_entries}
    return render(request, "StudentTrackingSystemApp/Course_Data.html", context)


def enrolment_data(request):
    from datamodel.models import Enrolment

    all_entries = Enrolment.objects.all()

    context = {"object_list": all_entries}
    return render(request, "StudentTrackingSystemApp/Enrolment_Data.html", context)


def get_student_data_api(request):
    from datamodel.models import Student, UploadSet
    from django.core import serializers
    from django.shortcuts import HttpResponse

    serializedData = serializers.serialize(
        "json",
        Student.objects.filter(
            upload_set=UploadSet.objects.order_by("upload_datetime").last()
        ),
    )
    return HttpResponse(serializedData)


def get_counts_by_semester(request, semester):
    from json import dumps
    from django.shortcuts import HttpResponse
    from generateCounts.counts import (
        count_coop_students_by_semester,
        count_total_students_by_semester,
        count_students_by_rank_semester,
    )

    countCoop = count_coop_students_by_semester(semester)
    countTotal = count_total_students_by_semester(semester)
    countRank = count_students_by_rank_semester(semester)

    data = {
        "countCoop": countCoop,
        "countTotal": countTotal,
        "FIR": countRank["FIR"],
        "SOP": countRank["SOP"],
        "JUN": countRank["JUN"],
        "SEN": countRank["SEN"],
    }
    return HttpResponse(dumps(data))


def get_counts_by_cohort(request, cohort):
    from json import dumps
    from django.shortcuts import HttpResponse
    from generateCounts.counts import (
        count_coop_students_by_cohort,
        count_total_students_by_cohort,
        count_students_by_rank_cohort,
    )

    countCoop = count_coop_students_by_cohort(cohort)
    countTotal = count_total_students_by_cohort(cohort)
    countRank = count_students_by_rank_cohort(cohort)

    data = {
        "countCoop": countCoop,
        "countTotal": countTotal,
        "FIR": countRank["FIR"],
        "SOP": countRank["SOP"],
        "JUN": countRank["JUN"],
        "SEN": countRank["SEN"],
    }

    return HttpResponse(dumps(data))


def get_count_parameters_api(request):
    from json import dumps
    from django.shortcuts import HttpResponse
    from datamodel.models import Student, Enrolment

    cohorts = []
    semesters = []

    startDates = Student.objects.values("start_date").distinct()
    for date in startDates:
        start_date = date["start_date"].strftime("%Y-%m")
        year = start_date[:4]
        month = start_date[5:]

        # If a student starts in sept then they are a part of the
        # currentYear-nextYear cohort
        # If a student starts in the winter or summer term, then they are
        # a part of the previousYear-currentYear cohort
        cohort = []
        if int(month) == 9:
            cohort = [year, "-", str(int(year) + 1)]
        else:
            cohort = [str(int(year) - 1), "-", year]

        cohorts.append("".join(cohort))

    # Remove dupliactes and sort list
    cohorts = list(dict.fromkeys(cohorts))
    cohorts.sort(reverse=True)

    enrollmentTerms = Enrolment.objects.values("term").distinct()
    for term in enrollmentTerms:
        semester = term["term"]
        semesters.append(semester)

    semesters.sort(reverse=True)
    semesters = semesters[1:]  # THIS IS TO REMOVE A STUPID WEIRD T AT THE FRONT

    return HttpResponse(dumps({"cohorts": cohorts, "semesters": semesters}))


def get_transcript(request, student_num=0):
    from django.shortcuts import HttpResponse
    from datamodel.models import Enrolment
    import json

    all_entries = Enrolment.objects.filter(student__student_number=student_num)

    student_transcript = []
    for entry in all_entries:
        transcript = {
            "Course_Code": entry.course.course_code,
            "Course_Name": entry.course.name,
            "Course_Type": entry.course.course_type,
            "Semester": entry.term,
            "Section": entry.course.section,
            "Credit_Hours": entry.course.credit_hours,
            "Grade": entry.grade,
        }
        student_transcript.append(transcript)

    jsonstrMast = json.dumps(student_transcript)
    return HttpResponse(jsonstrMast)
