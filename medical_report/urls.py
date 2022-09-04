from django.urls import path
from .views import developer,analysis,addImage


urlpatterns = [
    path('developer/',developer,name='developer'),
    path('analysis/',analysis,name='analysis'),
    path('addImage/',addImage,name='addImage'),

]