from django.db import models

# organization -> factory -> production line -> machine -> sensor

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Factory(models.Model):
    #want to avoid deleting an organization if it has factories
    organization = models.ForeignKey(Organization, on_delete = models.PROTECT, related_name= 'factories')
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('organization', 'name')

class ProductionLine(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='production_lines')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('factory','name')

#all these times stamps are merely writen for time tracking

class Machine(models.Model):
    #this production_line is not the same as the one in ProductionLine model
    #its written below to follow the pythonic way
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE, related_name='machines')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('production_line', 'name')

class Sensor(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='sensors')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('machine', 'name')


