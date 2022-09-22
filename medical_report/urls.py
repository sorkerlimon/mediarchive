from django.urls import path
from .views import developer,analysis,addImage,bloodAnalysis,urinAnalysis,bloodImage,urinImage,allimage


urlpatterns = [
    path('developer/',developer,name='developer'),
    path('analysis/',analysis,name='analysis'),
    path('addImage/',addImage,name='addImage'),
    path('bloodAnalysis/',bloodAnalysis,name='bloodAnalysis'),
    path('urinAnalysis/',urinAnalysis,name='urinAnalysis'),
    path('bloodImage/',bloodImage,name='bloodImage'),
    path('urinImage/',urinImage,name='urinImage'),
    path('allimage/',allimage,name='gallery'),

]