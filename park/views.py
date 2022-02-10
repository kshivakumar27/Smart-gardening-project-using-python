
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import Sensorstatesupdate
from django.contrib.auth.models import User , auth
from .models import *
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .form import *
from django.core.mail import EmailMessage
from django.template.loader import get_template

from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from .serializers import *
from .models import FeedbackForm

def home(request):
    return render(request,'home.html')

def adminpage(request):
    return render(request,'Admin.html')


def administrator(request):
    return render(request,'administratorupdate.html')


def administrators(request):
    print("Hello form is submitted")
    previous_temparature_value = request.POST.get('previous_temparature_value')
    present_temparature_value = request.POST.get('present_temparature_value')
    sprinkler_state = request.POST.get('sprinkler_state')

    previous_humidity_value = request.POST.get('previous_humidity_value')
    present_humidity_value = request.POST.get('present_humidity_value')
    water_pump_state = request.POST.get('water_pump_state')


    street_light_state = request.POST.get('street_light_state')
    alarm_state = request.POST.get('alarm_state')
#    next_update_time = request.POST.get('next_update_time')
    description = request.POST.get('description')


    
    adminupdate = AdminUpdates(previous_temparature_value=previous_temparature_value,present_temparature_value=present_temparature_value,sprinkler_state=sprinkler_state,previous_humidity_value=previous_humidity_value,present_humidity_value=present_humidity_value,water_pump_state=water_pump_state,street_light_state=street_light_state,alarm_state=alarm_state,description=description)
    adminupdate.save()
    return render(request,'admin.html')
    






def registerpage(request):
    return render(request,'register.html')



def loginpage(request):
    return render(request,'login.html')


def information(request):
    return render(request,'info.html')

def review(request):
    return render(request,'review.html')

def alarm(request):
    return render(request,'alarm.html')





def backtohome(request):
    return render(request,'home.html')

def mainpage(request):
    return render(request,'new.html')




def loginmethod(request):
     username   = request.POST['username']
     password   = request.POST['password']

     user = auth.authenticate(username = username , password=password)
#     return render(request,'new.html')

     if user is not None:
         auth.login(request,user)
         return redirect('new.html')
     else:
        messages.info(request,'invalid Credentials')
        print('invalid Credentials')
        return redirect('login.html')

#     return render(request,'new.html')




#def register(request):
#    if request.method == 'POST':
 #       first_name =request.POST['first_name']
  #      last_name = request.POST['last_name']
   #     username = request.POST['username']
    #    email = request.POST['email']
     #   password1 = request.POST['password1']
      #  password2 = request.POST['password2']

#        if password1==password2:
      #      if User.objects.filter(username=username).exists():
       #         messages.info(request,'Username taken')
	#        return redirect('/')
         #   elif User.objects.filter(email=email).exists():
	#	messages.info(request,'Email Taken'),
	 #       return redirect('/')
	  #  else:
           #     user = User.objects.create_user(username=username, password=password2, email=email,name=first_name,)
            #    user.save();
             #   print("usercreated")
#            return redirect('loginpage')
 #       else:
  #          print("password not matching")
   #         return redirect('/')

#    else:
 #       return render(request,'register.html')




#Register
def register(request):
    
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        email      = request.POST['email']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                print("User is not created... Username already exists")
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email-ID already exists with a registered User')
                 print("User is not created... Email ID exists")
                 return redirect('registerpage')
            else:
                 user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                 user.save();
                 print("User Created")
                 return render(request,'login.html')
        else:
            print("User is not created...")
            print("Password not matching...")
            messages.info(request,'Password not matching...')
            return redirect('registerpage')






#def plastic(request):
 #   return render(request,'plastic.html')


def p2l(request):
    return render(request,'p2l.html')

def humidity(request):
    return render(request,'humidity.html')






def temp(request):

#    dests = Sensorstateupdate.objects.all()

    return render(request,'temp.html')

def review(request):
    return render(request,'review.html')

def review1(request):
    return render(request,'review1.html')





def sensorupdate(request):
    tempstatus=Sensorstatesupdate.objects.all
    return render(request,'temp.html',{'all':tempstatus})


def review(request):

    rev = Register.objects.all()

    return render(request, "review.html", {'all4': rev})






def feedback(request):
    Feedback_form = FeedbackForm
    if request.method == 'POST':
  #      form = Feedback_Form(data=request.POST)

 #       if form.is_valid():
            u_name = request.POST.get('u_name')
            u_email = request.POST.get('u_email')
            u_phone = request.POST.get('u_phone')
            u_rate = request.POST.get('u_rate')
            u_suggestion = request.POST.get('u_suggestion')
            u_review = request.POST.get('u_review')

            feeedback_content = request.POST.get('content')

            template = get_template('park/feedback_form.txt')
            context = {
                'u_name' : u_name,
                'u_email' : u_email,
                'u_phone' : u_phone,
                'u_rate' : u_rate,
                'u_suggestion' : u_suggestion,
                'u_review' : u_review,
 #               'feedback_content' : feedback_content,
            }
            
            content = template.render(context)

            email = EmailMessage(
                "New feedback form email",
                content,
                "Creative web" + '',
                ['kshivakumar7227@gmail.com'],
                headers = { 'Reply To': u_email }
            )

            email.send()

            return redirect('park:success')
  #  return render(request, 'park/feedback.html', {'form':Feedback_Form })


