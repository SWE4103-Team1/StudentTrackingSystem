from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from audits import audit


@csrf_exempt
def audit_student_api(request, student_num):
    if request.method == "GET":
        try:
            audit_response, _, _ = audit.audit_student(student_num)
            return JsonResponse(audit_response.data)
        except KeyError as e:
            return HttpResponse(e.__str__(), status=404)  # student num not found
        except BaseException as e:
            import traceback

            traceback.print_exc()
            return HttpResponse(status=500)  # audit error

    return HttpResponse(status=405)  # incorrect HTTP method


@csrf_exempt
def bulk_student_audit_api(request):
    if request.method == "POST":
        try:

            audit_response, _, _ = audit.audit_student(student_num)
            return JsonResponse(audit_response.data)
        except KeyError as e:
            return HttpResponse(e.__str__(), status=404)  # student num not found
        except BaseException as e:
            import traceback

            traceback.print_exc()
            return HttpResponse(status=500)  # audit error

    return HttpResponse(status=405)  # incorrect HTTP method

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
