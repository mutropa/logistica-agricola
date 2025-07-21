import { defineConfig }       from 'astro/config';
import mdx                   from '@astrojs/mdx';
import vue                   from '@astrojs/vue';
import { fileURLToPath, URL } from 'url';

import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  integrations: [
    mdx(),
    vue(),
  ],
  vite: {
    resolve: {
      alias: {
        // faz '@' apontar para a tua pasta src
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },

    plugins: [tailwindcss()],
  },
});