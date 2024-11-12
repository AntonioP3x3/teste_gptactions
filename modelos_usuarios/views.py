from rest_framework.views import APIView
from rest_framework.response import Response
from modelos_usuarios.models import ModeloUsuarioModel
from modelos_usuarios.serializer import ModeloUsuarioSerializer

class ListCreateModeloUsuarioView(APIView):
  def get(self, request):
    all = ModeloUsuarioModel.objects.all()
    print("\n\n\n")
    print(all)
    return Response(ModeloUsuarioSerializer(all, many=True).data)

  def post(self, request):
    serializer = ModeloUsuarioSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      registro = ModeloUsuarioModel.objects.create(**serializer.validated_data)
      return Response(ModeloUsuarioSerializer(registro).data)

class CreateUpdateDeleteModeloUsuarioView(APIView):
  def get_registro(self, pk):
    try:
      registro = ModeloUsuarioModel.objects.get(pk=pk)
      return registro
    except:
      return Response({"error": f"O item buscado de id {pk} não foi encontrando no banco de dados."}, 404)
  
  def get(self, request, pk):
    registro = self.get_registro(pk)
    try:
      serializer = ModeloUsuarioSerializer(registro)
      return Response(serializer.data)
    except:
      return Response({"error": f"Não foi possível retornar o valor do item de id {pk}. Tente novamente ou entre em contato com a equipe de desenvolvimento para solução do erro"}, status=400)

  def put(self, request, pk):
    registro = self.get_registro(pk)
    try:
      serializer = ModeloUsuarioSerializer(registro, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    except:
      return Response({"error": f"Não foi possível atualizar o item de id {pk}. Tente novamente ou entre em contato com a equipe de desenvolvimento para solução do erro"}, status=500)

  def delete(self, request, pk):
    registro = self.get_registro(pk)
    try:
      registro.delete()
      return Response({"msg": f"Item de id {pk} foi deletado com sucesso"})
    except:
      return Response({"error": f"Não foi possível deletar o item de id {pk}. Tente novamente ou entre em contato com a equipe de desenvolvimento para solução do erro"}, status=500)

class ListModelosPorUsuarioView(APIView):
  def get(self, request, user_id):
    try:
      registro = ModeloUsuarioModel.objects.filter(user_id=user_id)
      if(len(registro) == 0):
        return Response({"error": f"O usuário de id {user_id} não existe ou não possui modelos salvos no banco de dados"}, 204)
      serializer = ModeloUsuarioSerializer(registro, many=True)
      return Response(serializer.data)
    except:
      return Response({"error": "Não fo possível obter os modelos do usuário por algum motivo. Tente novamente ou entre em contato com a equipe de desenvolvimento para solução do erro"})