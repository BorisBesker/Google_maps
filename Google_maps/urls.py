from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),  # Urls from "allauth" application
    url(r'^google/', include('google_embedded_maps.urls'))  # Urls from google_embedded_maps application
]
