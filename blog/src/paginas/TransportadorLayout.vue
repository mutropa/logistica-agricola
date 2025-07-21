<template>
  <div class="min-h-screen flex flex-col">
    <header class="bg-yellow-600 text-white p-4">
      <h1>Área do Transportador</h1>
    </header>

    <nav class="bg-yellow-100 p-2">
      <router-link to="/transportador/dashboard" class="mr-4">Dashboard</router-link>
    </nav>

    <main class="flex-1 p-4">
      <router-view />
    </main>
  </div>
</template>