def feedback1(request):
    return render(request,'feedback1.html')

def Feedbackreview(request):
    print("Hello form is submitted")
    u_name = request.POST.get('u_name')
    u_email = request.POST.get('u_email')
    u_phone = request.POST.get('u_phone')
    u_date = request.POST.get('u_date')
    u_rate = request.POST.get('u_rate')
    u_suggestion = request.POST.get('u_suggestion')
    u_review = request.POST.get('u_review')
    feed_back = FeedbackForm(u_name=u_name,u_email=u_email,u_phone=u_phone,u_date=u_date,u_rate=u_rate,u_suggestion=u_suggestion,u_review=u_review)
    feed_back.save()
    return render(request,'new.html')



def viewdetails(request):
    view = AdminUpdates.objects.all
    return render(request,'viewdetails.html',{'all':view})

def Feedbackview(request):
    Feed = FeedbackForm.objects.all
    return render(request,'Feedbackview.html',{'all1':Feed})


def adminlogin(request):
     username   = request.POST['username']
     password   = request.POST['password']

     user = auth.authenticate(username = username , password=password)
#     return render(request,'new.html')

     if user is not None:
         auth.login(request,user)
         return redirect('administratorupdate.html')
     else:
        messages.info(request,'invalid Credentials')
        print('invalid Credentials')
        return redirect('Admin.html')


def sprinkler(request):
    previous_temparature_value = request.POST.get('previous_temparature_value')
    present_temparature_value = request.POST.get('present_temparature_value')
    sprinkler_state = request.POST.get('sprinkler_state')
#  #  next_update_time = request.POST.get('next_update_time')
    description = request.POST.get('description')
    sprin = sprinklerstatus(previous_temparature_value=previous_temparature_value,present_temparature_value=present_temparature_value,sprinkler_state=sprinkler_state,description=description)
    sprin.save()
    
    if present_temparature_value >= previous_temparature_value:
         return render(request,'temp.html')
    else:
         return render(request,'Admin.html')
    

def sprink(request):
    return render(request,'sprink.html')

def sprinklerdisplay(request):
    spin = sprinklerstatus.objects.all
    return render(request,'sprinklerdisplay.html',{'all2':spin})



def lightings(request):

    sensor_update = request.POST.get('sensor_update')
    updatetime = request.POST.get('updatetime')
    description = request.POST.get('description')
    str = Streetlightings(sensor_update=sensor_update,updatetime=updatetime,description=description)
    str.save()
    dark='0'
    if sensor_update == '0':
         return render(request,'p2l.html')
    else:
         return render(request,'Admin.html')
    

def street(request):
    return render(request,'street.html')



def streetlightsdisplay(request):
    street=Streetlightings.objects.all
    return render(request,'streetlightsdisplay.html',{'all3':street})

def water(request):
    previous_humidity_value = request.POST.get('previous_humidity_value')
    present_humidity_value = request.POST.get('present_humidity_value')
    water_state = request.POST.get('water_state')
    updatetime = request.POST.get('updatetime')
    description = request.POST.get('description')
    wat = Humidityupdation(previous_humidity_value=previous_humidity_value,present_humidity_value=present_humidity_value,water_state=water_state,updatetime=updatetime,description=description)
    wat.save()
    
    if present_humidity_value >= previous_humidity_value:
         return render(request,'humidity.html')
    else:
         return render(request,'Admin.html')

def humidityupdatepage(request):
    return render(request,'humidityupdatepage.html')



def humiditydisplay(request):
    humid=Humidityupdation.objects.all
    return render(request,'humiditydisplay.html',{'all5':humid})


def garbage(request):
    garbage_update = request.POST.get('garbage_update')
    updatetime = request.POST.get('updatetime')
    description = request.POST.get('description')
    ala = alarmupdate(garbage_update=garbage_update,updatetime=updatetime,description=description)
    ala.save()
    found='1'
    if garbage_update == '1':
         return render(request,'alarm.html')
    else:
         return render(request,'Admin.html')
    


def alarmupdatepage(request):
    return render(request,'alarmupdatepage.html')



def alarmdisplay(request):
    alar=alarmupdate.objects.all
    return render(request,'alarmdisplay.html',{'all6':alar})
   
#WE MAY THINK WE ARE NARTURING OUR GARDEN,BUT OF COURSE ITS OURGARDEN THATIS REALLY NURTURING US
#EVERYTHING THAT SLOW US DOWN AND FORCES PATIENCE EVERYTHING THAT SETS US BACK INTO THE SLOW CIRCLES OF NATURE IS A HELP GARDNING IS AN INSTRUMENT OF GRACE   



def tempadmindisplay(request):
    return render(request,'tempadmindisplay.html')

def humadmindisplay(request):
    return render(request,'humadmindisplay.html')

def feedadmindisplay(request):
    return render(request,'feedadmindisplay.html')

def alarmadmindisplay(request):
    return render(request,'alarmadmindisplay.html')

def streetadmindisplay(request):
    return render(request,'streetadmindisplay.html')




