<template>
    <footer class="bg-white border-t border-gray-200 text-gray-700 text-sm">
      <!-- Colunas principais -->
      <div class="max-w-6xl mx-auto px-6 py-12 grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Sobre -->
        <div>
          <h3 class="font-semibold mb-4">Sobre</h3>
          <p class="text-sm leading-relaxed">
            Sou um desenvolvedor de software focado em soluções para o setor agrícola em Moçambique,
            unindo tecnologia e inovação para impulsionar o desenvolvimento local.
          </p>
        </div>
  
        <!-- Categorias -->
        <div>
          <h3 class="font-semibold mb-4">Categorias</h3>
          <ul class="space-y-2">
            <li><a href="/agtech" class="hover:text-amber-500 transition">AgTech Moçambique</a></li>
            <li><a href="/precisao" class="hover:text-amber-500 transition">Agricultura de Precisão</a></li>
            <li><a href="/ia-campo" class="hover:text-amber-500 transition">IA no Campo</a></li>
            <li><a href="/eventos" class="hover:text-amber-500 transition">Eventos e Comunidade</a></li>
          </ul>
        </div>
  
        <!-- Links Rápidos -->
        <div>
          <h3 class="font-semibold mb-4">Links Rápidos</h3>
          <ul class="space-y-2">
            <li><a href="/" class="hover:text-amber-500 transition">Início</a></li>
            <li><a href="/posts" class="hover:text-amber-500 transition">Postagens</a></li>
            <li><a href="/sobre" class="hover:text-amber-500 transition">Sobre Mim</a></li>
            <li><a href="/contato" class="hover:text-amber-500 transition">Contato</a></li>
          </ul>
        </div>
  
        <!-- Newsletter -->
        <div>
          <h3 class="font-semibold mb-4">Newsletter</h3>
          <p class="mb-4">Receba atualizações sobre tecnologia agrícola em Moçambique diretamente no seu e-mail.</p>
          <form @submit.prevent="subscribe">
            <input
              v-model="email"
              type="email"
              placeholder="Seu e-mail"
              class="w-full px-4 py-2 border border-gray-300 rounded mb-2 focus:outline-none focus:ring-2 focus:ring-amber-500"
            />
            <button
              type="submit"
              class="w-full bg-amber-500 text-white py-2 rounded hover:bg-amber-600 transition"
            >
              Inscrever-se
            </button>
          </form>
        </div>
      </div>
  
      <!-- Seção de redes sociais e copyright -->
      <div class="bg-gray-100">
        <div class="max-w-6xl mx-auto px-6 py-4 flex flex-col md:flex-row items-center justify-between">
          <p class="text-sm text-gray-500">© 2025 Anax Bonitao. Todos os direitos reservados.</p>
          <div class="flex space-x-4 mt-2 md:mt-0">
            <!-- Ícones de redes sociais -->
            <a href="https://twitter.com/seu_usuario" target="_blank" class="text-gray-500 hover:text-amber-500 transition" aria-label="Twitter">
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><!-- SVG do Twitter --></svg>
            </a>
            <a href="https://linkedin.com/in/seu_usuario" target="_blank" class="text-gray-500 hover:text-amber-500 transition" aria-label="LinkedIn">
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><!-- SVG do LinkedIn --></svg>
            </a>
            <a href="https://github.com/seu_usuario" target="_blank" class="text-gray-500 hover:text-amber-500 transition" aria-label="GitHub">
              <svg class="h-5 w-5" fill="currentColor" viewBox="0 0 24 24"><!-- SVG do GitHub --></svg>
            </a>
          </div>
        </div>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: 'Footer',
    data() {
      return {
        email: ''
      };
    },
    methods: {
      subscribe() {
        // Aqui você pode integrar API de newsletter ou serviço externo
        alert(`Inscrito: ${this.email}`);
        this.email = '';
      }
    }
  };
  </script>
  
  <style scoped>
  /* Adicione estilos específicos ao footer, se necessário */
  </style>
  