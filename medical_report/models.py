from django.db import models

# Create your models here.
from users.models import Profile
import uuid


class Blood_report(models.Model):
    blood_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    hemoglobin = models.FloatField(null=True, blank=True)
    rbc = models.FloatField(null=True, blank=True)
    wbc = models.FloatField(null=True, blank=True)
    platelets = models.FloatField(null=True, blank=True)
    esr = models.FloatField(null=True, blank=True)
    neutrophil = models.FloatField(null=True, blank=True)
    lymphocyte = models.FloatField(null=True, blank=True)
    mcv = models.FloatField(null=True, blank=True)
    mch = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return f'{str(self.blood_owner)} Blood report'

    
    