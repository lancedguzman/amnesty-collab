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
  src: url('../../media/font/arcade-bit.otf') format('truetype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

/* Replacing Geist Pixel with pixel_st_8px_ru */
@font-face {
  font-family: 'Geist Pixel';
  src: url('../../media/font/pixel_st_8px_ru.off') format('truetype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

body {
  margin: 0;
  background: #092d5d;
}
</style>
