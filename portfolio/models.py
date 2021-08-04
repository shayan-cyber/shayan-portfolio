from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import URLField

# Create your models here.
class Techstack(models.Model):
    name = models.CharField(max_length=20)
    icon = models.ImageField(upload_to = 'icons')
    documentation = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(blank = True, null = True)
    priority = models.IntegerField(default=0)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    tech_stack = models.ManyToManyField(Techstack, related_name="tech_stack")
    time = models.DateTimeField()
    type_of = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.name
class Achievement(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    time = models.DateField()

    def __str__(self):
        return self.name

class Work(models.Model):
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.position +' of ' + self.company_name
CHOICES_OF =[
    ('BG', 'Beginner'),
    ('IN', 'Intermediate'),
    ('PR', 'Pro'),
    ('EX', 'Expert'),

]
class Skill(models.Model):
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    type_of = models.CharField(max_length=2, choices=CHOICES_OF)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name  

class Contact(models.Model):
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " email: " + self.email

class Resume(models.Model):
    resume_pdf = models.FileField(upload_to="resume")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.time)
    
