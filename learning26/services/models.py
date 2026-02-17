from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
