from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict={"Name":"Kamta"}
    return render(request,'templatesApp/firstTemplate.html',context=myDict)

def renderEmployee(request):
    myDict={"id":123,"Name":"Kunal","Sal":10000}
    return render(request,'templatesApp/employeeTemplate.html',myDict)