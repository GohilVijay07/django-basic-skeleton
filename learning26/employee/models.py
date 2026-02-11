from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
        
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table = "course"
        
    def __str__(self):
        return self.name
    
class department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        db_table = "department"
        
    def __str__(self):
        return self.name
    
class ResidentPost(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.ManyToManyField(Employee, related_name="liked_posts")

    class Meta:
        db_table = "residentpost"
        
    def __str__(self):
        return self.name