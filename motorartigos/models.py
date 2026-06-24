from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length = 100)
    biografia = models.TextField()
    email = models.EmailField()    

    def __str__(self) -> str:
        return self.nome 
    
    class Meta:
        db_table = 'Autor'
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
    

class EixoTecnologia(models.Model):
    nome = models.CharField(max_length = 100)
    Autor = models.CharField(max_length = 100)


    def __str__(self) -> str:
        return self.nome 
    

    class Meta:
        db_table = 'EixoTecnologia'
        verbose_name = "Eixo Tecnologia"
