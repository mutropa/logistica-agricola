<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-green-700 text-white p-4">
      <h1>Área do Produtor</h1>
    </header>

    <nav class="bg-green-100 p-2">
      <router-link to="/produtor/dashboard" class="mr-4">Dashboard</router-link>
    </nav>

    <main class="flex-1 p-4">
      <router-view />
    </main>
  </div>
</template>

<script setup>
// Aqui você pode importar dados do usuário logado se desejar
</script>
