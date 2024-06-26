from django.urls import path

from .views import (
    home_view,
    about_view,
    experience_view,
    licenses_view,
    services_view,
    action_aechanism_view,
    join_as_expert_view,
    vocation_request_view,
    vocation_request_form_view,
    join_as_expert_form_view,
    vocation_request_form_from_home_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path("home-consultation-form", vocation_request_form_from_home_view, name="home_consultation_form"),
    path("about/", about_view, name="about"),
    path("experience/", experience_view, name="experience"),
    path("licenses/", licenses_view, name="licenses"),
    path("services/", services_view, name="services"),
    path("action-aechanism/", action_aechanism_view, name="action_aechanism"),
    
    path("join/", join_as_expert_view, name="join_as_officer"),
    path("join-form/", join_as_expert_form_view, name="join_as_expert_form"),
    
    path("consultation-request/", vocation_request_view, name="consultation_request"),
    path("consultation-form/", vocation_request_form_view, name="consultation_form"),
]
