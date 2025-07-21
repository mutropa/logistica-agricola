<template>
  <section class="bg-white pt-6 py-16 px-4 sm:px-6 lg:px-8" id="logistica">
    <div class="container mx-auto px-4">
      <h2 class="text-2xl font-bold text-center mb-14 text-gray-800 tracking-tight relative inline-block">
        <span class="after:block after:w-16 after:h-1 after:bg-amber-500 after:mx-auto after:mt-2">
          Logística e Transporte
        </span>
      </h2>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <!-- Lado esquerdo: Ilustração -->
        <div class="flex flex-col items-center">
          <img src="https://cdn-icons-png.flaticon.com/512/1995/1995524.png" alt="Transporte" class="w-64 h-64 mb-6" />
          <img src="https://img.freepik.com/free-vector/african-man-character-portrait_1308-133651.jpg" alt="Africano" class="w-40 h-40 rounded-full shadow-lg" />
          <p class="mt-4  text-sm text-center text-gray-600 max-w-xs">Transportadores locais conectando comunidades e fortalecendo a cadeia agrícola moçambicana.</p>
        </div>

        <!-- Lado direito: Lista de transportadores -->
        <div class="bg-blue-50 p-6 rounded-2xl shadow-lg">
          <h3 class="text-lg font-medium text-blue-700 mb-4">Transportadores Ativos</h3>
          <div class="space-y-4">
            <div
              v-for="t in transportadores"
              :key="t.id"
              class="bg-white rounded-xl p-4 shadow flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:shadow-md transition"
            >
              <div>
                <h4 class="text-lg font-bold text-gray-800">{{ t.nome }}</h4>
                <p class="text-sm text-gray-600">🚚 {{ t.veiculo }} • {{ t.capacidade }}</p>
                <p class="text-sm text-gray-600">📍 {{ t.regiao }}</p>

                <!-- Estrelas de confiabilidade -->
                <div class="flex items-center mt-2">
                  <span
                    v-for="i in 5"
                    :key="i"
                    class="text-yellow-400 text-lg"
                  >
                    {{ i <= t.classificacao ? '★' : '☆' }}
                  </span>
                  <span class="ml-2 text-xs text-gray-500">(Confiabilidade)</span>
                </div>

                <!-- Contato Oculto -->
                <div class="mt-2 text-sm text-gray-500">
                  📞 Contacto: <span class="font-medium text-gray-700">+258 *** *** ***</span>
                  <span class="block text-xs italic text-red-500">* Informação reservada. Disponível após adesão ao serviço.</span>
                </div>
              </div>

              <div class="text-right">
                <p class="text-sm text-green-600 font-semibold">💰 {{ t.preco }} MT</p>
                <p
                  class="text-xs font-medium mt-1"
                  :class="{
                    'text-green-700': t.status === 'Disponível',
                    'text-yellow-600': t.status === 'Em trânsito'
                  }"
                >
                  {{ t.status }}
                </p>
              </div>
            </div>
          </div>

          <button
            @click="irParaCadastro"
            class="mt-6 w-full bg-amber-500 text-white font-semibold py-2 px-4 rounded-xl hover:bg-amber-600 transition"
          >
          Inscrever-me
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const transportadores = [
  {
    id: 1,
    nome: 'Sidonio Mutropa',
    veiculo: 'Caminhão Baú',
    capacidade: '10 Toneladas',
    regiao: 'Nampula - Nacala',
    preco: 500,
    status: 'Disponível',
    classificacao: 4
  },
  {
    id: 2,
    nome: 'Julieta Albano',
    veiculo: 'Pick-up',
    capacidade: '1.5 Toneladas',
    regiao: 'Nampula - Ilha de Moçambique',
    preco: 250,
    status: 'Em trânsito',
    classificacao: 3
  }
]

const irParaCadastro = () => {
  window.location.href = '/cadastro-transportador'
}
</script>
