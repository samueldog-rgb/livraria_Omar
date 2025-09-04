from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor, Editora, Livros
from .serializers import AutorSerializer, EditoraSerializer, LivrosSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Filter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



@api_view(['GET' , 'POST'])
@permission_classes([IsAuthenticated])
def listar_autores(request):
    if request.method== 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer =AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


############################Autores###################### GET E POST
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id'] #permite o filtro exato
    search_filter = ['autor'] #Habilita a busca total de strings
    

class AutoresDetailView(RetrieveUpdateDestroyAPIView): # UPDATE E DELITE
    queryset = Autor.objects.all()  
    serializer_class = AutorSerializer

##################################################### 

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
class EditorasView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [IsAuthenticated]

class EditorasDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class LivrosView(ListCreateAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    permission_classes = [IsAuthenticated]


class LivrosDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

