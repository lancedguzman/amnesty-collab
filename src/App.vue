<script setup>
import { RouterView, useRoute } from 'vue-router'
import NavBar from './views/components/NavBar.vue'
import Footer from './views/components/Footer.vue'

const route = useRoute()
</script>

<template>
  <div class="app-layout">
    <NavBar />
    <main class="app-content">
      <RouterView />
    </main>
    <!-- Hide footer on both timeline and application pages -->
    <Footer class="footer" v-if="route.path !== '/timeline' && route.path !== '/application'" />
  </div>
</template>

<style>
/* Replacing ByteBounce with Arcade Bit */
@font-face {
  font-family: 'ByteBounce';
  src: url('/public/font/arcade-bit.otf') format('opentype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

/* Replacing Geist Pixel with pixel_st_8px_ru */
@font-face {
  font-family: 'Geist Pixel';
  src: url('/public/font/pixel-st-8px-ru.otf') format('opentype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

body {
  margin: 0;
  background: #092d5d;
  padding: 0;
}

.app-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  min-height: 100dvh;
}

.app-content {
  flex: 1 0 auto;
}

.footer {
  flex-shrink: 0;
  margin-top: auto;
}

</style>
