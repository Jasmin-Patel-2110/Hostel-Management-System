from django.db import models

class Student(models.Model):
    enrollment_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    branch = models.CharField(max_length=50,choices=[('COMPUTER', 'Computer Engg.'), ('CIVIL', 'Civil Engg.'), ('CHEMICAL', 'Chemical Engg.'), ('ELECTRICAL', 'Electrical Engg.'), ('EC', 'Electronics and Communication Engg.'), ('MECHANICAL', 'Mechanical Engg.')])
    semester = models.IntegerField(choices=[(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"),(6,"6"),(7,"7"),(8,"8")])
    contact_number = models.CharField(max_length=15)
    parent_contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=10, choices=[('OLD', 'Old'), ('NEW', 'New')])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"
