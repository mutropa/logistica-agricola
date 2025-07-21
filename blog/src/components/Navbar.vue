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
        <li>
          <router-link to="/" :class="[linkClass, 'flex items-center space-x-1 cursor-pointer hover:text-amber-500 transition']">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M13 5v6h6"/></svg>
            <span>Início</span>
          </router-link>
        </li>
        <li>
          <router-link to="/produtores" :class="[linkClass, 'flex items-center space-x-1 cursor-pointer hover:text-amber-500 transition']">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M5.5 21a7 7 0 0113 0"/></svg>
            <span>Produtores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/fornecedores" :class="[linkClass, 'flex items-center space-x-1 cursor-pointer hover:text-amber-500 transition']">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3h-8v4h8z"/></svg>
            <span>Fornecedores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/compradores" :class="[linkClass, 'flex items-center space-x-1 cursor-pointer hover:text-amber-500 transition']">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M3 10h18M12 3v18"/></svg>
            <span>Compradores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/mercado" :class="[linkClass, 'flex items-center space-x-1 cursor-pointer hover:text-amber-500 transition']">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a7 7 0 01-14.8 0"/></svg>
            <span>Mercado</span>
          </router-link>
        </li>
      </ul>

      <!-- Entrar + tema + idioma -->
      <div class="hidden md:flex items-center space-x-4">
        <router-link to="/login" :class="['font-semibold hover:underline', isDark ? 'text-amber-400' : 'text-amber-600','cursor-pointer']">Entrar</router-link>

        <!-- Botão tema -->
        <button @click="toggleTheme" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors" aria-label="Toggle theme">
          <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m8.485-8.485l-.707.707M4.222 4.222l-.707.707M21 12h-1M4 12H3m15.364 6.364l-.707-.707M4.222 19.778l-.707-.707"/>
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-800" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12.79A9 9 0 0112.21 3c0 4.97 4.03 9 9 9z"/>
          </svg>
        </button>

        <!-- Botão idioma -->
        <button @click="toggleLanguage" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors font-semibold" aria-label="Toggle language">
          {{ currentLanguage.toUpperCase() }}
        </button>
      </div>

      <!-- Botão burger -->
      <button @click="menuOpen = !menuOpen" class="md:hidden focus:outline-none" :class="isDark ? 'text-white' : 'text-gray-800'" aria-label="Menu">
        <svg v-if="!menuOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
        </svg>
      </button>
    </nav>

    <!-- Menu Mobile -->
    <transition name="fade">
      <ul v-if="menuOpen" :class="['md:hidden px-6 py-4 space-y-4 font-medium text-lg transition-all duration-300', isDark ? 'bg-black/90 border-b-gray-700 text-white' : 'bg-white/90 border-b-gray-300 text-gray-800']">
        <li>
          <router-link to="/" class="flex items-center space-x-1 hover:text-amber-500 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M3 12l2-2m0 0l7-7 7 7M13 5v6h6"/></svg>
            <span>Início</span>
          </router-link>
        </li>
        <li>
          <router-link to="/produtores" class="flex items-center space-x-1 hover:text-amber-500 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="7" r="4"/><path d="M5.5 21a7 7 0 0113 0"/></svg>
            <span>Produtores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/fornecedores" class="flex items-center space-x-1 hover:text-amber-500 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 3h-8v4h8z"/></svg>
            <span>Fornecedores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/compradores" class="flex items-center space-x-1 hover:text-amber-500 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M3 10h18M12 3v18"/></svg>
            <span>Compradores</span>
          </router-link>
        </li>
        <li>
          <router-link to="/mercado" class="flex items-center space-x-1 hover:text-amber-500 transition cursor-pointer">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a7 7 0 01-14.8 0"/></svg>
            <span>Mercado</span>
          </router-link>
        </li>
        <li>
          <router-link to="/login" class="font-semibold hover:underline text-amber-600 cursor-pointer">Entrar</router-link>
        </li>
        <li>
          <!-- Tema toggle no mobile -->
          <button @click="toggleTheme" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors w-full flex justify-center" aria-label="Toggle theme">
            <span>Toggle Tema</span>
          </button>
        </li>
        <li>
          <!-- Idioma toggle no mobile -->
          <button @click="toggleLanguage" class="p-2 rounded-md hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors w-full font-semibold" aria-label="Toggle language">
            Idioma: {{ currentLanguage.toUpperCase() }}
          </button>
        </li>
      </ul>
    </transition>
  </header>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const isDark = ref(false)
const menuOpen = ref(false)
const languages = ['pt', 'en']
const currentLanguage = ref('pt')

const toggleTheme = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
}

const toggleLanguage = () => {
  const currentIndex = languages.indexOf(currentLanguage.value)
  currentLanguage.value = languages[(currentIndex + 1) % languages.length]
  // Aqui você pode adicionar lógica para atualizar texto, carregar traduções, etc.
}

const linkClass = computed(() => {
  return isDark.value
    ? 'text-gray-300 hover:text-amber-500'
    : 'text-gray-700 hover:text-amber-600'
})

// Mantém o tema dark se o usuário trocar de página
watch(isDark, (val) => {
  if (val) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
})

// Mantém o idioma atual em localStorage (opcional)
watch(currentLanguage, (val) => {
  localStorage.setItem('olola-language', val)
})

// Recupera idioma do localStorage ao montar
const savedLanguage = localStorage.getItem('olola-language')
if (savedLanguage && languages.includes(savedLanguage)) {
  currentLanguage.value = savedLanguage
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
