from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TeacherViewSet


router = SimpleRouter()
router.register(r'teachers', TeacherViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
