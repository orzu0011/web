from rest_framework import viewsets
from .models import Groups
from .serializers import GroupsSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
