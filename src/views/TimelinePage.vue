<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const data = ref({
  application_timeline: [
    { date: 'Oct 2026', event: 'Applications Open' },
    { date: 'Nov 2026', event: 'Applications Close' },
  ],
  journey_levels: [
    {
      level: 'Level 1',
      name: 'Online Learning Sessions',
      date_range: 'Nov 2026 - Jan 2027',
      summary: 'Six youth collectives start the journey together through online learning.',
    },
    {
      level: 'Level 2',
      name: 'Youth Ideathon',
      date_range: 'Jan 21-26, 2027',
      summary: 'All 6 finalist groups pitch their final proposals to a panel.',
    },
    {
      level: 'Level 3',
      name: 'Campaign Execution',
      date_range: 'May - July 2027',
      summary: 'Top 3 finalist groups receive seed funding to run their campaigns.',
    },
  ],
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="content-wrapper">
      <h1 class="page-title">Digital Movers Timeline</h1>

      <section class="timeline-section">
        <h2 class="yellow-heading">Application Timeline</h2>
        <table class="pixel-table">
          <tbody>
            <tr v-for="(row, index) in data.application_timeline" :key="index">
              <td class="date-col">{{ row.date }}</td>
              <td>{{ row.event }}</td>
            </tr>
          </tbody>
        </table>
      </section>

      <div class="start-divider">START</div>

      <section class="timeline-section">
        <h2 class="yellow-heading">Digital Movers Journey</h2>
        <div v-for="(level, index) in data.journey_levels" :key="index" class="journey-card">
          <span class="level-label">{{ level.level }}</span>
          <h3>{{ level.name }}</h3>
          <span class="date-range">{{ level.date_range }}</span>
          <p>{{ level.summary }}</p>
        </div>
      </section>
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
  margin: 0;
  text-align: center;
  line-height: 0.8;
}
.yellow-heading {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4vw, 4rem);
  color: #fae11b;
  text-shadow: 0 0 10px #fae11b;
  margin: 2rem 0 1rem 0;
  text-align: center;
  line-height: 0.8;
}
.timeline-section {
  width: 100%;
}
.pixel-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  background: #063c70;
  border: 4px solid #fff;
}
.pixel-table td {
  border: 2px solid #fff;
  padding: 1rem;
  color: #fff;
}
.date-col {
  color: #fae11b !important;
  font-weight: bold;
  width: 30%;
}
.start-divider {
  font-family: 'ByteBounce', sans-serif;
  font-size: 2.5rem;
  color: #fff;
  text-align: center;
  margin: 2rem 0;
  letter-spacing: 0.1em;
  text-shadow: 2px 2px 0 #20a5fb;
}
.journey-card {
  box-sizing: border-box;
  margin-bottom: 2rem;
  padding: 1.5rem;
  border: 4px solid #fff;
  background: #063c70;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
}
.level-label {
  display: inline-block;
  background: #fae11b;
  color: #000;
  padding: 4px 8px;
  font-weight: bold;
  margin-bottom: 0.5rem;
}
.journey-card h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.5rem;
  color: #fff;
}
.date-range {
  display: block;
  color: #20a5fb;
  font-size: 1rem;
  margin-bottom: 1rem;
}
.journey-card p {
  margin: 0;
  line-height: 1.4;
  font-size: 1.125rem;
}
</style>
