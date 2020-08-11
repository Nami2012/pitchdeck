# Create your models here.
import datetime
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="/profile_pics/main.jpg",upload_to='profile_pics')

    def __str__(self):
        return f'(self.user.username) Profile'

    def save(self, *args,**kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class pitchDeck(models.Model):
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    pitchDeckId = models.AutoField(primary_key=True)
    startupName = models.CharField(max_length=64, blank=False)


    def __str__(self):
        return f'(self.user.username) pitchDeck'


class titleSlide(models.Model):
    name = models.TextField(blank=False, null=True)
    titleline = models.TextField(blank=False, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)
    def __str__(self):
        return f'(self.name) titleSlide'

class problemTryingToSolve(models.Model):
    bullet1 = models.TextField(blank= False, null=True)
    bullet2 = models.TextField(blank= True, null=True)
    bullet3 = models.TextField(blank= True, null=True)
    bullet4 = models.TextField(blank= True, null=True)
    bullet5 = models.TextField(blank= True, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)



class vision(models.Model):
    bullet1 = models.TextField(blank= False, null=True)
    bullet2 = models.TextField(blank= True, null=True)
    bullet3 = models.TextField(blank= True, null=True)
    bullet4 = models.TextField(blank= True, null=True)
    bullet5 = models.TextField(blank= True, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)

class uniqueValueProposition(models.Model):
    usp = models.CharField(max_length=64, blank=False)
    bullet1 = models.TextField(blank= False, null=True)
    bullet2 = models.TextField(blank= True, null=True)
    bullet3 = models.TextField(blank= True, null=True)
    bullet4 = models.TextField(blank= True, null=True)
    bullet5 = models.TextField(blank= True, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)

class underlyingMagic(models.Model):
    bullet1 = models.TextField(blank= False, null=True)
    bullet2 = models.TextField(blank= True, null=True)
    bullet3 = models.TextField(blank= True, null=True)
    bullet4 = models.TextField(blank= True, null=True)
    bullet5 = models.TextField(blank= True, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)


class milestones(models.Model):
    impact1 = models.IntegerField(blank = True)
    bullet1 = models.TextField(blank= False, null=True)
    
    impact2 = models.IntegerField(blank = True)
    bullet2 = models.TextField(blank= True, null=True)
    
    bullet3 = models.TextField(blank= True, null=True)
    bullet4 = models.TextField(blank= True, null=True)
    bullet5 = models.TextField(blank= True, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)

class totalAddressableMarket(models.Model):
    totalAvailableMarket = models.IntegerField(blank = False)
    servedAvailableMarket = models.IntegerField(blank = False)
    targetMarket = models.IntegerField(blank = False)
    
    TAMSection = models.CharField(max_length=64, blank=False)
    SAMSection = models.CharField(max_length=64, blank=False)
    TMSection = models.CharField(max_length=64, blank=False)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)


class businessModal(models.Model):
    customerAcquisitionStrategy = models.TextField(blank= False, null=True)
    serviceProvision = models.TextField(blank= False, null=True)
    modelType = models.TextField(blank= False, null=True)
    monetizationStrategy = models.TextField(blank= False, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)

class Competition(models.Model):
    startupsFree = models.CharField(max_length=64, blank=False)
    startupsPaid = models.CharField(max_length=64, blank=False)
    incumbentsFree = models.CharField(max_length=64, blank=False)
    incumbentsPaid = models.CharField(max_length=64, blank=False)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)

class competitiveAdvantage(models.Model):
    impact1 = models.IntegerField(blank = True)
    bullet1 = models.TextField(blank= False, null=True)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)
    

class member(models.Model):
    name =   models.CharField(max_length=64, blank=False)
    image = models.ImageField(default="/profile_pics/main.jpg",upload_to='profile_pics')
    credential1 = models.TextField(blank= False, null=True)

    def save(self, *args,**kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Team(models.Model):
    member1 = models.ForeignKey(to=member, on_delete=models.CASCADE)
    member2 = models.ForeignKey(to=member, on_delete=models.CASCADE)
    member2 = models.ForeignKey(to=member, on_delete=models.CASCADE)
    pitchDeckId =  models.ForeignKey(to=pitchDeck, on_delete=models.CASCADE)
   







    








