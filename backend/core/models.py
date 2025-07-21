from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

# Usuário genérico com tipos
class User(AbstractUser):
    USER_TYPES = [
        ('produtor', 'Produtor'),
        ('comprador', 'Comprador'),
        ('transportador', 'Transportador'),
    ]
    tipo = models.CharField(max_length=20, choices=USER_TYPES)
    is_verified = models.BooleanField(default=False)

class Localizacao(models.Model):
    cidade = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    bairro=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.cidade}, {self.provincia}"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios/', blank=True, null=True)

# Produto cadastrado por produtor
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    unidade_medida = models.CharField(max_length=50)  # ex: kg, litro
    produtor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'produtor'})
    data_colheita=models.DateField(default=date.today)

# Oferta de produto por produtor
class OfertaProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_disponivel = models.DateField(default=date.today)
    ativo = models.BooleanField(default=True)

# Pedido feito por comprador
class PedidoProduto(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'comprador'})
    oferta = models.ForeignKey(OfertaProduto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pendente')  # pendente, aceito, entregue

# Transporte de pedidos
class Transporte(models.Model):
    pedido = models.OneToOneField(PedidoProduto, on_delete=models.CASCADE)
    transportador = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'tipo': 'transportador'})
    data_agendada = models.DateField(default=date.today)
    status = models.CharField(max_length=20, default='em planejamento')  # em planejamento, em rota, entregue

class Pagamento(models.Model):
      pedido = models.OneToOneField(PedidoProduto, on_delete=models.CASCADE)
      valor=models.DecimalField(max_digits=10, decimal_places=2)
      status = models.CharField(max_length=20, default='Em espera')
      metodo=models.CharField(max_length=20, default='Mpesa')

class Produtor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=100)
    experiencia = models.TextField(blank=True)

class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferencias_compra = models.TextField(blank=True)

class Transportador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    capacidade_carga = models.DecimalField(max_digits=10, decimal_places=2, default=0)






