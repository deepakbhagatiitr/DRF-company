# companyapi/views.py
from rest_framework import viewsets
from .models import Company, Employee
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CompanySerializer, EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'], url_path='employees')
    def get_employees(self, request, pk=None):
        """
        Retrieve all employees for a specific company.
        """
        company = self.get_object()  # Get the company instance using the primary key (pk)
        employees = company.employees.all()  # Get all employees related to the company
        serializer = EmployeeSerializer(employees, many=True)  # Serialize the employees
        return Response(serializer.data)  # Return the serialized data

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer