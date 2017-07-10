from django.conf.urls import url
from django.contrib import admin

from accounts import views

urlpatterns = [
    url(r'^$', views.Login.as_view(), name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', views.Logout.as_view(), name="logout"),
    url(r'^welcome/$', views.Welcome.as_view(), name="welcome")
]
