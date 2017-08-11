from django.db import models
from django.utils import timezone

# Create your models here.
class ServicesList(models.Model):
    service = models.CharField(max_length=200)

    def __str__(self):
        return self.service

class Services(models.Model):
    service_type = models.ForeignKey(ServicesList, on_delete=models.CASCADE)
    service_title = models.CharField(max_length=200)
    service_content = models.TextField()
    created_date = models.DateTimeField()
    created_by = models.ForeignKey('auth.User', related_name='created_by_user')
    modified_date = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey('auth.User', related_name='modified_by_user')

    def __str__(self):
        return self.service_title
