<template>
  <div class="flex min-h-screen bg-gray-100">
    <!-- Sidebar -->
    <aside class="w-64 bg-white shadow-lg border-r border-gray-200 p-6 flex flex-col">
      <h2 class="text-xl font-extrabold text-green-700 mb-10 flex items-center space-x-2">
        <i class="fas fa-truck text-green-600"></i>
        <span> 🌿 Scully Sidonio</span>
      </h2>
      <nav class="flex flex-col space-y-6 text-green-800 text-lg">
        <a href="#" class="flex items-center space-x-3 hover:text-green-600 transition-colors">
          <i class="fas fa-tachometer-alt"></i>
          <span>Painel</span>
        </a>
        <a href="#" class="flex items-center space-x-3 hover:text-green-600 transition-colors">
          <i class="fas fa-box"></i>
          <span>Minhas Entregas</span>
        </a>
        <a href="#" class="flex items-center space-x-3 hover:text-green-600 transition-colors">
          <i class="fas fa-route"></i>
          <span>Rotas</span>
        </a>
        <a href="#" class="flex items-center space-x-3 hover:text-green-600 transition-colors relative">
          <i class="fas fa-bell"></i>
          <span>Notificações</span>
          <span
            class="absolute top-0 right-0 -mt-1 -mr-2 bg-red-600 text-white text-xs font-bold rounded-full px-2 py-0.5"
            >3</span
          >
        </a>
        <a href="#" class="flex items-center space-x-3 hover:text-green-600 transition-colors mt-auto">
          <i class="fas fa-sign-out-alt"></i>
          <span>Sair</span>
        </a>
      </nav>
    </aside>

    <!-- Main content -->
    <main class="flex-1 p-8">
      <header class="mb-8 flex justify-between items-center">
        <h1 class="text-3xl font-bold text-yellow-700">Painel do Transportador</h1>
        <div class="flex items-center space-x-4">
          <button
            title="Notificações"
            class="relative text-gray-600 hover:text-yellow-600 transition-colors"
          >
            <i class="fas fa-bell fa-lg"></i>
            <span
              class="absolute top-0 right-0 -mt-1 -mr-2 bg-red-600 text-white text-xs font-bold rounded-full px-2 py-0.5"
              >3</span
            >
          </button>
          <img
            src="https://i.pravatar.cc/40"
            alt="Perfil"
            class="rounded-full border-2 border-yellow-500"
          />
        </div>
      </header>

      <section class="bg-white rounded-lg shadow p-6 mb-8">
        <h2 class="text-xl font-semibold mb-4 text-yellow-700">Resumo das Entregas</h2>
        <div class="grid grid-cols-3 gap-6 text-center">
          <div class="bg-green-100 p-4 rounded shadow">
            <p class="text-3xl font-bold text-green-700">12</p>
            <p>Entregas Ativas</p>
          </div>
          <div class="bg-yellow-100 p-4 rounded shadow">
            <p class="text-3xl font-bold text-yellow-700">5</p>
            <p>Entregas Pendentes</p>
          </div>
          <div class="bg-red-100 p-4 rounded shadow">
            <p class="text-3xl font-bold text-red-700">2</p>
            <p>Entregas Atrasadas</p>
          </div>
        </div>
      </section>

      <section class="bg-white rounded-lg shadow p-6">
        <h2 class="text-xl font-semibold mb-4 text-yellow-700">Minhas Entregas</h2>
        <table class="w-full text-left table-auto border-collapse">
          <thead>
            <tr class="bg-yellow-200">
              <th class="py-3 px-4 border-b border-yellow-300">ID</th>
              <th class="py-3 px-4 border-b border-yellow-300">Produto</th>
              <th class="py-3 px-4 border-b border-yellow-300">Origem</th>
              <th class="py-3 px-4 border-b border-yellow-300">Destino</th>
              <th class="py-3 px-4 border-b border-yellow-300">Status</th>
              <th class="py-3 px-4 border-b border-yellow-300">Ações</th>
            </tr>
          </thead>
          <tbody>
            <tr class="hover:bg-yellow-50" v-for="entrega in entregas" :key="entrega.id">
              <td class="py-2 px-4 border-b border-gray-200">{{ entrega.id }}</td>
              <td class="py-2 px-4 border-b border-gray-200">{{ entrega.produto }}</td>
              <td class="py-2 px-4 border-b border-gray-200">{{ entrega.origem }}</td>
              <td class="py-2 px-4 border-b border-gray-200">{{ entrega.destino }}</td>
              <td
                class="py-2 px-4 border-b border-gray-200"
                :class="{
                  'text-green-600 font-semibold': entrega.status === 'Entregue',
                  'text-yellow-600 font-semibold': entrega.status === 'Em trânsito',
                  'text-red-600 font-semibold': entrega.status === 'Atrasado'
                }"
              >
                {{ entrega.status }}
              </td>
              <td class="py-2 px-4 border-b border-gray-200 space-x-2">
                <button
                  class="bg-yellow-400 hover:bg-yellow-500 text-white px-3 py-1 rounded text-sm"
                  @click="editarEntrega(entrega.id)"
                >
                  Editar
                </button>
                <button
                  class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm"
                  @click="deletarEntrega(entrega.id)"
                >
                  Deletar
                </button>
              </td>
            </tr>
            <tr v-if="entregas.length === 0">
              <td colspan="6" class="text-center py-4 text-gray-500">Nenhuma entrega encontrada.</td>
            </tr>
          </tbody>
        </table>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const entregas = ref([
  {
    id: 1,
    produto: 'Caixa de Tomates',
    origem: 'Fazenda Olola, Nampula',
    destino: 'Mercado Central',
    status: 'Em trânsito'
  },
  {
    id: 2,
    produto: 'Sacos de Milho',
    origem: 'Fazenda Mutropa',
    destino: 'Armazém Cidade',
    status: 'Entregue'
  },
  {
    id: 3,
    produto: 'Pacotes de Feijão',
    origem: 'Fazenda Viana',
    destino: 'Mercado Central',
    status: 'Atrasado'
  }
])

function editarEntrega(id) {
  alert(`Editar entrega ${id} - funcionalidade em desenvolvimento`)
}

function deletarEntrega(id) {
  const confirmDelete = confirm(`Tem certeza que deseja deletar a entrega ${id}?`)
  if (confirmDelete) {
    entregas.value = entregas.value.filter(e => e.id !== id)
    alert(`Entrega ${id} deletada.`)
  }
}
</script>

<style scoped>
/* Fonte Inter para ficar mais moderno */
@import url('https://fonts.googleapis.com/css2?family=Inter&display=swap');

body {
  font-family: 'Inter', sans-serif;
}
</style>
