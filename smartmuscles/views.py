from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup
from django.views.generic.edit import CreateView



# Create your views here.
def index(request):
    return HttpResponse("hello elgar")

def get_members(request):
    response=Signup.objects.all()
    return HttpResponse(response) 


    #CLASS BASED VIEWS

class MemberCreate(CreateView):
    model=Signup
    fields=['name','email','password']

