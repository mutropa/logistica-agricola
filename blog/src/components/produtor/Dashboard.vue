<template>
  <div class="flex min-h-screen bg-gray-100 text-gray-800">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-xl border-r border-gray-200 p-4 h-screen flex flex-col justify-between sticky top-0">
      <div>
        <h2 class="text-xl font-bold text-green-700 mb-6 flex items-center gap-2">
          <span>🌿</span> Sidonio Mutropa
        </h2>
        <nav class="space-y-4">
          <a href="#" class="flex items-center space-x-3 text-green-700 bg-green-50 p-2 rounded-lg font-medium">
            <i class="fas fa-home w-5 text-center"></i>
            <span>Painel</span>
          </a>
          <a href="#" class="flex items-center space-x-3 text-gray-600 hover:text-green-700 hover:bg-green-50 p-2 rounded-lg transition">
            <i class="fas fa-plus-circle w-5 text-center"></i>
            <span>Cadastrar Produto</span>
          </a>
          <a href="#" class="flex items-center space-x-3 text-gray-600 hover:text-green-700 hover:bg-green-50 p-2 rounded-lg transition">
            <i class="fas fa-shopping-cart w-5 text-center"></i>
            <span>Pedidos</span>
            <span class="bg-red-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center ml-auto">3</span>
          </a>
          <a href="#" class="flex items-center space-x-3 text-gray-600 hover:text-green-700 hover:bg-green-50 p-2 rounded-lg transition">
            <i class="fas fa-chart-line w-5 text-center"></i>
            <span>Relatórios</span>
          </a>
          <a href="#" class="flex items-center space-x-3 text-gray-600 hover:text-green-700 hover:bg-green-50 p-2 rounded-lg transition">
            <i class="fas fa-bell w-5 text-center"></i>
            <span>Notificações</span>
            <span class="bg-yellow-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center ml-auto">2</span>
          </a>
          <a href="#" class="flex items-center space-x-3 text-gray-600 hover:text-green-700 hover:bg-green-50 p-2 rounded-lg transition">
            <i class="fas fa-truck w-5 text-center"></i>
            <span>Transportes</span>
          </a>
        </nav>
      </div>

      <!-- Rodapé -->
      <div class="mt-6 border-t pt-4">
        <a href="#" class="flex items-center space-x-3 text-red-600 hover:text-red-800 p-2 rounded-lg transition">
          <i class="fas fa-sign-out-alt"></i>
          <span>Sair</span>
        </a>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 p-6">
      <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
        <div>
          <h1 class="text-2xl md:text-3xl font-semibold text-gray-800">Painel do Produtor</h1>
          <p class="text-gray-600 text-sm">Bem-vindo, Sidônio! Hoje é 22 de Junho de 2025</p>
        </div>
        
        <div class="flex gap-3">
          <div class="relative w-full sm:w-64">
            <label for="busca" class="sr-only">Buscar</label>
            <input
              id="busca"
              type="text"
              placeholder="Buscar produto, pedido, cliente..."
              class="w-full px-4 py-2 pl-10 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500"
            />
            <span class="absolute left-3 top-2.5 text-gray-500">
              🔍
            </span>
          </div>
          <button class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg shadow flex items-center gap-2">
            <i class="fas fa-plus"></i> Novo
          </button>
        </div>
      </div>

      <!-- Cards de Resumo -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <!-- Produtos -->
        <div class="bg-white rounded-lg p-5 shadow-md border-l-4 border-green-500">
          <div class="flex items-center gap-3 mb-3">
            <div class="bg-green-100 p-3 rounded-full">
              <i class="fas fa-seedling text-green-600"></i>
            </div>
            <h2 class="text-lg font-bold text-gray-700">Produtos</h2>
          </div>
          <p class="text-2xl font-bold">12</p>
          <p class="text-sm text-gray-500 mt-1">10 ativos, 2 inativos</p>
          <div class="mt-3 pt-3 border-t">
            <p class="flex justify-between text-sm">
              <span class="text-gray-600">Estoque baixo:</span>
              <span class="font-medium text-red-600">2 produtos</span>
            </p>
          </div>
        </div>

        <!-- Pedidos -->
        <div class="bg-white rounded-lg p-5 shadow-md border-l-4 border-yellow-500">
          <div class="flex items-center gap-3 mb-3">
            <div class="bg-yellow-100 p-3 rounded-full">
              <i class="fas fa-shopping-cart text-yellow-600"></i>
            </div>
            <h2 class="text-lg font-bold text-gray-700">Pedidos</h2>
          </div>
          <p class="text-2xl font-bold">8</p>
          <p class="text-sm text-gray-500 mt-1">5 confirmados, 3 pendentes</p>
          <div class="mt-3 pt-3 border-t">
            <p class="flex justify-between text-sm">
              <span class="text-gray-600">Último pedido:</span>
              <span class="font-medium">3 dias atrás</span>
            </p>
          </div>
        </div>

        <!-- Transportes -->
        <div class="bg-white rounded-lg p-5 shadow-md border-l-4 border-blue-500">
          <div class="flex items-center gap-3 mb-3">
            <div class="bg-blue-100 p-3 rounded-full">
              <i class="fas fa-truck text-blue-600"></i>
            </div>
            <h2 class="text-lg font-bold text-gray-700">Transportes</h2>
          </div>
          <p class="text-2xl font-bold">2</p>
          <p class="text-sm text-gray-500 mt-1">1 em rota, 1 agendado</p>
          <div class="mt-3 pt-3 border-t">
            <p class="flex justify-between text-sm">
              <span class="text-gray-600">Próximo:</span>
              <span class="font-medium">Amanhã</span>
            </p>
          </div>
        </div>

        <!-- Financeiro -->
        <div class="bg-white rounded-lg p-5 shadow-md border-l-4 border-purple-500">
          <div class="flex items-center gap-3 mb-3">
            <div class="bg-purple-100 p-3 rounded-full">
              <i class="fas fa-wallet text-purple-600"></i>
            </div>
            <h2 class="text-lg font-bold text-gray-700">Financeiro</h2>
          </div>
          <p class="text-2xl font-bold">R$ 8.240</p>
          <p class="text-sm text-gray-500 mt-1">A receber este mês</p>
          <div class="mt-3 pt-3 border-t">
            <p class="flex justify-between text-sm">
              <span class="text-gray-600">Lucro médio:</span>
              <span class="font-medium text-green-600">27%</span>
            </p>
          </div>
        </div>
      </div>

      <!-- Gráficos e Tabelas -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <!-- Gráfico de Vendas -->
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-green-800">Histórico de Vendas</h2>
            <select class="border border-gray-300 rounded px-3 py-1 text-sm">
              <option>Últimos 6 meses</option>
              <option>2024</option>
            </select>
          </div>
          <ChartComponent />
        </div>

        <!-- Pedidos Recentes -->
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-green-800">Pedidos Recentes</h2>
            <a href="#" class="text-green-600 hover:text-green-800 text-sm">Ver todos</a>
          </div>
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Produto</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Comprador</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Quantidade</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">Soja</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">AgroIndústria ABC</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">500 sacas</td>
                  <td class="px-4 py-3 whitespace-nowrap">
                    <span class="px-2 py-1 text-xs bg-green-100 text-green-800 rounded-full">Entregue</span>
                  </td>
                </tr>
                <tr>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">Milho</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">Distribuidora XYZ</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">300 sacas</td>
                  <td class="px-4 py-3 whitespace-nowrap">
                    <span class="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 rounded-full">Pendente</span>
                  </td>
                </tr>
                <tr>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">Arroz</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">Supermercado 123</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm">200 sacas</td>
                  <td class="px-4 py-3 whitespace-nowrap">
                    <span class="px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full">Em transporte</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Próximos Transportes -->
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-green-800">Próximos Transportes</h2>
            <a href="#" class="text-green-600 hover:text-green-800 text-sm">Ver agenda</a>
          </div>
          <div class="space-y-4">
            <div class="flex items-start gap-4 p-3 border border-gray-200 rounded-lg">
              <div class="bg-blue-100 p-2 rounded-full mt-1">
                <i class="fas fa-truck text-blue-600"></i>
              </div>
              <div class="flex-1">
                <h3 class="font-medium">Soja para AgroIndústria ABC</h3>
                <p class="text-sm text-gray-600">500 sacas · Talhão 3</p>
                <div class="flex justify-between mt-2">
                  <span class="text-sm bg-gray-100 px-2 py-1 rounded flex items-center gap-1">
                    <i class="fas fa-calendar"></i> 23/06/2025
                  </span>
                  <span class="text-sm bg-gray-100 px-2 py-1 rounded flex items-center gap-1">
                    <i class="fas fa-user"></i> Transportadora Norte
                  </span>
                </div>
              </div>
            </div>
            
            <div class="flex items-start gap-4 p-3 border border-gray-200 rounded-lg">
              <div class="bg-green-100 p-2 rounded-full mt-1">
                <i class="fas fa-tractor text-green-600"></i>
              </div>
              <div class="flex-1">
                <h3 class="font-medium">Colheita de Milho</h3>
                <p class="text-sm text-gray-600">Talhão 2 · 10 hectares</p>
                <div class="flex justify-between mt-2">
                  <span class="text-sm bg-gray-100 px-2 py-1 rounded flex items-center gap-1">
                    <i class="fas fa-calendar"></i> 25/06/2025
                  </span>
                  <span class="text-sm bg-gray-100 px-2 py-1 rounded flex items-center gap-1">
                    <i class="fas fa-clock"></i> 08:00 AM
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Alertas e Notificações -->
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-xl font-semibold text-green-800">Alertas Importantes</h2>
            <span class="bg-red-500 text-white text-xs rounded-full h-6 w-6 flex items-center justify-center">2</span>
          </div>
          <div class="space-y-4">
            <div class="flex items-start gap-3 p-3 bg-red-50 border border-red-200 rounded-lg">
              <i class="fas fa-exclamation-triangle text-red-500 mt-1"></i>
              <div>
                <h3 class="font-medium">Estoque crítico de Feijão</h3>
                <p class="text-sm text-gray-600">Apenas 15 sacas disponíveis</p>
              </div>
            </div>
            
            <div class="flex items-start gap-3 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
              <i class="fas fa-cloud-sun text-yellow-500 mt-1"></i>
              <div>
                <h3 class="font-medium">Previsão de chuva forte</h3>
                <p class="text-sm text-gray-600">25/06 - Atraso possível na colheita</p>
              </div>
            </div>
            
            <div class="flex items-start gap-3 p-3 bg-blue-50 border border-blue-200 rounded-lg">
              <i class="fas fa-file-invoice-dollar text-blue-500 mt-1"></i>
              <div>
                <h3 class="font-medium">Pagamento pendente</h3>
                <p class="text-sm text-gray-600">Distribuidora XYZ · R$ 2.450,00</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import ChartComponent from './ChartComponent.vue'
</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
}

.sticky {
  position: sticky;
}

.fa, .fas {
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
}
</style>