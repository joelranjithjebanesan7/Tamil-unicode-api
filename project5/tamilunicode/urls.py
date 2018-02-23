from django.conf.urls import url
from tamilunicode import views
from django.conf.urls import include
 


urlpatterns = [
    
    url(r'^tamilunicode/$',views.unicodes, name = 'tamilunicodes'),
    
    ]