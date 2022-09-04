from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def developer(request):
    return render(request, "medical_report/developer.html")

@login_required(login_url='login')
def analysis(request):
    return render(request, "medical_report/analysis.html")


@login_required(login_url='login')
def addImage(request):
    return render(request, "medical_report/addImage.html")

