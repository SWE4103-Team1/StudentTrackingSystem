from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponse

from audits import audit


def audit_student_api(request):
    # get student num from somewhere
    student_num = 123
    audit_response = audit.audit_student(student_num)
    return JsonResponse(audit_response)
