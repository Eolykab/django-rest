from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'create/installation', views.InstallationViewSet, basename='installation')
router.register(r'status', views.StatusViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]