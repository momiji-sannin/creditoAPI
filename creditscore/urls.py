from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('applications', views.ApplicationViewSet, basename='applications')

application_router = routers.NestedDefaultRouter(router, 'applications', lookup='application')
application_router.register('documents', views.DocumentViewSet, basename='application-documents')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(application_router.urls)),
]
