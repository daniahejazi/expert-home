from django.db import models


def handle_upload_files(instance, filename):
    return f'{instance.expert.name}/{filename}'


class Expert(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    specialization = models.CharField(max_length=255)
    yearsExperiance = models.SmallIntegerField(default=0)
    specialization_info = models.TextField()
    displayName = models.BooleanField(default=True)
    services = models.TextField()
    workExperienseComapnies = models.TextField()
    qualifications = models.TextField()
    extraInfo = models.TextField(null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Cerificate(models.Model):
    expert = models.ForeignKey(Expert, related_name="certificates", on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=handle_upload_files)
    
    
class Vocation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.name
    
    