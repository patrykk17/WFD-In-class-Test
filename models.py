from django.db import models

# Salesperson model
class Salesperson(models.Model):
    Salesperson_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)

# Customer model
class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State_Province = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    Postal_Code = models.CharField(max_length=20)

# Car model
class Car(models.Model):
    Car_ID = models.AutoField(primary_key=True)
    Serial_Number = models.CharField(max_length=100)
    Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Colour = models.CharField(max_length=30)
    Year = models.IntegerField()
    Car_for_Sale_YN = models.BooleanField()

# Sales Invoice model
class Sales_Invoice(models.Model):
    Invoice_ID = models.AutoField(primary_key=True)
    Invoice_Number = models.CharField(max_length=50)
    Date = models.DateField()
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Salesperson_ID = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

# Mechanic model
class Mechanic(models.Model):
    Mechanic_ID = models.AutoField(primary_key=True)
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)

# Service model
class Service(models.Model):
    Service_ID = models.AutoField(primary_key=True)
    Service_Name = models.CharField(max_length=100)
    Hourly_Rate = models.DecimalField(max_digits=6, decimal_places=2)

# Service Ticket model
class Service_Ticket(models.Model):
    Service_Ticket_ID = models.AutoField(primary_key=True)
    Service_Ticket_Number = models.CharField(max_length=50)
    Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date_Received = models.DateField()
    Comments = models.TextField()
    Date_Returned_to_Customer = models.DateField()

# Service mechanic model
class Service_Mechanic(models.Model):
    ServiceMechanic_ID = models.AutoField(primary_key=True)
    Mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    Service_Ticket_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE)
    Service_ID = models.ForeignKey(Service, on_delete=models.CASCADE)
    Hours = models.DecimalField(max_digits=5, decimal_places=2)
    Comment = models.TextField()
    Rate = models.DecimalField(max_digits=6, decimal_places=2)

# Parts model
class Parts(models.Model):
    Parts_ID = models.AutoField(primary_key=True)
    Part_Number = models.CharField(max_length=50)
    Description = models.TextField()
    Purchase_Price = models.DecimalField(max_digits=8, decimal_places=2)
    Retail_Price = models.DecimalField(max_digits=8, decimal_places=2)

# Parts used model
class Parts_Used(models.Model):
    Parts_Used_ID = models.AutoField(primary_key=True)
    Part_ID = models.ForeignKey(Parts, on_delete=models.CASCADE)
    Service_Ticket_ID = models.ForeignKey(Service_Ticket, on_delete=models.CASCADE)
    Number_Used = models.IntegerField()
    Price = models.DecimalField(max_digits=8, decimal_places=2)
