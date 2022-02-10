from django.urls import path

from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register.html",views.registerpage, name = "registerpage"),
    path("login.html",views.loginpage, name = "loginpage"),
    path("home.html",views.backtohome, name = "backtohome"),
    path("new.html",views.mainpage, name = "mainpage"),
    path("info.html",views.information, name = "information"),
    path("review.html",views.review, name = "review"),



    path("alarm.html",views.alarm, name = "alarm"),
    path("temp.html",views.temp, name = "temp"),
    path("p2l.html",views.p2l, name = "p2l"),
    path("humidity.html",views.humidity, name = "humidity"),


    path("review1.html",views.review1, name = "review1"),
    path("Admin.html",views.adminpage, name = "adminpage"),
    path("administratorupdate.html",views.administrator, name = "administrator"),
    path("sprinklerdisplay.html",views.sprinklerdisplay, name = "sprinklerdisplay"),
   
    path("feedback.html",views.feedback, name = "feedback"),
    path("feedback1.html",views.feedback1, name = "feedback1"),
    path("viewdetails.html",views.viewdetails, name = "viewdetails"),
    path("Feedbackview.html", views.Feedbackview, name="Feedbackview"),
    path("feedback",views.feedback, name = "feedback"),
    path("Feedbackview",views.feedback, name = "Feedbackview"),



    path("sensorupdate",views.sensorupdate, name = "sensorupdate"),
    path("loginmethod",views.loginmethod, name = "loginmethod"),
    path('register',views.register, name = 'register'),


    path("Feedbackreview",views.Feedbackreview, name = "Feedbackreview"),
    path("administrators",views.administrators, name = "administrators"),
    path("viewdetails",views.viewdetails,name ="viewdetails"),
    path("adminlogin",views.adminlogin, name = "adminlogin"),


    path("sprink.html",views.sprink, name = "sprink"),
    path("sprinkler",views.sprinkler, name = "sprinkler"),
    path("sprinklerdisplay.html",views.sprinklerdisplay, name = "sprinklerdisplay"),


    path("street.html",views.street, name = "street"),
    path("lightings",views.lightings, name = "lightings"),
    path("streetlightsdisplay.html",views.streetlightsdisplay, name = "streetlightsdisplay"),




    path("humidityupdatepage.html",views.humidityupdatepage, name = "humidityupdatepage"),
    path("water",views.water, name = "water"),
    path("humiditydisplay.html",views.humiditydisplay, name = "humiditydisplay"),

    path("alarmupdatepage.html",views.alarmupdatepage, name = "alarmupdatepage"),
    path("garbage",views.garbage, name = "garbage"),
    path("alarmdisplay.html",views.alarmdisplay, name = "alarmdisplay"),



    path("tempadmindisplay.html",views.tempadmindisplay, name = "tempadmindisplay"),
    path("humadmindisplay.html",views.humadmindisplay, name = "humadmindisplay"),
    path("feedadmindisplay.html",views.feedadmindisplay, name = "feedadmindisplay"),
    path("alarmadmindisplay.html",views.alarmadmindisplay, name = "alarmadmindisplay"),
    path("streetadmindisplay.html",views.streetadmindisplay, name = "streetadmindisplay"),



]