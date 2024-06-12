from django.db import models


def handle_upload_files(instance, filename):
    return f'{instance.expert.name}/{filename}'


class Expert(models.Model):
    DISPLAY_NAME_CHOISES = (
        ("YES", "Yes"),
        ("NO", "No")
    )
    name = models.CharField(verbose_name="الاسم", max_length=255)
    # email = models.EmailField(verbose_name="البريد الالكتروني")
    # phone = models.CharField(verbose_name="رقم الهاتف",max_length=25)
    general_specialization = models.CharField(verbose_name="التخصص العام",max_length=255)
    sum_experience_years = models.SmallIntegerField(verbose_name="مجموع سنوات الخبرة العملية",default=0)
    details_specialization_info = models.TextField(verbose_name="تخصص دقيق")
    display_name_type = models.CharField(verbose_name="هل ترغب بعرض اسمك و صورتك",max_length=3, choices=DISPLAY_NAME_CHOISES, default="YES")
    services = models.TextField(verbose_name="الخدمات التي يمكن تقديمها و الاستشارات")
    work_experiense_comapnies = models.TextField(verbose_name="الجهات التي عملتم معها")
    study_qualifications = models.TextField(verbose_name="الجهات التي حصلتم منها على شهادة اكاديمية")
    heigh_special_companies = models.TextField(verbose_name="الجهات التي لديكم فيها عضوية مجلس ادارة او استشارة او تعاون")
    extraInfo = models.TextField(verbose_name="اقتراحات او تفاصيل او معلومات هامة",null=True, blank=True)
    
    created_at = models.DateTimeField(verbose_name="تاريخ الارسال", auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "طلبات الانضمام كخبير"
    
    
class Cerificate(models.Model):
    expert = models.ForeignKey(Expert, related_name="certificates", on_delete=models.CASCADE)
    attachment = models.FileField(verbose_name="الرخصة", upload_to=handle_upload_files)
    
    class Meta:
        verbose_name_plural = "الرخص المهنية"
    
class Vocation(models.Model):
    first_name = models.CharField(verbose_name="الاسم الاول",max_length=255)
    last_name = models.CharField(verbose_name="الاسم الاخير",max_length=255)
    email = models.EmailField(verbose_name="البريد الالكتروني")
    phone = models.CharField(verbose_name="رقم الهاتف", max_length=25)
    message = models.TextField(verbose_name="تفاصيل الاستشارة")
    created_at = models.DateTimeField(verbose_name="تاريخ الارسال", auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "طلبات الاستشارة"