from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [

    url(r'^$', views.login_view, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^welcome/$', views.welcome, name="welcome"),
    url(r'^logout/$', views.logout_view, name="logout")


]
