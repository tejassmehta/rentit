from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ListingsPKAPIView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', ListingsRudView.as_view(), name='post-rud'),
]