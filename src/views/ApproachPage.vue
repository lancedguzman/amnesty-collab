<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const data = ref({
  title: 'Our Approach',
  intro:
    'Enter the introduction to your approach here. This text replaces the content that was previously fetched from the database.',
  points: [
    'First key point of your approach.',
    'Second key point of your approach.',
    'Third key point of your approach.',
  ],
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="content-wrapper">
      <h1 class="page-title">{{ data.title }}</h1>
      <p class="intro-text">{{ data.intro }}</p>

      <ul class="points-list">
        <li v-for="(point, index) in data.points" :key="index">
          {{ point }}
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.page-container {
  box-sizing: border-box;
  min-height: calc(100vh - 76px);
  display: flex;
  justify-content: center;
  padding: 64px clamp(24px, 6vw, 80px);
  background: #092d5d;
  color: #fff;
}
.content-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  width: min(100%, 800px);
}
.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(4rem, 4.5vw, 5rem);
  color: #fff;
  text-shadow: 3px 4px 0 #20a5fb;
  margin: 0 0 1rem 0;
  text-align: center;
  line-height: 0.8;
}
.intro-text,
.points-list li {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  line-height: 1.4;
  color: #fff;
  text-align: center;
}
.points-list {
  text-align: left;
  margin-top: 1.5rem;
  padding-left: 1.5rem;
}
.points-list li {
  text-align: left;
  margin-bottom: 1rem;
}
</style>
