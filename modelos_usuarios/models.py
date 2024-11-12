from django.db import models

class ModeloUsuarioModel(models.Model):
  user_id = models.IntegerField()
  modelo = models.TextField()
  tipo_prompt = models.CharField()