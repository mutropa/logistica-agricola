<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-emerald-100 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl overflow-hidden">
      <!-- Cabeçalho com imagem temática -->
      <div class="relative h-40 bg-gradient-to-r from-green-600 to-emerald-700">
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="text-center p-4">
            <i class="fas fa-seedling text-5xl text-white opacity-80 mb-2"></i>
            <h1 class="text-2xl font-bold text-white">Cadastre-se no Sidonio Mutropa</h1>
          </div>
        </div>
        <div class="absolute bottom-0 left-0 right-0 h-12 bg-white rounded-t-3xl"></div>
      </div>

      <!-- Formulário -->
      <div class="px-8 py-6">
        <div class="flex justify-center mb-6">
          <div class="flex bg-gray-100 rounded-full p-1">
            <button 
              v-for="(type, index) in userTypes" 
              :key="index"
              @click="selectUserType(type.value)"
              class="px-4 py-2 rounded-full text-sm font-medium transition-all"
              :class="{
                'bg-green-600 text-white shadow': userType === type.value,
                'text-gray-600 hover:bg-gray-200': userType !== type.value
              }"
            >
              <i :class="type.icon" class="mr-1"></i>
              {{ type.label }}
            </button>
          </div>
        </div>

        <form @submit.prevent="register">
          <div class="mb-5">
            <label class="block text-gray-700 mb-2 font-medium">Nome Completo</label>
            <div class="relative">
              <i class="fas fa-user absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
              <input 
                v-model="name"
                type="text" 
                class="w-full pl-12 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                placeholder="Seu nome completo"
                required
              >
            </div>
          </div>
          
          <div class="mb-5">
            <label class="block text-gray-700 mb-2 font-medium">Email</label>
            <div class="relative">
              <i class="fas fa-envelope absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
              <input 
                v-model="email"
                type="email" 
                class="w-full pl-12 pr-4 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                placeholder="seu.email@exemplo.com"
                required
              >
            </div>
          </div>
          
          <div class="mb-5">
            <label class="block text-gray-700 mb-2 font-medium">Senha</label>
            <div class="relative">
              <i class="fas fa-lock absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400"></i>
              <input 
                v-model="password"
                :type="showPassword ? 'text' : 'password'"
                class="w-full pl-12 pr-12 py-3 border border-gray-300 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                placeholder="Crie uma senha segura"
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
            <div class="mt-2 text-xs text-gray-500">
              <p v-if="passwordStrength === 'weak'" class="text-red-500"><i class="fas fa-exclamation-circle mr-1"></i> Senha fraca - tente adicionar mais caracteres</p>
              <p v-if="passwordStrength === 'medium'" class="text-yellow-500"><i class="fas fa-check-circle mr-1"></i> Senha média - você pode melhorar</p>
              <p v-if="passwordStrength === 'strong'" class="text-green-500"><i class="fas fa-check-circle mr-1"></i> Senha forte - ótimo trabalho!</p>
            </div>
          </div>
          
          <div v-if="userType === 'produtor'" class="mb-5">
            <label class="block text-gray-700 mb-2 font-medium">Tipo de Produção</label>
            <div class="grid grid-cols-2 gap-3">
              <button 
                v-for="(crop, index) in crops" 
                :key="index"
                type="button"
                class="py-2 border rounded-xl text-sm flex items-center justify-center"
                :class="{
                  'border-green-500 bg-green-50': selectedCrops.includes(crop),
                  'border-gray-300 hover:bg-gray-50': !selectedCrops.includes(crop)
                }"
                @click="toggleCrop(crop)"
              >
                <i class="fas mr-2" :class="cropIcons[crop]"></i>
                {{ crop }}
              </button>
            </div>
          </div>
          
          <div class="mb-6">
            <label class="flex items-center cursor-pointer">
              <input type="checkbox" v-model="termsAccepted" class="mr-2 h-5 w-5 text-green-600 rounded focus:ring-green-500">
              <span class="text-sm text-gray-700">Concordo com os <a href="#" class="text-green-600 hover:underline">Termos de Serviço</a> e <a href="#" class="text-green-600 hover:underline">Política de Privacidade</a></span>
            </label>
          </div>
          
          <button 
            type="submit" 
            class="w-full bg-gradient-to-r from-green-600 to-emerald-700 text-white py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 font-medium"
            :disabled="loading || !termsAccepted"
            :class="{'opacity-70 cursor-not-allowed': !termsAccepted}"
          >
            <span v-if="!loading">Criar minha conta</span>
            <span v-else class="flex items-center justify-center">
              <i class="fas fa-spinner fa-spin mr-2"></i> Criando conta...
            </span>
          </button>
          
          <div v-if="error" class="mt-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-xl">
            <i class="fas fa-exclamation-circle mr-2"></i> {{ error }}
          </div>
          
          <div v-if="successMessage" class="mt-4 p-3 bg-green-50 border border-green-200 text-green-700 rounded-xl">
            <i class="fas fa-check-circle mr-2"></i> {{ successMessage }}
          </div>
        </form>

        <div class="mt-6 pt-5 border-t border-gray-200 text-center">
          <p class="text-gray-600">
            Já tem uma conta?
            <router-link 
              to="/login" 
              class="text-green-600 font-medium hover:text-green-800 hover:underline"
            >
              Faça login aqui
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const name = ref('')
const email = ref('')
const password = ref('')
const userType = ref('produtor')
const termsAccepted = ref(false)
const showPassword = ref(false)
const loading = ref(false)
const error = ref(null)
const successMessage = ref(null)
const selectedCrops = ref([])

