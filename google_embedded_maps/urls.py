from django.conf.urls import url

from .views import Welcome

urlpatterns = [
    url(r'^welcome/', Welcome.as_view()),
]
