from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    projects = Project.objects.all().order_by('-priority')
    skills = Skill.objects.all().order_by("-amount")
    works = Work.objects.all().order_by("-start_date")
    achievements = Achievement.objects.all().order_by("-time")
    resume = Resume.objects.all()[0]

    print(projects)
    context = {
        'projects':projects,
        'skills':skills,
        'works':works,
        'achievements':achievements,
        'resume':resume
    }

    return render(request, "index.html", context)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact_obj = Contact(name = name, email=email, message=message)
        contact_obj.save()

        email_context = {
            "name":name,
            
            "message":message,
            "email":email
        }
        template_email = render_to_string('email_template.html', email_context)

        email_obj = EmailMessage(

            name + " has sent an email",
            template_email,
            settings.EMAIL_HOST_USER,
            ['debroyshayan@gmail.com']
            
        )
        email_obj.fail_silently = False
        email_obj.send()
        print(email_obj)


        messages.success(request,"Message sent")
    return render(request, "contact.html")



