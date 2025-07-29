<template>
  <div class="bg-gray-50 min-h-screen pt-[60px]">
    <Navbar />

    <!-- Seta para baixo -->
    <transition name="fade">
      <div
        v-if="showDownArrow"
        class="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 animate-bounce text-amber-600"
      >
        <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </div>
    </transition>

    <!-- Seta para cima -->
    <transition name="fade">
      <div
        v-if="showUpArrow"
        class="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50 animate-bounce text-green-600"
      >
        <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7" />
        </svg>
      </div>
    </transition>

    <main>
      <section
        class="relative h-[90vh] flex flex-col items-center justify-center text-center text-white"
        style="background: url('/public/assets/imagens/home.png') center/cover"
      >
        <div class="bg-black/50 p-8 rounded-lg animate-[fadeInUp_1s_ease-out]">
          <h1 class="text-5xl font-bold mb-4">O futuro nasce aqui</h1>
<p class="mb-6 text-lg italic">Tecnologia que respeita as raízes e conecta o coração africano ao mundo</p>

          <button class="px-6 py-3 bg-amber-500 hover:bg-amber-600 rounded-full font-semibold">Saiba Mais</button>
        </div>

        <div class="absolute bottom-20 w-full flex flex-col items-center px-4">
          <div class="relative w-full max-w-[600px] flex items-center">
            <div class="flex-grow border-t border-white"></div>
            <div class="mx-4 text-white">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35M11 18a7 7 0 100-14 7 7 0 000 14z" />
              </svg>
            </div>
            <div class="flex-grow border-t border-white"></div>
          </div>

          <div class="mt-4 w-full max-w-[600px] flex justify-between">
            <button class="px-6 py-2 bg-green-600 hover:bg-green-700 rounded-full font-semibold">Comprar</button>
            <button class="px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-full font-semibold">Vender</button>
          </div>
        </div>
      </section>

 <section class="pt-6 pb-16 bg-gray-50" style=" background-image: url('/assets/imagens/africano.png'); background-repeat: no-repeat; background-size: cover;
    background-position: center;
  "
>

 <div class="container mx-auto px-4">
          <h2 class="text-2xl font-extrabold text-center mb-14 text-gray-800 tracking-tight relative inline-block">
            <span class="after:block after:w-16 after:h-1 after:bg-amber-500 after:mx-auto after:mt-2">Produtos em Destaque</span>
          </h2>

          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 px-8 gap-8">
            <div
              v-for="produto in produtos"
              :key="produto.id"
              class="relative bg-white shadow-lg rounded-xl overflow-hidden hover:shadow-xl transition duration-300 flex flex-col"
            >
              <span
                :class="`absolute top-3 left-3 z-10 text-white text-xs font-semibold px-3 py-1 rounded-full ${produto.etiqueta.cor}`">
                {{ produto.etiqueta.texto }}
              </span>

              <img :src="produto.imagem" :alt="produto.nome" class="w-full h-40 object-cover" />

              <div class="p-4 flex flex-col flex-1">
                <h3 class="text-lg font-semibold text-gray-800 mb-1 flex items-center gap-2">
                  <svg class="w-5 h-5" :class="produto.iconeCor" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 3a1 1 0 01.993.883L11 4v5h5a1 1 0 01.117 1.993L16 11h-5v5a1 1 0 01-1.993.117L9 16v-5H4a1 1 0 01-.117-1.993L4 9h5V4a1 1 0 011-1z" />
                  </svg>
                  {{ produto.nome }}
                </h3>
                <p class="text-gray-600 text-sm mb-2">{{ produto.descricao }}</p>

                <div class="text-gray-500 text-xs flex justify-between items-center mb-3">
                  <div class="flex items-center gap-1">
                    <svg class="w-4 h-4 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path d="M17.657 16.657L13.414 12.414 17.657 8.171 16.243 6.757 12 11 7.757 6.757 6.343 8.171 10.586 12.414 6.343 16.657 7.757 18.071 12 13.828 16.243 18.071z" />
                    </svg>
                    {{ produto.visualizacoes }} views
                  </div>
                  <div class="flex items-center gap-1">
                    <svg class="w-4 h-4 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 18.343l-6.828-6.829a4 4 0 010-5.656z" />
                    </svg>
                    {{ produto.likes }}
                  </div>
                </div>

                <div class="mt-auto flex items-center justify-between">
                  <span class="text-amber-600 font-bold text-lg">{{ produto.preco }}</span>
                  <button class="bg-amber-500 hover:bg-amber-600 text-white px-4 py-1 rounded-full text-sm font-medium">Comprar</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
