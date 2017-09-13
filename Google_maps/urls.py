from django.conf.urls import url, include
from django.contrib import admin
from allauth.account.views import LoginView

from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name="z"),

    url(r'^logout/$', views.Logout.as_view(), name="logout"),
    url(r'^register/$', views.Register.as_view(), name="register"),
    url(r'^welcome/$', views.Welcome.as_view(), name="welcome"),
    url(r'^accounts/', include('allauth.urls')),
]
