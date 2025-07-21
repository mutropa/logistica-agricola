<template>
  <div id="map" class="w-full min-h-[240px] h-full rounded-lg shadow-lg"></div>
</template>

<script>
import 'leaflet/dist/leaflet.css';
import { onMounted, nextTick } from 'vue';

export default {
  name: 'MapComponent',
  setup() {
    onMounted(async () => {
      await nextTick();  
      // garante DOM pronto

      // Importar leaflet JS e CSS
      const L = (await import('leaflet')).default;
      // Import CSS fora do onMounted ou no topo do script (recomendo no topo)
      await import('leaflet/dist/leaflet.css');

      const map = L.map('map', {
        center: [-18.665695, 35.529562],
        zoom: 6,
      });

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
      }).addTo(map);

      const response = await fetch('/assets/moz.json');
      const mozProvinces = await response.json();

      L.geoJSON(mozProvinces, {
        style: {
          fillColor: '#4CAF50',
          weight: 1,
          color: '#264F36',
          fillOpacity: 0.6,
        },
        onEachFeature: (feature, layer) => {
          layer.bindPopup(`<strong>${feature.properties.NAME_1}</strong>`);
        },
      }).addTo(map);
    });
  },
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 100%;
}
</style>