<section class="pt-6 pb-16 -mt-10 bg-gray-50 relative overflow-hidden">
  <div class="container mx-auto px-4">
    <h2 class="text-2xl font-extrabold text-center mb-14 text-gray-800 tracking-tight relative inline-block">
      <span class="after:block after:w-16 after:h-1 after:bg-amber-500 after:mx-auto after:mt-2">Serviços de AI</span>
    </h2>

    <!-- Card único com todos os serviços -->
    <div class="bg-white/80 backdrop-blur-sm p-6 md:p-10 rounded-3xl shadow-md hover:shadow-lg transition-all duration-300 space-y-16">

      <!-- Serviço: Análise de Demanda e Preço com IA -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-10 items-center font-sans text-gray-800">
        <!-- Coluna do conteúdo textual e tabela -->
        <div class="space-y-6">
          <!-- Título e descrição -->
          <div>
            <h3 class="text-2xl font-bold mb-3">
                📊 Análise de Demanda 
            </h3>
             <p class="leading-relaxed text-sm text-gray-600">
              Utilizamos algoritmos de inteligência artificial para prever padrões de demanda e ajustar os preços dos produtos agrícolas de forma dinâmica. Essa abordagem está alinhada com os princípios da <strong>FAO</strong> e de programas do <strong>Ministério da Agricultura</strong>, promovendo decisões comerciais mais estratégicas, menos desperdício e valorização do esforço do produtor.
            </p>
          </div>

          <!-- Campo de pesquisa e tabela -->
          <div class="space-y-4">
            <!-- Campo de pesquisa -->
            <div>
              <input
                type="text"
                id="searchInput"
                placeholder="🔍 Pesquisar por produto ou indicador..."
                class="w-full md:w-2/3 px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-amber-500 focus:border-amber-500 transition"
                onkeyup="filterTable()"
              />
            </div>

            <!-- Tabela de previsões -->
            <div class="overflow-x-auto">
              <table id="forecastTable" class="min-w-full text-sm text-left text-gray-700 bg-white shadow-md rounded-xl overflow-hidden">
                <thead class="bg-amber-100 text-gray-800 text-xs uppercase">
                  <tr>
                    <th class="px-6 py-3">Indicador</th>
                    <th class="px-6 py-3">Produto</th>
                    <th class="px-6 py-3">Valor</th>
                    <th class="px-6 py-3">Observação</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                  <tr class="hover:bg-amber-50 transition">
                    <td class="px-6 py-4 font-medium">📈 Preço Sugerido</td>
                    <td class="px-6 py-4">Milho</td>
                    <td class="px-6 py-4 text-green-600 font-semibold">48 MZN/kg</td>
                    <td class="px-6 py-4">Baseado em previsões regionais</td>
                  </tr>
                  <tr class="hover:bg-green-50 transition">
                    <td class="px-6 py-4 font-medium">📦 Estoque Ideal</td>
                    <td class="px-6 py-4">Feijão</td>
                    <td class="px-6 py-4 font-semibold">800kg</td>
                    <td class="px-6 py-4">Recomendado para zona norte</td>
                  </tr>
                  <tr class="hover:bg-rose-50 transition">
                    <td class="px-6 py-4 font-medium">⚠️ Alerta de Queda</td>
                    <td class="px-6 py-4">Mandioca</td>
                    <td class="px-6 py-4 text-rose-600 font-semibold">Alta oferta</td>
                    <td class="px-6 py-4">Risco de excedente nos próximos 10 dias</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- Coluna do gráfico -->
        <div class="flex justify-center h-full items-stretch">
          <canvas id="forecastChart" class="rounded-2xl h-full shadow-lg ring-1 ring-gray-200 w-full max-w-md"></canvas>
        </div>
      </div>

      

    </div>
  </div>
