from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blood_report

# Create your views here.

def developer(request):
    return render(request, "medical_report/developer.html")

@login_required(login_url='login')
def analysis(request):
    return render(request, "medical_report/blood_analysis.html")


@login_required(login_url='login')
def bloodAnalysis(request):
    blood_reports = Blood_report.objects.all()
    context = {

        'blood_reports': blood_reports,
    }
    return render(request, "medical_report/blood_analysis.html",context)

@login_required(login_url='login')
def urinAnalysis(request):
    return render(request, "medical_report/urin_analysis.html")


@login_required(login_url='login')
def addImage(request):
    return render(request, "medical_report/blood_image_add.html")

@login_required(login_url='login')
def bloodImage(request):
    return render(request, "medical_report/blood_image_add.html")

@login_required(login_url='login')
def urinImage(request):
    return render(request, "medical_report/urin_image_add.html")

