<script setup>
import { ref, onMounted } from 'vue'

const data = ref(null)
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/api/timeline/')
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
  <div class="timeline-page">
    <p v-if="loading">Loading...</p>
    <p v-else-if="error">Couldn't load content: {{ error }}</p>

    <template v-else>
      <section class="application-timeline">
        <h2>Application Timeline</h2>
        <table>
          <tbody>
            <tr v-for="(row, index) in data.application_timeline" :key="index">
              <td>{{ row.date }}</td>
              <td>{{ row.event }}</td>
            </tr>
          </tbody>
        </table>
      </section>

      <div class="start-divider">START</div>

      <section class="journey">
        <h2>Digital Movers Journey</h2>
        <div
          v-for="(level, index) in data.journey_levels"
          :key="index"
          class="journey-level"
        >
          <span class="level-label">{{ level.level }}</span>
          <h3>{{ level.name }}</h3>
          <span class="date-range">{{ level.date_range }}</span>
          <p>{{ level.summary }}</p>
        </div>
      </section>
    </template>
  </div>
</template>

<style scoped>
/* Placeholder styling only. To be replaced by UI/UX.
   Structure/classes below can be restyled freely*/
.timeline-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}
.application-timeline table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}
.application-timeline td {
  border: 1px solid #ccc;
  padding: 0.5rem 1rem;
}
.start-divider {
  text-align: center;
  font-weight: bold;
  margin: 3rem 0;
  letter-spacing: 0.2em;
}
.journey-level {
  margin-bottom: 3rem;
}
.level-label {
  color: #4285F4;
  font-size: 0.85rem;
  text-transform: uppercase;
}
.date-range {
  display: block;
  color: #777;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}
</style>