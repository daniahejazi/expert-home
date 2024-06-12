from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .models import Cerificate, Expert, Vocation

# Create your views here.

from .forms import VocationForm, ExpertForm

def home_view(request):
    return render(request, 'app/home.html')

def about_view(request):
    return render(request, 'app/about.html')

def experience_view(request):
    return render(request, 'app/experience.html')

def licenses_view(request):
    return render(request, 'app/licenses.html')

def services_view(request):
    return render(request, 'app/services.html')

def action_aechanism_view(request):
    return render(request, 'app/AechanismofAction.html')

def join_as_expert_view(request):
    return render(request, 'app/JoinAsAnOfficer.html')


def join_as_expert_form_view(request):
    if request.method == 'POST':
        new_form = ExpertForm(request.POST)
        if new_form.is_valid():
            new_form.save()
        
            new_expert = Expert.objects.last()
            
            if request.FILES:
                for file in request.FILES.getlist("attachments"):
                    new_cerificate = Cerificate(expert=new_expert, attachment=file)
                    new_cerificate.save()
                    messages.success(request, "تم حفظ بياناتك بنجاح")
                    return redirect('join_as_officer')
        

            # messages.success(request, "تم ارسال طلبك بنجاح")
            # return redirect('join_as_officer')
        
    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect('join_as_officer')






def vocation_request_view(request):
    return render(request, 'app/consultation_request.html')

def vocation_request_form_view(request):
    if request.method == 'POST':

        form = VocationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, "تم ارسال طلبك بنجاح")
            return redirect('consultation_request')
        
    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect('consultation_request')


def vocation_request_form_from_home_view(request):
    if request.method == 'POST':

        form = VocationForm(request.POST)
        print(form.data)
        if form.is_valid():
            print("-------- OK -------")
            form.save()
            messages.success(request, "تم ارسال طلبك بنجاح")
            return redirect('home')
        
    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect('home')
