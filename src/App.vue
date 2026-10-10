<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
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
}
</style>
