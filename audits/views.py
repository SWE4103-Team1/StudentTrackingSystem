from django.shortcuts import render, HttpResponse
from django.shortcuts import HttpResponse

from audits import audit


def audit_student_api(request):
    audit_response = audit.audit_student()
    return HttpResponse({})
