"""simplemfl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from facilities.views import OrgUnitViewSet, FacilityViewSet, AdminUnitViewSet, HospitalViewSet
import facilities.urls

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'facilities', FacilityViewSet, base_name='facilities')
router.register(r'adminunits', AdminUnitViewSet, base_name='adminunits')
router.register(r'orgunits', OrgUnitViewSet)
router.register(r'hospitals', HospitalViewSet, base_name='hospitals')
# router.register(r'geojson', GeoJSONOrgUnitViewSet, base_name='geojson')

urlpatterns = [
    url(r'^$', facilities.views.index),
    url(r'', include(facilities.urls)),

    # Django Admin
    url(r'^admin/', admin.site.urls),
    # Django Rest Framework
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]

# Django debug toolbar support
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns