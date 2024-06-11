from django.shortcuts import render

# Create your views here.


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

def join_view(request):
    # TODO: form here
    return render(request, 'app/JoinAsAnOfficer.html')

def consultation_request_view(request):
    # TODO: form here
    return render(request, 'app/consultation_request.html')