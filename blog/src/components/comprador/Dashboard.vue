<template>
  <div class="flex min-h-screen bg-gray-50">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-xl border-r border-gray-200 p-4">
      <h2 class="text-2xl font-bold text-purple-700 mb-6">🌿 Zinha Mutropa</h2>
      <nav class="space-y-4">
        <a href="#" class="flex items-center space-x-2 text-purple-800 hover:text-purple-600">
          <i class="fas fa-home"></i><span>Início</span>
        </a>
        <a href="#" class="flex items-center space-x-2 text-purple-800 hover:text-purple-600">
          <i class="fas fa-boxes"></i><span>Meus Insumos</span>
        </a>
        <a href="#" class="flex items-center space-x-2 text-purple-800 hover:text-purple-600">
          <i class="fas fa-shopping-basket"></i><span>Pedidos de Produtores</span>
        </a>
        <a href="#" class="flex items-center space-x-2 text-purple-800 hover:text-purple-600">
          <i class="fas fa-truck"></i><span>Entregas</span>
        </a>
        <a href="#" class="flex items-center space-x-2 text-purple-800 hover:text-purple-600">
          <i class="fas fa-chart-line"></i><span>Relatórios</span>
        </a>
        <a href="#" class="flex items-center space-x-2 text-red-600 hover:text-red-400">
          <i class="fas fa-sign-out-alt"></i><span>Sair</span>
        </a>
      </nav>
    </aside>

    <!-- Main content -->
    <main class="flex-1 p-6">
      <header class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold text-gray-800">Painel do Fornecedor</h1>
        <div class="text-sm text-gray-500">Bem-vindo de volta!</div>
      </header>

      <!-- Seção Meus Insumos -->
      <section class="mb-10">
        <h2 class="text-xl font-semibold text-purple-700 mb-4">📦 Meus Insumos</h2>
        <table class="min-w-full bg-white border border-gray-200 shadow-sm">
          <thead>
            <tr class="bg-purple-100 text-left">
              <th class="p-3">Nome</th>
              <th class="p-3">Categoria</th>
              <th class="p-3">Quantidade</th>
              <th class="p-3">Preço</th>
              <th class="p-3">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="p-3">Adubo Orgânico</td>
              <td class="p-3">Fertilizante</td>
              <td class="p-3">500 kg</td>
              <td class="p-3">R$ 35,00</td>
              <td class="p-3 space-x-2">
                <button class="text-blue-500 hover:underline">Editar</button>
                <button class="text-red-500 hover:underline">Excluir</button>
              </td>
            </tr>
            <!-- Repetir conforme dados -->
          </tbody>
        </table>
      </section>

      <!-- Seção Pedidos -->
      <section class="mb-10">
        <h2 class="text-xl font-semibold text-purple-700 mb-4">🧾 Pedidos de Produtores</h2>
        <ul class="space-y-4">
          <li class="bg-white p-4 rounded shadow border">
            <strong>Produtor:</strong> Maria Silva <br>
            <strong>Itens:</strong> 20 kg de semente de milho <br>
            <strong>Status:</strong> Pendente
          </li>
        </ul>
      </section>

      <!-- Seção Entregas -->
      <section class="mb-10">
        <h2 class="text-xl font-semibold text-purple-700 mb-4">🚚 Entregas</h2>
        <ul class="space-y-4">
          <li class="bg-white p-4 rounded shadow border">
            <strong>Destino:</strong> Fazenda Nhapossa <br>
            <strong>Data:</strong> 15/06/2025 <br>
            <strong>Status:</strong> Em transporte
          </li>
        </ul>
      </section>

      <!-- Seção Gráfico -->
      <section>
        <h2 class="text-xl font-semibold text-purple-700 mb-4">📊 Fornecimento Mensal</h2>
        <!-- Aqui entra o componente vue-chartjs -->
        <LineChart :chart-data="lineData" :chart-options="lineOptions" />
      </section>
    </main>
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

const lineData = {
  labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
  datasets: [
    {
      label: 'Insumos Entregues (kg)',
      backgroundColor: '#C084FC',
      borderColor: '#9333EA',
      data: [200, 400, 350, 300, 500, 450],
      fill: false,
      tension: 0.4
    }
  ]
}

const lineOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    title: { display: true, text: 'Entregas Mensais' }
  }
}
</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
}
</style>

<!-- Lembrete: certifique-se que Font Awesome esteja incluído no seu projeto -->