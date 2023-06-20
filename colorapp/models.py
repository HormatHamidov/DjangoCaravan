from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7) 
    
    def __str__(self):
        return self.name


class Meyve(models.Model):
    name = models.CharField(max_length=50)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
