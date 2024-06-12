from django import forms

from .models import Expert, Vocation, Cerificate


# class CerificateForm(forms.ModelForm):
#     class Meta:
#         model = Cerificate
#         fields = ("expert", "attachment")

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = (
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
            "extraInfo"
        )
        



class VocationForm(forms.ModelForm):
    class Meta:
        model = Vocation
        fields = ("first_name", "last_name", "email", "phone", "message")
