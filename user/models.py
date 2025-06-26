from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.IntegerField()
    departmet = models.CharField(max_length=50,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
