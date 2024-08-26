from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import GroupViewSet

router = SimpleRouter()
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = router.urls
