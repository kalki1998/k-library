from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    email = models.EmailField()
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)  

    def __str__(self):
        return self.name  


    
