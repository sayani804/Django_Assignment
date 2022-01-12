from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import *
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def student_page(request):
#     return render(request, "student.html")


def homepage(request):
    
    return render(request, 'home.html')

def userSignUp(request):
    if request.method == "POST":
        fms = SignUpForm(request.POST)
        if fms.is_valid():
            fms.save()
            print("sucess")
            return redirect('/login')
    else:
        fms = SignUpForm()
    return render(request, 'signup.html', {'forms' : fms})

# User Login funtion
def userlogin(request):
	if request.method == "POST":
		fms = LoginForm(request=request, data=request.POST)
		if fms.is_valid():
			uname = fms.cleaned_data['username']
			upass = fms.cleaned_data['password']
			user = authenticate(username=uname, password=upass)
			if user is not None:
				login(request, user)
				return redirect('/studentInfoView/')
	else:
		fms = LoginForm()
	return render(request, 'userlogin.html', {'forms' : fms})


# User Logout function
def user_logout(request):
    logout(request)
    return redirect('/studentInfoView/')



def student_page(request):
    if request.method == "POST":
        form = StudentsForm( request.POST)
        print(request.POST,"@@@@@@@@")
        if form.is_valid():
            print(form,"this is form1")
            form.save()
            print("save form")
        else:
            print("something worng 1111111")

        
    form = StudentsForm()
    context = {
        'form': form 
    }

    return render(request, "student.html",context )



def student_marks_page(request):
    if request.method == 'POST':
        
        form = StudentsAcademicsForm(request.POST)
        if form.is_valid():
            form.save()
            print("suceesfully") 
        else:
            print("error")
    Academic_form = StudentsAcademicsForm()
    StudentInfo_list = StudentInfo.objects.all()
    context = {"Academic_form": Academic_form , "StudentInfo_list" :StudentInfo_list}
    return render(request, "AcademicDetails.html", context)


def studentInfoView_page(request):
    StudentInfo_list = StudentInfo.objects.all()
    print(StudentInfo_list, "Alll list")
    form = StudentsForm()
    context = {"StudentInfo_list": StudentInfo_list , 'form': form }
    return render(request, "StudentInfoView.html", context)

def studentView_page(request, rollNo):
    getStudent = StudentAcademics.objects.get(rollNo_id=rollNo)
 
    print( getStudent.maths, "!!!!!!!!!!!!!!!!")
    StudentAcademic_list = StudentAcademics.objects.all()
    context = {"StudentAcademic_list": StudentAcademic_list , "getStudent":getStudent}
    return render(request , "StudentAcademicView.html", context)



def search_page(request):
    if request.method == 'GET':  
        student_name =  request.GET.get('search')    
        print(student_name ,"###############")  
        try:
            stname = StudentInfo.objects.filter(name=student_name)
            print(stname ,"!!!!!!!!!!!!!!!!!!")
            return render(request,"StudentInfoView.html",{"stname":stname})
        except:
            print("wrong")
            return render(request,"StudentInfoView.html",{"stname":stname})
    else:
        print("nothing")
        return render(request,"StudentInfoView.html")



def EditStudentInfo(request, rollNo):
    if request.method == "POST":
        EditStudentInfo = StudentInfo.objects.get(rollNo=rollNo)
        print(EditStudentInfo,"$$$$$$$$$$")
        EditStudentInfo.name = request.POST['name']
        EditStudentInfo.student_class = request.POST['student_class']
        EditStudentInfo.school = request.POST['school']
        EditStudentInfo.mobile = request.POST['mobile']
        EditStudentInfo.address = request.POST['address']
        EditStudentInfo.save()
        print("StudentInfo edited---------------------")
    else:
        print("error!!!!!!!!!!!")

    return redirect("/studentInfoView/")

@csrf_exempt
def deleteStudentInfo(request, rollNo):
    if request.method == "DELETE":
        delete_Info =  StudentInfo.objects.get(rollNo=rollNo)
        delete_Info.delete()
        print("fffffffffffffffffffff")
    else:
        print("error @@@@@@@@@")
    return redirect("/studentInfoView/")


def geturl_page(request):
      
    # geturl =  request.GET.get('geturls')
    geturl ='https://www.geeksforgeeks.org/'
    # geturl =  request.GET.get('geturls')
    s = requests.get(geturl)
    print(s,"yyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    
    findurl =BeautifulSoup(s.text, 'html.parser')
    print(findurl,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    urls = [] 
    for link in findurl.find_all():
        data = link.get('href')
        if (data == None):
            print("error")
        else:
            urls.append(data)
            
        print(data,"0000000000000000000000000000000000")
    print(urls,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request,"UrlPageView.html" , {"urls":urls})
        