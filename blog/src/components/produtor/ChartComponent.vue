<!-- ChartComponent.vue -->
<template>
  <div class="h-64">
    <Line :data="lineData" :options="lineOptions" />
  </div>
</template>

<script setup>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
)

const lineData = {
  labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
  datasets: [
    {
      label: 'Produção (kg)',
      backgroundColor: '#34D399',
      borderColor: '#10B981',
      data: [120, 190, 300, 500, 200, 300],
      fill: false,
      tension: 0.4
    }
  ]
}

const lineOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
    title: { display: true, text: 'Desempenho Mensal' }
  }
}
</script>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
}
</style>
