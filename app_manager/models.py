from django.db import models

# Create your models here.


class App_info(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.TextField()
    is_free = models.BooleanField(default='FALSE')
    logo_url = models.ImageField()

    def __str__(self):
        return self.name