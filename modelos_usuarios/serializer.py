from rest_framework import serializers
from modelos_usuarios.models import ModeloUsuarioModel

class ModeloUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloUsuarioModel
        fields = "__all__"