from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import JsonResponse
import paho.mqtt.client as paho
from collections import defaultdict

from sensor.models import AuthUser, Batch, Dryer, Role , Loglogin, Elevator
from sensor.models import AuthUser as AuthUserTraffic

import mysql.connector
import os
from datetime import datetime, timedelta

from django.template.loader import render_to_string

# from sensor.backend import _function as func
# from sensor import globalFunctionModel as funcModel


# MQTT_HOST = func.MQTT_HOST #"mqtt.erac.live"
# MQTT_PORT = func.MQTT_PORT
# MQTT_USERNAME = func.MQTT_HOST
# MQTT_PASS = func.MQTT_PASS
# MQTT_DEVICE = func.MQTT_DEVICE_ALL

client = paho.Client()
# print("Connecting to broker")
# comment if not using wss
# client.tls_set('/etc/ssl/certs/ca-certificates.crt')
# # client.tls_insecure_set(True)
# client.username_pw_set(MQTT_USERNAME, MQTT_PASS)
# # tutup comment
# client.connect(MQTT_HOST, MQTT_PORT, 60)

now = datetime.now()

timeselect = 12
# Create your views here.
# db = mysql.connector.connect(
#     host=host,
#     user=user,
#     passwd=passwd,
#     database=database
# ) 
class Dict(defaultdict):
    def _init_(self):
        defaultdict._init_(self, Dict)

    def _repr_(self):
        return dict._repr_(self)

def addUser(request):
    if request.session._session:
        username = ''
        username = request.session['username']
        role = request.session['lvl']
        if username:
            userid = request.session['userid']
            user = AuthUser.objects.all()
            role = Role.objects.all()
            content = {
                'username':username,
                'user':user,
                'roles':role,
                'userid':userid
            }
            # return HttpResponse(content)
            return render(request, 'sensor/user/addUser.html', content)

        else:
            error = 'Wrong credential'
            return render(request, '/', {"error": error})
    return HttpResponseRedirect('/')

def Buttonpage(request):
    dryer = Dryer.objects.all()
    if request.session._session:
        username = ''
        username = request.session['username']
        role = request.session['lvl']
        if username:
            userid = request.session['userid']
            user = AuthUser.objects.all()
            role = Role.objects.all()
            content = {
                'username':username,
                'user':user,
                'roles':role,
                'userid':userid,
                'dryer':dryer
            }
            # return HttpResponse(content)
            return render(request, 'sensor/user/Buttonpage.html', content)

        else:
            error = 'Wrong credential'
            return render(request, '/', {"error": error})
    return HttpResponseRedirect('/')

def weight(request):
    dryer = Dryer.objects.all()
    if request.session._session:
        username = ''
        username = request.session['username']
        role = request.session['lvl']
        if username:
            userid = request.session['userid']
            user = AuthUser.objects.all()
            role = Role.objects.all()
            content = {
                'username':username,
                'user':user,
                'roles':role,
                'dryer' : dryer,
                'userid':userid
            }
            # return HttpResponse(content)
            return render(request, 'sensor/weight.html', content)

        else:
            error = 'Wrong credential'
            return render(request, '/', {"error": error})
    return HttpResponseRedirect('/')

def submitweight(request):
    if request.method == "POST":
        userid = request.session['userid']
        username = request.session['username']
        # Get the posted form

        dryer_id = request.POST['dryer_id']
        data1 = request.POST['data1']

        master = Dryer.objects.get(dryer_id=dryer_id)
        master.data1 = data1
        master.save()
        return redirect('/weight')
    return redirect('/')

def sampling(request):
    dryer = Dryer.objects.all()
    if request.session._session:
        username = ''
        username = request.session['username']
        role = request.session['lvl']
        if username:
            userid = request.session['userid']
            user = AuthUser.objects.all()
            role = Role.objects.all()
            content = {
                'username':username,
                'user':user,
                'roles':role,
                'dryer' : dryer,
                'userid':userid
            }
            # return HttpResponse(content)
            return render(request, 'sensor/sampling.html', content)

        else:
            error = 'Wrong credential'
            return render(request, '/', {"error": error})
    return HttpResponseRedirect('/')

def submitsampling(request):
    dryer = Dryer.objects.all()
    if request.method == "POST":
        userid = request.session['userid']
        username = request.session['username']
        # Get the posted form

        dryer_id = request.POST['dryer_id']
        batch_id = request.POST['batch_id']
        sampling = request.POST['sampling']

        master = Dryer.objects.get(dryer_id=dryer_id)
        master = Dryer.objects.get(batch_id=batch_id)
        master.sampling = sampling
        master.save()
        return redirect('/sampling')
    return redirect('/')

