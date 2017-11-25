from django.db import models

class Quote(models.Model):
    author=models.CharField(max_length=50)
    content=models.CharField(max_length=400)
    
