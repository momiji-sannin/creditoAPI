from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('applications', views.ApplicationViewSet, basename='applications')

urlpatterns = [
    path(r'', include(router.urls)),
]
