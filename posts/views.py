from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("bonjour")
def view1(request):
  return HttpResponse("ahmed")
def view2(request):
  return HttpResponse("fatimetou")
def view3(request):
  return HttpResponse("sidahmed")
def somme(request):
   # "<input type='int' name="a" value=''></input>
    a=int(input("donner a"))
    b=int(input("donner b"))
    print (a+b)
    return HttpResponse('<h1> la somme de a + b ='+ str(a+b) + '. </h1>')