from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'', include('reco.urls')),
]
