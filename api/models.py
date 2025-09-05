from django.db import models

class Autor(models.Model):
    autor = models.CharField(max_length=100)
    s_autor = models.CharField(max_length=100)
    nasc = models.DateField(null=True, blank=True)
    nacio = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.autor} {self.s_nome}'

class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.editora


class Livros(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=255)
    descricao = models.TextField()
    idioma = models.CharField(max_length=255, default="portugues")
    ano_publicacao =  models.IntegerField()
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)






#     nome CharField(max_length=100) Nome da editora (ex: Companhia das 
# Letras).
# cnpj CharField(max_length=18, unique=True, 
# null=True, blank=True) CNPJ da empresa (opcional e único).
# endereco CharField(max_length=200, null=True, 
# blank=True) Endereço físico da editora.
# telefone CharField(max_length=20, null=True, 
# blank=True) Telefone de contato da editora.
# email EmailField(null=True, blank=True) E-mail de contato da editora.
# site URLField(null=True, blank=True) Site da editora (opcional)    