def submitlimit(request):
    elevator = Elevator.objects.all()
    if request.method == "POST":
        userid = request.session['userid']
        username = request.session['username']
        # Get the posted form

        elevator_id = request.POST['elevator_id']
        climit = request.POST['climit']

        master = Elevator.objects.get(elevator_id=elevator_id)
        master.climit = climit
        master.save()
        return redirect('/currentlimit')
    return redirect('/')


def loguser(request):    
    username = ''
    username = request.session['username']
    if username:
        userid = request.session['userid']
    else:
        error = 'Wrong credential'
        return render(request, '/', {"error": error})
    return render(request, 'sensor/user/loguser.html', {'username':username})


def submitNewUser(request):
    if request.method == "POST":
        # Get the posted form
        userid = request.session['userid']
        username = request.session['username']

        uname = request.POST['uname']
        password = request.POST['password']
        fname = request.POST['fname']
        email = request.POST['email']
        active = request.POST['is_active']
        role = request.POST['lvl']
        hashed_pass = make_password(password)

        role = Role.objects.get(id=role)
        master = AuthUser(username=uname,password=hashed_pass,first_name=fname,email=email,is_active=active,date_joined=now,role=role)
        master.save()
        return redirect('/usermgt')
    return redirect('/')

def deleteUser(request, id):
    role = request.session['lvl']
    username = request.session['username']
    userid = request.session['userid']
    user = AuthUser.objects.get(id=id) 
    checkdelete = False
    if role == 1:
        username = user.username
        user.delete()
        checkdelete = True
    return redirect('/usermgt')

def updateUser(request, id):
    if request.session._session:
        username = ''
        username = request.session['username']  
        role = Role.objects.all()
        userobj = AuthUser.objects.get(id=id)

        context = {
            'username':username,
            'roles':role,
            'x': userobj,
        }

        return render(request, 'sensor/user/updateUser.html', context)

    return HttpResponseRedirect('/')

def updatingUser(request):
    if request.method == "POST":
        # Get the posted form
        userid = int(request.POST['userid'])
        uname = request.POST['uname']
        unametemp = uname
        email = request.POST['email']
        role = request.POST['lvl']
        roleOri = request.session['role']
        username = request.session['username']
        # return HttpResponse(userid)
        if roleOri == 1:
            role = roleOri
        user = AuthUser.objects.get(id=userid)
        user.username = uname
        user.email = email
        user.role = role
        user.save()

    return redirect('/usermgt')

def profileUser(request, id):
    username = ''
    username = request.session['username']
    if username:
        userid = request.session['userid']
    else:
        error = 'Wrong credential'
        return render(request, '/', {"error": error})
    user = AuthUser.objects.all().filter(id=id)
    # return HttpResponse(userupdate)
    return render(request, 'sensor/user/profileUser.html', {'user': user,'username':username})  

def usermgt(request):
    if request.session._session:
        username = ''
        username = request.session['username']
        userid = request.session['userid']
        role = request.session['lvl']
        user = AuthUser.objects.all()
        dryer=Dryer.objects.all()
        
        if username:
            userid = request.session['userid']
            context = {
                'username': username,
                'userid': userid, 
                'user': user, 
                'role': role,
                'dryer' : dryer
            }
            return render(request, 'sensor/user/usermgt.html', context)
        else:
            error = 'Wrong credential'
            return render(request, '/', {"error": error})
    return HttpResponseRedirect('/')    

# def logUserJson(request):
#     objects_list = []
#     username = request.session['username']
#     loglogin = Loglogin.objects.all().order_by('-datecreated')[:500]
#     for log in loglogin:
#         userid = log.userid
#         user = AuthUser.objects.all().filter(id=userid,username=username)
#         for usr in user:
#             d = Dict()
#             b = str(log.datecreated)
#             bb = b.split('+')
#             d["datecreated"] = bb[0]
#             d["userid"] = userid
#             d["username"] = usr.username
#             d["role"] = usr.role.level
#             objects_list.append(d)

#     return JsonResponse(objects_list, safe=False)

# def resetPassword(request,id):
#     if request.method == "POST":
#         user = AuthUser.objects.get(id=id)
#         npswd = request.POST['npswd']
#         cpswd = request.POST['cpswd']
#         # print('user:',user.username)
#         if npswd == cpswd:
#             hashed_pass = make_password(npswd)
#             # return HttpResponse(user.email)
#             user.password = hashed_pass
#             username = user.username
#             user.save()
#             try:
#                 user = AuthUserTraffic.objects.get(username=username)
#                 user.password = hashed_pass
#                 user.save()
#             except:
#                 pass
#             messages.success(request, 'Password has been changed')
#             logaction(id, 'resetpassword', '')
#             return redirect('/sYE8kSrGbwM=/updateUser/'+id+'')
#         else:
#             messages.error(request, 'Password not matched')
#             return redirect('/sYE8kSrGbwM=/updateUser/'+id+'')


def on_connect(client, userdata, flags, rc):
    print("MQTT Connected users.py")
    # switchPower()

client.on_connect = on_connect