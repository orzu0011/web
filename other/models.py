from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = ('Xona')
        verbose_name_plural = ('Xonalar')