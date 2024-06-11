from django.urls import path

from .views import (
    home_view,
    about_view,
    experience_view,
    licenses_view,
    services_view,
    action_aechanism_view,
    join_view,
    consultation_request_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("experience/", experience_view, name="experience"),
    path("licenses/", licenses_view, name="licenses"),
    path("services/", services_view, name="services"),
    path("action-aechanism/", action_aechanism_view, name="action_aechanism"),
    path("join/", join_view, name="join_as_officer"),
    path("consultation-request/", consultation_request_view, name="consultation_request"),
]
