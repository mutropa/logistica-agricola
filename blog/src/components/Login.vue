<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-emerald-100 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden">
      <!-- Cabeçalho com imagem temática -->
      <div class="relative h-40 bg-gradient-to-r from-green-600 to-emerald-700">
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="text-center p-4">
            <i class="fas fa-leaf text-5xl text-white opacity-80 mb-2"></i>
            <h1 class="text-2xl font-bold text-white">Sidonio Mutropa</h1>
          </div>
        </div>
        <div class="absolute bottom-0 left-0 right-0 h-12 bg-white rounded-t-3xl"></div>
      </div>

      <!-- Formulário -->
      <div class="px-8 py-6">
        <h2 class="text-2xl font-bold text-gray-800 mb-1">Entrar no Sistema</h2>
        <p class="text-gray-600 mb-6">Acesse sua conta para gerenciar sua produção</p>

        <form @submit.prevent="login">
          <div class="mb-5">
            <label class="block text-gray-700 mb-2 font-medium">Email/Usuário</label>
            <div class="relative">
              <i class="fas fa-user absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
              <input 
                v-model="username"
                type="text" 
                class="w-full pl-12 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                placeholder="seu.email@exemplo.com"
                required
              >
            </div>
          </div>
          
          <div class="mb-6">
            <label class="block text-gray-700 mb-2 font-medium">Senha</label>
            <div class="relative">
              <i class="fas fa-lock absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
              <input 
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                class="w-full pl-12 pr-12 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                placeholder="Digite sua senha"
                required
              >
              <button 
                type="button" 
                class="absolute right-4 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
                @click="showPassword = !showPassword"
              >
                <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
              </button>
            </div>
          </div>
          
          <button 
            type="submit" 
            class="w-full bg-gradient-to-r from-green-600 to-emerald-700 text-white py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 font-medium"
            :disabled="loading"
          >
            <span v-if="!loading">Entrar</span>
            <span v-else class="flex items-center justify-center">
              <i class="fas fa-spinner fa-spin mr-2"></i> Autenticando...
            </span>
          </button>
          
          <div v-if="error" class="mt-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-xl">
            <i class="fas fa-exclamation-circle mr-2"></i> {{ error }}
          </div>
        </form>

        <div class="mt-6 pt-5 border-t border-gray-200">
          <p class="text-gray-600 text-center">
            Ainda não tem uma conta?
            <router-link 
              to="/registar" 
              class="text-green-600 font-medium hover:text-green-800 hover:underline"
            >
              Registe-se aqui
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')
const error = ref(null)
const loading = ref(false)
const showPassword = ref(false)

const login = async () => {
  error.value = null
  loading.value = true
  
  try {
    const response = await fetch('http://localhost:8000/api/authentication/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        username: username.value,
        password: password.value,
      }),
    })

    if (!response.ok) {
      const errorData = await response.json()
      throw new Error(errorData.detail || 'Credenciais inválidas')
    }

    const data = await response.json()
    console.log('Resposta da API:', data)
    
    let tipo
    if (data.access) {
      // Decodifica o JWT para pegar o tipo
      const payload = JSON.parse(atob(data.access.split('.')[1]))
      tipo = payload.tipo
    }
    
    console.log('Tipo do usuário:', tipo)
    
    // Armazena tokens e informações do usuário
    localStorage.setItem('access', data.access)
    localStorage.setItem('tipo', tipo)

    // Redireciona conforme o tipo
    if (tipo === 'produtor') router.push('/produtor/dashboard')
    else if (tipo === 'comprador') router.push('/comprador/dashboard')
    else if (tipo === 'transportador') router.push('/transportador/dashboard')
    else router.push('/login')

  } catch (err) {
    console.error('Erro no login:', err)
    error.value = err.message || 'Erro ao tentar fazer login. Tente novamente.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');

/* Adicionando animação para o spinner */
.fa-spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>