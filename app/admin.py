from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Expert, Cerificate, Vocation


# admin.site.register(Expert)
# admin.site.register(Cerificate)

admin.site.site_title = "UHX Dashboard"
admin.site.site_header = "UHX Dashboard"
admin.site.index_title = "لوحة التحكم"


class CerificateInline(admin.TabularInline):
    model = Cerificate
    extra = 0
    fields = ("attachment",)
    readonly_fields = ["attachment"]
    can_delete = False


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "name",
        "general_specialization",
        "sum_experience_years",
    )
    search_fields = ("name", "general_specialization")
    list_filter = ("created_at",)
    list_per_page = 20
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    readonly_fields = (
        "name",
        # "email",
        # "phone",
        "general_specialization",
        "sum_experience_years",
        "details_specialization_info",
        "display_name_type",
        "services",
        "work_experiense_comapnies",
        "study_qualifications",
        "heigh_special_companies",
        "extraInfo",
        "created_at",
    )
    list_display_links = ("created_at", "name")

    inlines = [CerificateInline]


@admin.register(Vocation)
class VocationAdmin(admin.ModelAdmin):
    list_display = ("created_at", "first_name", "last_name", "email", "phone")
    readonly_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "message",
        "created_at",
    )
    search_fields = ("first_name", "last_name", "email", "phone", "message")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    list_display_links = ("created_at", "first_name", "last_name")
    list_per_page = 20


admin.site.unregister(User)
admin.site.unregister(Group)
