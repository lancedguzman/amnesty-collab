<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const data = ref({
  title: 'Our Approach: Revolutionizing Youth Engagement in the Philippines',
  intro:
    'Young people want real decision-making power, not tokenistic participation! We’re not interested in creating mini-adults. Rather, we support genuine youth-led and youth-owned initiatives that challenge dominant narratives with creative, accessible, and hopeful messages. You’ll enjoy working with us if you want to:',
  points: [
    'Shift from participation to shared power, ensuring children and youth influence decision-making processes.',
    'Build safe and enabling environments with strong safeguarding protocols, particularly for children and youth.',
    'Develop age-appropriate engagement approaches tailored specifically to children and youth.',
    'Counter harmful narratives by promoting children and young people’s rights, agency, and participation.',
    'Integrate well-being and resilience into engagement strategies.',
    'Localize approaches to reflect diverse contexts and lived realities.',
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
  width: min(100%, 900px);
}
.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  color: #fff;
  text-shadow: 2px 3px 0 #20a5fb;
  margin: 0 0 1rem 0;
  text-align: center;
  line-height: 1.1;
}
.intro-text,
.points-list li {
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1.25rem, 1.5vw, 1.5rem);
  line-height: 1.6;
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
  margin-bottom: 1.25rem;
}
</style>
