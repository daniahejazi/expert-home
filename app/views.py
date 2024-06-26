from django.shortcuts import redirect, render
from django.contrib import messages


from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail

from django.conf import settings
from django.urls import reverse

from .models import Cerificate, Expert

# Create your views here.

from .forms import VocationForm, ExpertForm


def home_view(request):
    return render(request, "app/home.html")


def about_view(request):
    return render(request, "app/about.html")


def experience_view(request):
    return render(request, "app/experience.html")


def licenses_view(request):
    return render(request, "app/licenses.html")


def services_view(request):
    return render(request, "app/services.html")


def action_aechanism_view(request):
    return render(request, "app/AechanismofAction.html")


def join_as_expert_view(request):
    return render(request, "app/JoinAsAnOfficer.html")


def join_as_expert_form_view(request):
    if request.method == "POST":
        new_form = ExpertForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            # get the expert object from new form
            new_expert = new_form.instance

            if request.FILES:
                for file in request.FILES.getlist("attachments"):
                    new_cerificate = Cerificate(expert=new_expert, attachment=file)
                    new_cerificate.save()

            name = new_form.cleaned_data["name"]
            to_email = new_form.cleaned_data["email"]
            phone = new_form.cleaned_data["phone"]
            general_specialization = new_form.cleaned_data["general_specialization"]
            sum_experience_years = new_form.cleaned_data["sum_experience_years"]

            admin_url = reverse("admin:index")
            admin_page_url = request.build_absolute_uri(admin_url)

            context = {
                "name": name,
                "email": to_email,
                "phone": phone,
                "general_specialization": general_specialization,
                "sum_experience_years": sum_experience_years,
                "admin_page_url": admin_page_url,
            }
            email_body = render_to_string("component/join_email.html", context)

            subject = f"طلب انضمام كخبير من السيد : {name}"
            from_email = settings.NOTIFI_EMAIL
            ask_email = settings.ASK_EMAIL

            email = EmailMessage(subject, email_body, from_email, [ask_email])
            email.content_subtype = "html"
            email.send()

            subject = f"تم استلام طلبك بنجاح"
            context = {}
            email_body = render_to_string("component/join_email_for_user.html", context)
            email = EmailMessage(subject, email_body, from_email, [to_email])
            email.content_subtype = "html"
            email.send()

            messages.success(request, "تم حفظ بياناتك بنجاح")
            return redirect("join_as_officer")

    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect("join_as_officer")


def vocation_request_view(request):
    return render(request, "app/consultation_request.html")


def vocation_request_form_view(request):
    if request.method == "POST":

        form = VocationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            to_email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            admin_url = reverse("admin:index")
            admin_page_url = request.build_absolute_uri(admin_url)

            context = {
                "first_name": first_name,
                "last_name": last_name,
                "email": to_email,
                "phone": phone,
                "message": message,
                "admin_page_url": admin_page_url,
            }
            email_body = render_to_string("component/vocation_email.html", context)

            subject = f"طلب استشارة من السيد :{first_name} {last_name}"
            from_email = settings.NOTIFI_EMAIL
            info_email = settings.INFO_EMAIL
            email = EmailMessage(subject, email_body, from_email, [info_email], context)
            email.content_subtype = "html"
            email.send()

            subject = f"تم استلام طلبك بنجاح"
            context = {}
            email_body = render_to_string("component/vocation_email_for_user.html", context)
            email = EmailMessage(subject, email_body, from_email, [to_email])
            email.content_subtype = "html"
            email.send()

            messages.success(request, "تم ارسال طلبك بنجاح")
            return redirect("consultation_request")

    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect("consultation_request")


def vocation_request_form_from_home_view(request):
    if request.method == "POST":

        form = VocationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            to_email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            admin_url = reverse("admin:index")
            # Build the absolute URL
            admin_page_url = request.build_absolute_uri(admin_url)
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "email": to_email,
                "phone": phone,
                "message": message,
                "admin_page_url": admin_page_url,
            }
            email_body = render_to_string("component/vocation_email.html", context)

            subject = f"طلب استشارة من السيد :{first_name} {last_name}"
            from_email = settings.NOTIFI_EMAIL
            info_email = settings.INFO_EMAIL

            email = EmailMessage(subject, email_body, from_email, [info_email])
            email.content_subtype = "html"
            email.send()

            subject = f"تم استلام طلبك بنجاح"
            context = {}
            email_body = render_to_string("component/vocation_email_for_user.html", context)
            email = EmailMessage(subject, email_body, from_email, [to_email])
            email.content_subtype = "html"
            email.send()

            messages.success(request, "تم ارسال طلبك بنجاح")
            return redirect("home")

    messages.error(request, "يوجد خطآ برجاء اعادة المحاولة")
    return redirect("home")
