from rest_framework import routers
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# #set namespace
app_name = 'boards'


router = routers.DefaultRouter()
# mension path in space given between''
router.register('listboards', views.listboards)
# mension path in space given between''
router.register('city', views.listCities)
router.register('contact', views.listconatct)
# router.register('filterboards', views.filterboard)


urlpatterns = [
    path('', include(router.urls)),

    path('contact', views.listconatct),
    path('filterboard', views.filterboard.as_view(), name='filterboard'),


]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
