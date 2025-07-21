<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-blue-700 text-white p-4">
      <h1>Área do Comprador</h1>
    </header>

    <nav class="bg-blue-100 p-2">
      <router-link to="/comprador/dashboard" class="mr-4">Dashboard</router-link>
    </nav>

    <main class="flex-1 p-4">
      <router-view />
    </main>
  </div>
</template>
