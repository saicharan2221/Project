import mysql.connector as sql
from urllib import request
from django.contrib.auth  import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.utils.decorators import method_decorator

from app.models import *
from app.forms import LeaveApplicationform
# Create your views here.

def login(request):
     if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            m=sql.connect(host="localhost",user="root",passwd="root",database='project')
            cursor=m.cursor()
            c="select * from app_user where username='{}' and password='{}' ".format(username,password)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            # ind=found[0][0]
            # print(ind)
            if(t): 
                userid=(t[0][0])
                username=(t[0][1])
                print(username)
                request.session['username'] = username
                request.session['userid'] = userid
                d={'username':username}
                return render(request,'home.html',d)
            else:

                messages.info(request,"Please Enter Valid details")
                return HttpResponseRedirect(reverse('login'))
     return render(request,'login.html')

def Admin(request):
    return render(request,'admin.html')




def home(request):
    return render(request,'home.html')

def logout(request):
    try:
      del request.session['username']
    except:
      pass
    # return HttpResponse("<strong>You are logged out.</strong>")
    # logout(request)
    messages.info(request,"Logout successfully")
    return HttpResponseRedirect(reverse('login'))
    # return render(request,'')

def employee(request):
    a={"username":request.session['username'],"userid":request.session['userid']}
    emp= Employee.objects.filter(user_id = a['userid'])
    context={
        'emp':emp
    }
    # temp=loader.get_template("employee.html")
    # return HttpResponse(temp.render(context,request))
    return render(request,'employee.html',context)



def department(request): 
    a={"username":request.session['username'],"userid":request.session['userid']}
    dep=EmpDetails.objects.filter(user_id=a['userid'])
    b=dep[0]
    c=b.dept_id
    dept= Department.objects.filter(dept_id =c)
    context={
        'dept':dept
    }
   
    return render(request,'department.html',context)



def designation(request):
    a={"username":request.session['username'],"userid":request.session['userid']}
    deg=EmpDetails.objects.filter(user_id=a['userid'])
    b=deg[0]
    c=b.desg_id      
    desg= Designation.objects.filter(desg_id =c)
    context={
        'desg':desg
    }
    return render(request,'designation.html',context)



def employee_details(request): 
    
    a={"username":request.session['username'],"userid":request.session['userid']}
    emp_details= EmpDetails.objects.filter(user_id = a['userid'])
    context={
        'emp_details':emp_details
    }
    return render(request,'employee_details.html',context)



def leaves(request):
    a={"userid":request.session['userid']}
    lv=Leaves.objects.filter(user_id=a['userid'])
    det=LeaveApplication.objects.filter(user_id=a['userid'])        
    ep=EmpDetails.objects.filter(user_id=a['userid'])
    e=Employee.objects.filter(user_id=a['userid'])
    context={
        'lv':lv,
         'det':det,
         'ep':ep,
         'e':e,
    }

    return render(request,'leaves.html',context)


def leaveapplication(request):
    a={"userid":request.session['userid']}
    ap=AppUser.objects.filter(user_id=a['userid'])
    print(ap[0].user_id)
    # print(a)
    # lv=Leaves.objects.filter(user_id=a['userid'])
    lvu=LeaveApplication(user_id=ap[0].user_id)
    lvu.save()

    form=LeaveApplicationform(request.POST)
    if form.is_valid():
        form.user_id=a['userid']
        print(a['userid'])
        form.save()
    context={'form':form}
    return render(request,'leaveapplication.html',context)
