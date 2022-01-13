import matplotlib.pyplot as plt
from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import *
import pandas as pd
import matplotlib.pyplot as plt

def Home(request):
    if request.method == "GET":
        return render(request, 'login/loginpage.html')


    if request.method == "POST":
        name = request.POST['u-name']
        passw = request.POST['u-passw']


        if name == 'ITQAN' and passw == 'ITQAN#9696' :
            return render(request, 'login/success.html')
        else:
            return render(request, 'login/unsuccess.html')


# def form(request):
#     if request.method == "GET":
#         return render(request, 'login/loginpage.html')
#
#
#     if request.method=="POST":
#         name = request.POST['u-name']
#         passw = request.POST['u-passw']
#
#
#         if name == 'ITQAN' and passw == 'ITQAN#9696' :
#             return render(request, 'login/success.html')
#         else:
#             return render(request, 'login/unsuccess.html')

def color(request):

    if request.method == "GET":
        return render(request, 'login/homepage.html')


    elif request.method == "POST":

        color = request.POST.get('green',False)
        if color == '':
            context = {
                'colour': 'darkgreen'

            }
            return render(request, 'login/homepage.html', context)

        color1 = request.POST.get('blue',False)
        if color1 == '':
            context = {
                'colour': 'darkblue'

            }
            return render(request, 'login/homepage.html', context)


        color2 = request.POST.get('yellow',False)
        if color2 == '':
            context = {
                'colour': 'yellow'

            }
            return render(request, 'login/homepage.html', context)

        color3 = request.POST.get('navyblue',False)
        if color3 == '':
            context = {
                'colour': 'deepskyblue'

            }
            return render(request, 'login/homepage.html', context)


def feedback(request):
    if request.method == "GET":
        # info = person_performance_details.objects.all()
        # context = {
        #     'information' : info
        # }

        return render(request, 'login/details.html')


    if request.method=="POST":
        Name = request.POST['name']
        Position = request.POST['Position']
        date = request.POST['bdate']
        availability = request.POST['Availability']
        performance = request.POST['Performance']
        Task = request.POST['Task']
        Work_activity = request.POST['Work_activity']

        performance_details.objects.create(name=Name, availability_in_percentage = availability,performance_in_percentage=performance,task=Task,work_activity = Work_activity,position= Position,date=date)

        return render(request, 'login/details.html')

def feedbacklist(request):
    info = performance_details.objects.all()
    context = {
        'information' : info
    }
    return render(request,'login/listoffeedback.html',context)

def Dashboardd(request):
    info = performance_details.objects.all()
    name_array = []
    date_array = []
    performance_array = []

    for i in info:
        name_array.append(i.name)
        date_array.append(i.date)
        performance_array.append(i.performance_in_percentage)
    print(name_array)
    print(performance_array)

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.bar(name_array, performance_array)


    plt.pie(performance_array, labels=name_array)

    context = {
        'information01' : fig.savefig('new03.png'),
        'information02' : plt.savefig('new04.png'),

    }


    return render(request,'login/dashboard.html',context)


def HL(request):
    if request.method == "GET":
        return render(request, 'login/ayon.html')


    if request.method == "POST":
        name = request.POST['username']
        passw = request.POST['password']

        if name == 'Halima' and passw == '123':


            return render(request,'login/Sucsess01.html')
        else:
            return render(request,'login/Unsuccessful1.html')
