from django.shortcuts import render
from modelapp.models import Student
# Create your views here.
def student__info__view(request):
    student=Student.objects.all()
    return render(request,'testapp/results.html',{'student':student})
