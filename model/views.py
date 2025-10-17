from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from model.models import Student
class CreatestudentView(View):
    def get(self,request):
        return render(request,"student_details.html")
    
    def post(self,request):
        print(request.POST)
        Student.objects.create(name =request.POST.get('username'),
                                  roll_no =request.POST.get('userrollno'),
                                   department=request.POST.get('userdepartment'),
                                    email=request.POST.get('useremail'),
                                    marks=request.POST.get('usermarks'),
                                      )
        return render(request,"student_details.html")

class UpdateStudent(View):
    def get(self,request):
        stu_data=Student.objects.get(id=1)
        return render(request,"student_update.html", {"stu_data":stu_data})   

    def post(self,request):  
        stu_data=Student.objects.get(id=1)
        print(request.POST)
        stu_data.name =request.POST.get("username")
        stu_data.roll_no =request.POST.get("userrollno")
        stu_data.department =request.POST.get("userdepartment")
        stu_data.email =request.POST.get("useremail")
        stu_data.marks =request.POST.get("usermarks")
        stu_data.save()
        return render(request,"student_update.html")
    
class StudentdeleteView(View):
    def get(self,request,**kwargs):
        delete_id =kwargs.get("pk")
        stu_data =Student.objects.get(id=delete_id)
        stu_data.delete()
        return render(request,"student_details.html")

