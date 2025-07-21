from django.contrib import admin
from .models import User, Localizacao, Perfil, Produto, OfertaProduto, PedidoProduto, Transporte, Pagamento, Produtor, Comprador, Transportador

admin.site.register(User)
admin.site.register(Localizacao)
admin.site.register(Perfil)
admin.site.register(Produto)
admin.site.register(OfertaProduto)
admin.site.register(PedidoProduto)
admin.site.register(Transporte)
admin.site.register(Pagamento)
admin.site.register(Produtor)
admin.site.register(Comprador)
admin.site.register(Transportador)
