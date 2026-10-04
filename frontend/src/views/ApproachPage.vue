<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/api/approach/')
    if (!res.ok) throw new Error(`Request failed: ${res.status}`)
    data.value = await res.json()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="approach-page">
    <p v-if="loading">Loading...</p>
    <p v-else-if="error">Couldn't load content: {{ error }}</p>

    <template v-else>
      <h1>{{ data.title }}</h1>
      <p class="intro">{{ data.intro }}</p>

      <ul class="points">
        <li v-for="(point, index) in data.points" :key="index">
          {{ point }}
        </li>
      </ul>
    </template>
  </div>
</template>

<style scoped>
/* Placeholder styling only. To be replaced by UI/UX.
   Structure/classes below can be restyled freely*/
.approach-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}
.intro {
  margin-bottom: 1.5rem;
}
.points li {
  margin-bottom: 0.75rem;
}
</style>