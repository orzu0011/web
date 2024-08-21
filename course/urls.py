from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CourseViewSet


router = SimpleRouter()
router.register(r'courses', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
