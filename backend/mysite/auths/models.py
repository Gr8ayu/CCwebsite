from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# Extending AbstractUser with custom fields
# class User (AbstractUser):
#     email = models.EmailField( unique=True,verbose_name='email', max_length=255)
    
#     REQUIRED_FIELDS = ['username']

#     USERNAME_FIELD = 'email'

#     def get_username(self):
#         return self.email

#     def __str__(self):
#         return self.username


# Adding signals to automatically create userProfile when user is created 
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    
    if created :
        UserProfile.objects.create(user=instance)

        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    
    instance.userprofile.save()

        
class Skill(models.Model):
    title = models.CharField(max_length=50)
    # type = Technical, creative, etc etc...
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50,null=True, blank=True) 
    lastname = models.CharField(max_length=50,null=True, blank=True)

    bio = models.TextField(max_length=500,null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    company = models.CharField(max_length=30,null=True, blank=True)
    interest = models.CharField(max_length=100,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', default = 'profile_pictures/default.png')
    resume = models.FileField(upload_to = 'resume/', null=True, blank=True)
    
    
    branch = models.CharField(max_length=50,null=True, blank=True)
    USN = models.CharField(max_length=100,null=True, blank=True)
    sem = models.CharField(max_length=100,null=True, blank=True)

    website = models.URLField(default='', blank=True)
    linkedIn_ID = models.URLField(default='', blank=True)
    github_ID = models.URLField(default='', blank=True)
    
    codechef_id = models.CharField(max_length=30,null=True, blank=True)
    codeforces_id = models.CharField(max_length=30,null=True, blank=True)
    hackerrank_id = models.CharField(max_length=30,null=True, blank=True)
    
    sem = models.CharField(max_length=100,null=True, blank=True)




    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username 
    

class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    institute_name= models.CharField(max_length=200)
    course = models.CharField(max_length=10,null=True, blank=True)
    duration_from = models.DateField("Date From", default=datetime.date.today)
    duration_to = models.DateField("Date To",null=True, blank = True)
    score = models.CharField(max_length=10,null=True, blank=True)
    descriptions = models.TextField(max_length=500,null=True, blank=True)

    def __str__(self):
        return self.institute_name 

class Experience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # position = models.CharField(max_length=50)
    # company = models.CharField(max_length=50)
    description = models.TextField(max_length=500,null=True, blank=True)    
    domains = models.CharField(max_length=100,null=True, blank=True)
    duration_from = models.DateField("Date From", default=datetime.date.today)
    duration_to = models.DateField("Date To",null=True, blank = True)
    
















# class UserResume(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Education
    # Experience
    # skills
    # Award and Achivements TODO



# class SkillSet(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     skill = models.ManyToManyField(Skill)



# TODO : Modify it to store user's skill along with degree of expertise eg HTML[9/10], CSS[7/10] .... 