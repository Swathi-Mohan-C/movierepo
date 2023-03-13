from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import person
# Create your views here.
"""def home(request):
    return render(request,"home1.html")
def about(request):
    return render(request,"abouts.html")
def contact(request):
    return HttpResponse(" -------This is the contact page----------")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse("----------Thank You------------")"""
def demo(request):
    obj=place.objects.all()
    swa = person.objects.all()
    return render(request,"index.html",{'result': obj,'results': swa})





"""def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    multi=x*y
    sub=x-y
    div=x/y
    return render(request,"abouts.html",{'result':res,'mult':multi,'subs':sub,'di':div})
"""


