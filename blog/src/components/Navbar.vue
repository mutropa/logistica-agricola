<template>
  <header :class="['fixed top-0 left-0 w-full z-50 transition-colors duration-500', isDark ? 'bg-black/80 border-b-gray-700 text-white' : 'bg-white/90 border-b-gray-300 text-gray-800']">
    <nav class="h-16 px-6 flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center space-x-3">
        <img src="/assets/imagens/logo.png" alt="OlolaAI" class="h-10 w-10 object-cover rounded-full" />
        <span class="font-extrabold text-xl tracking-wide cursor-pointer" :class="isDark ? 'text-amber-500' : 'text-amber-600'">OlolaAI</span>
      </div>

      <!-- Links desktop -->
      <ul class="hidden md:flex space-x-6 font-medium">
        <li><a href="/" :class="[linkClass, 'flex items-center space-x-1']">🏠 Início</a></li>
        <li><a href="/produtores" :class="[linkClass, 'flex items-center space-x-1']">👨‍🌾 Produtores</a></li>
        <li><a href="/fornecedores" :class="[linkClass, 'flex items-center space-x-1']">📦 Fornecedores</a></li>
        <li><a href="/compradores" :class="[linkClass, 'flex items-center space-x-1']">🛒 Compradores</a></li>
        <li><a href="/mercado" :class="[linkClass, 'flex items-center space-x-1']">📈 Mercado</a></li>
      </ul>

      <!-- Ações -->
      <div class="hidden md:flex items-center space-x-4">
        <a href="/login" :class="['font-semibold hover:underline', isDark ? 'text-amber-400' : 'text-amber-600']">Entrar</a>

        <!-- Botão tema -->
        <button @click="toggleTheme" class="p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors" aria-label="Toggle theme">
          <svg v-if="isDark" class="h-6 w-6 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1M4.22 4.22l.7.7M19.08 19.08l.7.7M21 12h-1M4 12H3" />
          </svg>
          <svg v-else class="h-6 w-6 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12.79A9 9 0 0112.21 3c0 4.97 4.03 9 9 9z" />
          </svg>
        </button>

        <!-- Idioma -->
        <button @click="toggleLanguage" class="p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-700 font-semibold">
          {{ currentLanguage.toUpperCase() }}
        </button>
      </div>

      <!-- Menu mobile -->
      <button @click="menuOpen = !menuOpen" class="md:hidden" :class="isDark ? 'text-white' : 'text-gray-800'" aria-label="Menu">
        <svg v-if="!menuOpen" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </nav>

    <!-- Menu mobile (expansível) -->
    <transition name="fade">
      <ul v-if="menuOpen" :class="['md:hidden px-6 py-4 space-y-4 font-medium text-lg', isDark ? 'bg-black/90 text-white' : 'bg-white/90 text-gray-800']">
        <li><a href="/">Início</a></li>
        <li><a href="/produtores">Produtores</a></li>
        <li><a href="/fornecedores">Fornecedores</a></li>
        <li><a href="/compradores">Compradores</a></li>
        <li><a href="/mercado">Mercado</a></li>
        <li><a href="/login">Entrar</a></li>
        <li><button @click="toggleTheme">Toggle Tema</button></li>
        <li><button @click="toggleLanguage">Idioma: {{ currentLanguage.toUpperCase() }}</button></li>
      </ul>
    </transition>
  </header>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'

const isDark = ref(false)
const menuOpen = ref(false)

const languages = ['pt', 'en']
const currentLanguage = ref('pt')

// Tema
const toggleTheme = () => {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle('dark', isDark.value)
}

// Idioma
const toggleLanguage = () => {
  const currentIndex = languages.indexOf(currentLanguage.value)
  currentLanguage.value = languages[(currentIndex + 1) % languages.length]
}

// Salvar idioma no localStorage
watch(currentLanguage, (val) => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('olola-language', val)
  }
})

// Recuperar idioma salvo ao montar (client only)
onMounted(() => {
  const savedLanguage = localStorage.getItem('olola-language')
  if (savedLanguage && languages.includes(savedLanguage)) {
    currentLanguage.value = savedLanguage
  }
})

// Classe dos links com base no tema
const linkClass = computed(() =>
  isDark.value
    ? 'text-gray-300 hover:text-amber-500'
    : 'text-gray-700 hover:text-amber-600'
)
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
