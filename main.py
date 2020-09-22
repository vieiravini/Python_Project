class cliente:

    def __init__(self, *args, **kwarg):
        self.nome = kwarg.get("nome", "")
        self.idade = kwarg.get("idade", 0)
        self.numeroPedido = kwarg.get("numeroPedido", 0)
        self.pedido = kwarg.get("pedido", object)

class pedido:
    def __init__(self, *args, **kwarg):
        self.itens = kwarg.get("itens", {})

    def fazerPedido(self, filaPedidos):
        print('fazendo pedido')
        filaPedidos.pop(0)
        print('pedido feito')


def inserir_fila(cliente):
    if cliente.idade > 65:
        filaClientesIdoso.append(cliente)
        filaPedidos.append(cliente.pedido)
    else:
        filaClientesNormal.append(cliente)
        filaPedidos.append(cliente.pedido)

filaClientesNormal = []
filaClientesIdoso = []
filaPedidos =[]

PedidoPablo = pedido(numero=1, itens="mclanchefeliz")
PedidoVitor = pedido(numero=1, itens="quarteirao")
PedidoPedro = pedido(numero=1, itens={"quarteirao", "bigmac"})

Pablo = cliente(nome="Pablo", idade=19, pedido=PedidoPablo)
Vitor = cliente(nome="Vitor", idade=30, pedido=PedidoVitor)
Pedro = cliente(nome="Pedro", idade=76, pedido=PedidoPedro)


inserir_fila(Pablo)
inserir_fila(Vitor)
inserir_fila(Pedro)

print('-----lista de pedidos------')
for i in range(0,3):
    #print(filaClientesNormal[i].pedido.itens)
    
    print(filaPedidos[i].itens)
print('-----lista de pedidos------')

PedidoPablo.fazerPedido(filaPedidos)
PedidoVitor.fazerPedido(filaPedidos)
PedidoPedro.fazerPedido(filaPedidos)


