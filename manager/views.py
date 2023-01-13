from django.shortcuts import render, redirect
from .models import*
from .forms import ContactForm


def home(request):
    template_name = "manager/home.html"
    skill_list = skills.objects.all()
    language_list = Planguage.objects.all()
    framework_list = Framework.objects.all()
    database_list = DataBase.objects.all()
    tool_list = Dtool.objects.all()
    project_list = Project.objects.all()
    context = {'skill_list':skill_list, 'language_list':language_list, 'framework_list':framework_list, 'database_list':database_list, 'tool_list':tool_list, 'project_list':project_list}
    return render(request, template_name, context)

def contact_view(request):
    template_name = 'manager/contact.html'
    form = ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, template_name, context)