</section>

<section class="relative py-20 bg-cover bg-center bg-no-repeat overflow-hidden"
         style="background-image: url('/assets/imagens/satelite.jpg');">
  <div class="absolute inset-0 bg-black/30 z-0"></div>

  <div class="container mx-auto px-4 relative z-10">
    <div class="flex flex-col-reverse md:flex-row items-center justify-between gap-12">
      <div class="w-full md:w-2/3 space-y-8 animate-fadeInUp">
        <h2 class="text-2xl md:text-2xl font-bold text-white leading-snug">
          🛰️ Análise Geoespacial Inteligente
        </h2>
        <p class="text-white text-sm leading-relaxed">
          Utilizando dados de satélite, IA e geolocalização, nossa tecnologia identifica zonas agrícolas estratégicas, antecipa padrões climáticos e recomenda áreas ideais para cultivo. Tudo isso para impulsionar o futuro da agricultura africana.
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="bg-white/80 backdrop-blur-md shadow-xl border-l-4 border-green-500 rounded-xl p-5">
            <h4 class="font-semibold text-lg text-gray-800 mb-1">🌍 Área Produtiva Ativa</h4>
            <p class="text-sm text-gray-600">Nampula: <span class="text-green-600 font-bold">12.500 ha</span></p>
          </div>
          <!-- ...outros cards iguais -->
        </div>
      </div>

      <div class="w-full md:w-1/3 flex justify-center">
        <div class="w-full max-w-md h-80 md:h-[400px] bg-white/80 backdrop-blur-md shadow-xl rounded-xl p-3">
          <MapComponent />
        </div>
      </div>
    </div>
  </div>
</section>

    <LogisticaSeccao />

      <Footer />
    </main>
  </div>
</template>

<script>
import Navbar from './Navbar.vue'
import Footer from './Footer.vue'
import Chart from 'chart.js/auto'
import MapComponent from './Map.vue'
import LogisticaSeccao from './LogisticaSeccao.vue'