// Tipos de usuário com ícones
const userTypes = [
  { value: 'produtor', label: 'Produtor', icon: 'fas fa-tractor' },
  { value: 'comprador', label: 'Comprador', icon: 'fas fa-shopping-cart' },
  { value: 'transportador', label: 'Transportador', icon: 'fas fa-truck' }
]

// Culturas agrícolas
const crops = [
  'Grãos', 'Frutas', 'Hortaliças', 'Café', 
  'Cana', 'Algodão', 'Pecuária', 'Outros'
]

// Ícones para cada cultura
const cropIcons = {
  'Grãos': 'fa-wheat',
  'Frutas': 'fa-apple-alt',
  'Hortaliças': 'fa-carrot',
  'Café': 'fa-coffee',
  'Cana': 'fa-leaf',
  'Algodão': 'fa-cloud',
  'Pecuária': 'fa-cow',
  'Outros': 'fa-seedling'
}

// Força da senha
const passwordStrength = computed(() => {
  if (password.value.length === 0) return null
  if (password.value.length < 6) return 'weak'
  if (password.value.length < 10) return 'medium'
  return 'strong'
})

// Selecionar tipo de usuário
const selectUserType = (type) => {
  userType.value = type
  selectedCrops.value = []
}

// Alternar seleção de cultura
const toggleCrop = (crop) => {
  if (selectedCrops.value.includes(crop)) {
    selectedCrops.value = selectedCrops.value.filter(c => c !== crop)
  } else {
    selectedCrops.value.push(crop)
  }
}

// Watch para limpar mensagens quando campos mudam
watch([name, email, password], () => {
  error.value = null
  successMessage.value = null
})

const register = async () => {
  error.value = null
  loading.value = true
  successMessage.value = null
  
  try {
    const payload = {
      username: name.value,
      email: email.value,
      password: password.value,
      tipo: userType.value,
      // Incluindo culturas selecionadas se for produtor
      culturas: userType.value === 'produtor' ? selectedCrops.value : []
    }

    const res = await fetch('http://localhost:8000/api/authentication/registo/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    })

    const data = await res.json()

    if (res.ok) {
      successMessage.value = 'Registro realizado com sucesso! Redirecionando...'
      setTimeout(() => {
        router.push('/login')
      }, 2000)
    } else {
      throw new Error(data.message || data.detail || 'Erro no registro. Tente novamente.')
    }
  } catch (err) {
    console.error('Erro no registro:', err)
    error.value = err.message || 'Erro ao tentar registrar. Verifique seus dados e tente novamente.'
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

/* Estilizando a barra de força da senha */
.password-strength {
  height: 5px;
  border-radius: 2.5px;
  margin-top: 5px;
  background-color: #e0e0e0;
  overflow: hidden;
}

.password-strength::before {
  content: '';
  display: block;
  height: 100%;
  border-radius: 2.5px;
  transition: width 0.3s ease;
}
</style>