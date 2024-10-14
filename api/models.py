from django.db import models

class Company(models.Model):
    TYPE_CHOICES = (
        ('IT', 'IT'),
        ('Non-IT', 'Non-IT'),
    )
    
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=13, choices=TYPE_CHOICES)  # Updated max_length to 13
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    POSITION_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('manager', 'Manager'),
        ('analyst', 'Analyst'),
        # Add more positions as needed
    ]

    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)  # ForeignKey to Company
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    about = models.TextField(blank=True, null=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    def __str__(self):
        return self.name
