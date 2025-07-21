import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueLazyLoad from 'vue3-lazyload'
import '@fortawesome/fontawesome-free/css/all.css'


// Criação da instância principal da aplicação Vue
const app = createApp(App)

// Registro do Vue Router
app.use(router)

// Configuração do Vue LazyLoad com imagens personalizadas
app.use(VueLazyLoad, {
  loading: '/assets/loading.jpg', // Imagem exibida durante o carregamento
  error: '/assets/error.jpg'      // Imagem exibida em caso de erro
})

// Montagem da aplicação no elemento com id "app"
// Isso deve ser feito por último
app.mount('#vue-app')
