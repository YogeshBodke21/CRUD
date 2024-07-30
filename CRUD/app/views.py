from django.shortcuts import render, redirect
from .forms import StudentForm, StudentRegistrationForm
from .models import StudentInfo
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def Student_retrieve(request):
    template_name = "app/index.html"
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
        form = StudentForm()
    obj = StudentInfo.objects.all()
    return render (request, template_name, {"form":form, "obj":obj})


def delete_view(request, pk):
    obj1 = StudentInfo.objects.get(id=pk)
    if request.method == "POST":
        obj1.delete()
    return redirect ("retrieve")

def update_view(request, pk):
    obj = StudentInfo.objects.get(id=pk)
    form = StudentForm(instance=obj)
    template_name = "app/updatepage.html"
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid:
            form.save()
            return redirect("retrieve")
    return render (request, template_name, locals())



class StudentRegistrationView(View):
    def get(self, request):
        form = StudentRegistrationForm()
        return render (request, "app/signupform.html", locals())
    
    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulation, You have register successfully.")
            return redirect("login")

        return render (request, "app/signupform.html", locals())
    


def signin_view(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        pw = request.POST.get("passw")
        user = authenticate(username=un, password=pw)
        print("-----", user)
        if user is not None:
            login(request, user)
            return redirect("retrieve")
        
    return render (request, "app/loginform.html")


def logout_view(request):
    logout(request)
    return redirect ('login')
