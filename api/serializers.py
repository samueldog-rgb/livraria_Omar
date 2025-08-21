from rest_framework import serializers
from .models import Autor, Editora, Livros

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        
class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivrosSerializer(serializers.ModelSerializer):
    editora = EditoraSerializer(read_only=True)
    editora_id = serializers.PrimaryKeyRelatedField(
        queryset = Editora.objects.all(), source= 'editora', write_only=True
    )


    class Meta:
        model = Livros
        fields = ['id', 'titulo' , 'substituto', 'editora', 'autor', 'isbn', 
                   'ano_publicacao', 'paginas','preco','estoque','desconto',
                     'disponivel', 'dimensoes',  'peso', 'editora', 'editora_id']