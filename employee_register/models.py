from django.db import models


class Position(models.Model):
    tittle = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tittle



class Employee(models.Model):
    full_name = models.CharField(max_length=200,null=True)
    emp_code = models.IntegerField(null=True)
    mobile = models.CharField(max_length=200, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,null=True)


# Create your models here.
