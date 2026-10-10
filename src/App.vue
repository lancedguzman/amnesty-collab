<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <RouterView />
</template>

<style>
@font-face {
  font-family: 'ByteBounce';
  /* Fixed path: Removed one level of traversal so it doesn't escape the project root */
  src: url('../../media/fonts/ByteBounce.ttf') format('truetype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

@font-face {
  font-family: 'Geist Pixel';
  /* Fixed path: Removed one level of traversal so it doesn't escape the project root */
  src: url('../../media/fonts/GeistPixel-Regular-VariableFont_ELSH.ttf') format('truetype');
  font-style: normal;
  font-weight: 400;
  font-display: swap;
}

body {
  margin: 0;
}
</style>
