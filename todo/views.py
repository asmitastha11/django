from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

# contact, about....
def contact(request):
    person = [
        {
        "name":"ram",
        "age":25,
    },
    {
        "name":"shyam",
        "age":15,
    },
    {
        "name":"sita",
        "age":21,
    },
    {
        "name":"gita",
        "age":25,
    },
    {
        "name":"asmita",
        "age":25,
    },
    {
        "name":"lia",
        "age":50,
    }
 ]
    context = {
        "name":"Contact Page",
        "person":person
    }
    return render(request,'contact.html',context)

# def contact(request):
#     return HttpResponse("contact details")