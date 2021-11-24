from dataloader.load_extract import DataFileExtractor
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from generateCounts.counts import *
from users.roles import UserRole
from StudentTrackingSystemApp import configfuncs, rankings
from django.utils.datastructures import MultiValueDictKeyError


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
                context = {
                    "error": "Invalid login credentials. Please try again."}
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
                    "DataError": "No Configuration File Found: Must Upload Configuration Files Before Data Files"}
                return render(request, "StudentTrackingSystemApp/settings.html", context)

            else:
                for f in data_files:
                    if f.name == "personData.txt":
                        personData = f
                    elif f.name == "courseData.txt":
                        courseData = f
                    elif f.name == "transferData.txt":
                        transferData = f

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
                if not rankings.prereq_exist():
                    # write code here to pass msg to front
                    pass
                rankings.set_prereq_file(prereq_file)
                print(prereq_file)
        except MultiValueDictKeyError:
            pass

    context = {}
    return render(request, "StudentTrackingSystemApp/settings.html", context)


def dashboard(request):
    context = {
        "coopSemester": "",
        "totalSemester": "",
        "coopStartDate": "",
        "totalStartDate": "",
        "rankSemester": "",
    }

    if request.method == "POST":
        semester = request.POST.get("semester")
        start_date = request.POST.get("start_date")

        try:
            context["coopSemester"] = str(
                count_coop_students_by_semester(semester))
            context["totalSemester"] = str(
                count_total_students_by_semester(semester))
            context["coopStartDate"] = str(
                count_coop_students_by_start_date(start_date)
            )
            context["totalStartDate"] = str(
                count_total_students_by_start_date(start_date)
            )
            context["rankSemester"] = str(count_students_by_rank(semester))

            return render(
                request, "StudentTrackingSystemApp/Dashboard/index.html", context
            )

        except Exception as e:
            print(f"ERROR: {e}")

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
    from datamodel.models import Student
    from django.core import serializers
    from django.shortcuts import HttpResponse

    serializedData = serializers.serialize(
        "json", Student.objects.filter(upload_set=UploadSet.objects.first())
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


def get_counts_by_start_date(request, start_date):
    from json import dumps
    from django.shortcuts import HttpResponse
    from generateCounts.counts import (
        count_coop_students_by_start_date,
        count_total_students_by_start_date,
        count_students_by_rank_start_date,
    )

    countCoop = count_coop_students_by_start_date(start_date)
    countTotal = count_total_students_by_start_date(start_date)
    countRank = count_students_by_rank_start_date(start_date)

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
        cohorts.append(date["start_date"].strftime("%Y-%m-%d"))

    enrollmentTerms = Enrolment.objects.values("term").distinct()
    for term in enrollmentTerms:
        semesters.append(term["term"])

    return HttpResponse(dumps({"cohorts": cohorts, "semesters": semesters}))


def get_transcript(request, student_num=0):
    from django.shortcuts import HttpResponse
    from datamodel.models import Enrolment
    import json
    from django.core import serializers

    # get student id
    student_ID = Student.objects.filter(student_number=student_num)
    student_django_id = student_ID[0].id
    all_entries = Enrolment.objects.filter(student_id=student_django_id)
    print(all_entries[1])
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
        jsonstr = json.dumps(transcript)
        student_transcript.append(transcript)

    jsonstrMast = json.dumps(student_transcript)
    return HttpResponse(jsonstrMast)
