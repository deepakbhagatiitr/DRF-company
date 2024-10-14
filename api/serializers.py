# companyapi/serializers.py
from rest_framework import serializers
from .models import Company,Employee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  # Include all fields from the Company model

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # Include all fields from the Company model
