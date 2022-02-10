from django.db import models

#Create your models here.

class Register(models.Model):
    Firstname =models.CharField(max_length=100)
    phonenumber =models.IntegerField()
    EmailId = models.CharField(max_length=100)
    Complaints =models.CharField(max_length=100000)
	
	
class Sensorstatesupdate(models.Model):
    
    Updated = models.DateTimeField(auto_now=True)
    Temp_status = models.IntegerField()
    
    Tempsensorstate = models.BooleanField(default=False)
    
    Parklocation = models.CharField(max_length=100)
    Review = models.TextField()


class Humidityupdate(models.Model):
    
    Updated = models.DateTimeField(auto_now=True)
    Humidity_status = models.IntegerField()
    
    Humiditysensorstate = models.BooleanField(default=False)
    
    Parklocation = models.CharField(max_length=100)
    Review = models.TextField()


class Streetlightings(models.Model):
    
    sensor_update = models.CharField(max_length=100)
    updatetime = models.DateTimeField(auto_now=True)
    description = models.TextField()


class FeedbackForm(models.Model):
    u_name = models.CharField(max_length=100)
    u_email = models.CharField(max_length=100)
    u_phone = models.IntegerField()
    u_date = models.DateTimeField(auto_now=True)
    u_rate = models.IntegerField()
    u_suggestion = models.TextField()
    u_review = models.TextField()


   
class AdminUpdates(models.Model):
    previous_temparature_value = models.IntegerField()
    present_temparature_value = models.IntegerField() 
    sprinkler_state = models.CharField(max_length=100)
    previous_humidity_value = models.IntegerField()
    present_humidity_value = models.IntegerField()
    water_pump_state = models.CharField(max_length=100)
    street_light_state = models.CharField(max_length=100)
    alarm_state = models.CharField(max_length=100)
#    next_update_time = models.IntegerField()
    description = models.TextField()

class sprinklerstatus(models.Model):
    previous_temparature_value = models.IntegerField()
    present_temparature_value = models.IntegerField() 
    sprinkler_state = models.CharField(max_length=100)
    #next_update_time = models.IntegerField() 
    description = models.TextField()

class Humidityupdation(models.Model):
    previous_humidity_value = models.IntegerField()
    present_humidity_value = models.IntegerField()
    water_state = models.CharField(max_length=100)
    updatetime = models.DateTimeField(auto_now=True)
    description = models.TextField() 

class alarmupdate(models.Model):
    garbage_update = models.CharField(max_length=100)
    updatetime = models.DateTimeField(auto_now=True)
    description = models.TextField() 


     






