from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from audits import audit


@csrf_exempt
def audit_student_api(request, student_num):
    print("in audit student")
    if request.method == "GET":
        try:
            audit_response, _, _ = audit.audit_student(student_num)
            return JsonResponse(audit_response.data)
        except KeyError as e:
            return HttpResponse(e.__str__(), status=404)  # student num not found
        except BaseException as e:
            return HttpResponse(status=500)  # audit error

    return HttpResponse(status=405)  # incorrect HTTP method
