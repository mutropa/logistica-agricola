<script setup>
import App from './App.vue'
import { createApp } from 'vue'
import router from '../router'

const mount = () => {
  const app = createApp(App)
  app.use(router)
  app.mount('#vue-app')
}

onMounted(mount)
</script>

<template>
  <div id="vue-app"></div>
</template>
