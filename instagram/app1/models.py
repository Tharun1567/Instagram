from django.db import models


# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rate=models.IntegerField()
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    genre=models.CharField(max_length=30)
    author=models.ForeignKey("Author",on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title+" "+self.author.name
        
    

     

    