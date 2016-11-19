from django.conf.urls import url
from .views import IndexView, LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^home/?$', IndexView.as_view(), name='index'),
]
