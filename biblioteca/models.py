from django.db import models

class autor(models.Model):
    nombre = models.CharField(max_length=200)
    lugar_nacimiento = models.CharField(max_length=200)
    fecha_nacimiento =models.DateTimeField()

    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor_id = models.ForeignKey(autor,primary_key=id,on_delete=models.CASCADE)
    
        
    def __str__(self):
        return self.titulo
    

    

    
