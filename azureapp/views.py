from django.shortcuts import render
from .models import Person

# Create your views here.
def display_data(request):
    persons=Person.objects.all()
    return render(request,'azureapp/display_data.html',{'persons': persons})
