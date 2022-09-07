from django.db import models

# Create your models here.
from users.models import Profile
import uuid


class Blood_report(models.Model):
    blood_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    Hemoglobin = models.FloatField(null=True, blank=True)
    RBC = models.FloatField(null=True, blank=True)
    WBC = models.FloatField(null=True, blank=True)
    Platelets = models.FloatField(null=True, blank=True)
    ESR = models.FloatField(null=True, blank=True)
    Neutrophil = models.FloatField(null=True, blank=True)
    Lymphocyte = models.FloatField(null=True, blank=True)
    MCV = models.FloatField(null=True, blank=True)
    MCH = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self):
        return f'{str(self.blood_owner)} Blood report'

    
    