export default {
  components: { Navbar, Footer,MapComponent,LogisticaSeccao},
  data() {
    return {
      showDownArrow: true,
      showUpArrow: false,
      posts: [
        { id: 1, title: 'Construindo com Vue 3', date: '08 Mai, 2025', slug: 'vue-3', image: '/src/assets/posts/vue3.jpg' },
        { id: 2, title: 'Tailwind no Workflow', date: '01 Mai, 2025', slug: 'tailwind-workflow', image: '/src/assets/posts/tailwind.jpg' },
      ],
      produtos: [
        {
          id: 1,
          nome: 'Milho Amarelo',
          descricao: 'Milho colhido organicamente, ideal para consumo ou revenda.',
          preco: 'MZN 120 /saco',
          imagem: '/assets/imagens/milho.jpg',
          etiqueta: { texto: 'Novo', cor: 'bg-amber-500' },
          iconeCor: 'text-amber-500',
          visualizacoes: 120,
          likes: 34,
        },
        {
          id: 2,
          nome: 'Feijão Nhemba',
          descricao: 'Produção familiar com alto padrão de qualidade.',
          preco: 'MZN 90 /kg',
          imagem: '/assets/imagens/erv.jpg',
          etiqueta: { texto: 'Promoção', cor: 'bg-green-600' },
          iconeCor: 'text-green-600',
          visualizacoes: 95,
          likes: 20,
        },
        {
          id: 3,
          nome: 'Batata Doce',
          descricao: 'Rica em nutrientes e sabor — direto do produtor.',
          preco: 'MZN 50 /kg',
          imagem: '/assets/imagens/batata.jpg',
          etiqueta: { texto: 'Popular', cor: 'bg-blue-600' },
          iconeCor: 'text-blue-600',
          visualizacoes: 78,
          likes: 18,
        },
        {
          id: 4,
          nome: 'Mandioca Fresca',
          descricao: 'Colhida hoje, pronta para cozinhar ou secar.',
          preco: 'MZN 60 /kg',
          imagem: '/assets/imagens/mandioca.jpg',
          etiqueta: { texto: 'Fresca', cor: 'bg-purple-600' },
          iconeCor: 'text-purple-600',
          visualizacoes: 80,
          likes: 25,
        },
        {
          id: 5,
          nome: 'Feijão Manteiga',
          descricao: 'Colhida esta época',
          preco: 'MZN 75 /kg',
          imagem: '/assets/imagens/feijao.jpg',
          etiqueta: { texto: 'Antigo', cor: 'bg-green-600' },
          iconeCor: 'text-purple-600',
          visualizacoes: 80,
          likes: 25,
        },
        {
          id: 6,
          nome: 'Cebola',
          descricao: 'Colhida esta época',
          preco: 'MZN 100/kg',
          imagem: '/assets/imagens/cebola.jpg',
          etiqueta: { texto: 'Antiga', cor: 'bg-purple-600' },
          iconeCor: 'text-purple-600',
          visualizacoes: 60,
          likes: 55,
        },
        {
          id: 7,
          nome: 'Castanha',
          descricao: 'Colhida esta época',
          preco: 'MZN 200/kg',
          imagem: '/assets/imagens/castanha.jpg',
          etiqueta: { texto: 'Nova', cor: 'bg-yellow-600' },
          iconeCor: 'text-purple-600',
          visualizacoes: 50,
          likes: 30,
        },
        {
          id: 8,
          nome: 'Repolho',
          descricao: 'Colhido esta época',
          preco: 'MZN 500/kg',
          imagem: '/assets/imagens/repolho.jpg',
          etiqueta: { texto: 'Seca', cor: 'bg-yellow-600' },
          iconeCor: 'text-purple-600',
          visualizacoes: 120,
          likes: 50,
        }
      ]
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    this.initChart()
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll() {
      const scrollY = window.scrollY
      this.showDownArrow = scrollY < 50
      this.showUpArrow = scrollY > 300 && this.posts.length >= 2
    },
    filterTable() {
    const input = document.getElementById("searchInput");
    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll("#forecastTable tbody tr");

    rows.forEach(row => {
      const text = row.innerText.toLowerCase();
      row.style.display = text.includes(filter) ? "" : "none";
    });
  },

    initChart() {
      // No método initChart, antes de criar o Chart:
   
      const canvas = document.getElementById('forecastChart')
      if (!canvas) return
        canvas.height = canvas.parentElement.offsetHeight;
        canvas.width = canvas.parentElement.offsetWidth;

      const ctx = canvas.getContext('2d')
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro'],
          datasets: [
            {
              label: 'Milho (MZN/kg)',
              data: [30,34,38,45, 47, 48, 49, 50],
              borderColor: '#f59e0b',
              backgroundColor: 'rgba(245, 158, 11, 0.1)',
              fill: true,
              tension: 0.4
            },
            {
              label: 'Feijão (MZN/kg)',
              data: [60, 58, 59, 61, 62,70,74,80],
              borderColor: '#10b981',
              backgroundColor: 'rgba(16, 185, 129, 0.1)',
              fill: true,
              tension: 0.4
            }
          ]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              labels: {
                color: '#374151'
              }
            }
          },
          scales: {
            x: {
              ticks: {
                color: '#6b7280'
              }
            },
            y: {
              ticks: {
                color: '#6b7280'
              }
            }
          }
        }
      })
    }
  }
}
</script>
<style>
  @keyframes spin-slow {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }

  .animate-spin-slow {
    animation: spin-slow 20s linear infinite;
  }
</style>
