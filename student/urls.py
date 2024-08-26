from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import StudentViewSet

router = SimpleRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls
