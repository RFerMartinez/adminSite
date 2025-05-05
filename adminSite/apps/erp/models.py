# Django imports
from django.db import models

# Project imports

# Python imports
from datetime import datetime

class TypeEmp(models.Model):
    names = models.CharField(max_length=150, verbose_name='Tipo')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'tipo'
        ordering = ['id']

class Category(models.Model):
    names = models.CharField(max_length=150, verbose_name='Categoria')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']

class Employee(models.Model):

    category = models.ManyToManyField(Category)

    type_emp = models.ForeignKey(TypeEmp, on_delete=models.CASCADE)

    names = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=8, unique=True, verbose_name='D.N.I.') #fecha
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro') #hora y fecha
    date_creation = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(default=0)
    age1 = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
        # decimal_places -> números de digitos luego del punto decimal
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['-id'] # de manera descendente y por 'id'