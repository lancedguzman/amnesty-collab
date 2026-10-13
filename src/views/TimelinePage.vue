<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

// Helper function to resolve dynamic image paths in Vite
const getImageUrl = (filename) => {
  return new URL(`../../media/assets/${filename}`, import.meta.url).href
}

const data = ref({
  application_timeline: [
    { date: 'Oct 2026', event: 'Applications Open' },
    { date: 'Nov 2026', event: 'Applications Close' },
  ],
  journey_levels: [
    {
      level: 'LEVEL ONE',
      name: 'ONLINE LEARNING SERIES',
      summary:
        'A series of online learning sessions which aims to provide foundational knowledge and clear application for human rights project proposals.',
      chibi: 'chibi-blue.png',
      chibiClass: 'chibi-right',
      platform: 'dark-blue-cloud.png',
      platformHue: '0deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0000.png',
    },
    {
      level: 'LEVEL TWO',
      name: 'NATIONAL YOUTH IDEATHON',
      summary:
        'A 5-day in-person Ideathon in Metro Manila spanning creative ideation, project design, safeguarding, and final project pitch with panellists.',
      chibi: null,
      platform: 'dark-blue-cloud.png',
      platformHue: '0deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0001.png',
    },
    {
      level: 'LEVEL THREE',
      name: 'MENTORSHIP & PROJECT DEVELOPMENT',
      summary:
        'The top 3 finalist groups to complete overall documentation and receive M&E frameworks and funding! Plus final Q&A around the Plan and beyond, Activity, and Operational/Budget.',
      chibi: 'chibi-pink.png',
      chibiClass: 'chibi-right chibi-pink',
      platform: 'dark-blue-cloud.png',
      platformHue: '280deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0002.png',
    },
    {
      level: 'LEVEL FOUR',
      name: 'CAMPAIGN ROLLOUT',
      summary: 'Implementation of your 3-month youth-led campaign on HRs violations.',
      chibi: 'chibi-green.png', // Moved green chibi to Level 4
      chibiClass: 'chibi-left',
      platform: 'dark-blue-cloud.png',
      platformHue: '320deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0003.png',
    },
    {
      level: 'LEVEL FIVE',
      name: 'GRADUATION & RETREAT',
      summary:
        'Re-evaluation, reflection, grassroots impact evaluation, network & community building, and celebration.',
      chibi: 'trophy.png', // Replaced chibi with trophy[cite: 19]
      chibiClass: 'trophy-center',
      platform: 'orange-cloud.png', // Updated to orange cloud[cite: 17]
      platformHue: '0deg',
      arrow: null,
    },
  ],
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="stars-overlay"></div>
    <div class="content-wrapper">
      <!-- Logos -->
      <div class="header-logos">
        <img
          src="../../media/assets/amnesty-logo.png"
          alt="Amnesty International"
          class="amnesty-logo"
        />
        <!--[cite: 15] -->
        <img src="../../media/assets/digital-mover-logo.png" alt="Digital Movers" class="dm-logo" />
        <!--[cite: 16] -->
      </div>

      <!-- Application Timeline -->
      <section class="app-timeline-box">
        <h2 class="box-title">APPLICATION TIMELINE</h2>
        <table class="pixel-table">
          <tbody>
            <tr v-for="(row, index) in data.application_timeline" :key="index">
              <td class="date-col">{{ row.date }}</td>
              <td>{{ row.event }}</td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- Start Section -->
      <div class="start-section">
        <img
          src="../../media/assets/start-header.png"
          alt="Start Platform"
          class="start-header-img"
        />
        <!--[cite: 18] -->
      </div>

      <div class="journey-header">
        <h2>DIGITAL MOVERS JOURNEY</h2>
        <p class="journey-dates">NOV 2026 - AUG 2027</p>
      </div>

      <!-- Journey Levels -->
      <section class="timeline-levels">
        <div v-for="(level, index) in data.journey_levels" :key="index" class="level-block">
          <div class="level-content">
            <span class="level-label">{{ level.level }}</span>
            <h3 class="level-name">{{ level.name }}</h3>
            <p class="level-desc">{{ level.summary }}</p>
          </div>

          <div class="platform-container">
            <img
              :src="getImageUrl(level.platform)"
              alt="Cloud Platform"
              class="level-platform"
              :style="{ filter: `hue-rotate(${level.platformHue})` }"
            />
            <img
              v-if="level.chibi"
              :src="getImageUrl(level.chibi)"
              alt="Character or Trophy"
              :class="['chibi-img', level.chibiClass]"
            />
          </div>

          <!-- Image-based connector arrow -->
          <img
            v-if="level.arrow"
            :src="getImageUrl(level.arrow)"
            class="path-arrow"
            alt="Path Arrow"
          />
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.page-container {
  box-sizing: border-box;
  min-height: calc(100vh - 76px);
  position: relative;
  background: #0b1a40;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 20px;
  overflow: hidden;
  font-family: 'Geist Pixel', sans-serif;
}

.stars-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image:
    radial-gradient(1px 1px at 10% 10%, white 100%, transparent),
    radial-gradient(1px 1px at 30% 50%, white 100%, transparent),
    radial-gradient(2px 2px at 80% 20%, white 100%, transparent),
    radial-gradient(1px 1px at 60% 80%, white 100%, transparent);
  background-size: 200px 200px;
  opacity: 0.5;
  pointer-events: none;
}

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 800px;
}

.header-logos {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  margin-bottom: 30px;
}

.amnesty-logo {
  height: 40px;
  filter: brightness(0) invert(1);
}

.dm-logo {
  height: 100px;
  filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.5));
}

.app-timeline-box {
  width: 90%;
  max-width: 500px;
  background: rgba(14, 38, 86, 0.8);
  border-radius: 16px;
  border: 2px solid #1a4a8c;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 30px rgba(32, 165, 251, 0.2);
}

.box-title {
  text-align: center;
  font-size: 1.1rem;
  letter-spacing: 2px;
  margin-bottom: 15px;
}

.pixel-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.pixel-table td {
  padding: 8px;
  border-bottom: 1px solid #1a4a8c;
}

.date-col {
  color: #fae11b;
  font-weight: bold;
}

.start-section {
  text-align: center;
  margin-bottom: 10px;
}

.start-header-img {
  width: 250px;
  mix-blend-mode: screen;
}

.journey-header {
  text-align: center;
  margin-bottom: 20px;
}

.journey-header h2 {
  font-family: 'ByteBounce', sans-serif;
  font-size: 2.5rem;
  margin: 0;
  text-shadow: 2px 2px 0 #20a5fb;
}

.journey-dates {
  color: #fae11b;
  font-size: 1rem;
  margin-top: 5px;
}

.timeline-levels {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0; /* Minimized gap for compactness */
}

.level-block {
  text-align: center;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.level-content {
  max-width: 400px;
  margin: 0 auto;
  z-index: 2;
}

.level-label {
  color: #20a5fb;
  font-size: 0.9rem;
  letter-spacing: 2px;
}

.level-name {
  font-size: 1.2rem;
  margin: 5px 0;
  text-transform: uppercase;
}

.level-desc {
  font-size: 0.85rem;
  line-height: 1.4;
  color: #d0e5ff;
  margin-bottom: 5px;
}

.platform-container {
  position: relative;
  display: flex;
  justify-content: center;
  z-index: 2;
}

.level-platform {
  width: 220px;
  /* Blend out black backgrounds on the jpgs */
  mix-blend-mode: screen;
}

.chibi-img {
  position: absolute;
  width: 80px;
  bottom: 20px;
}

.chibi-right {
  right: -50px;
}

.chibi-left {
  left: -50px;
}

.trophy-center {
  width: 70px;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  mix-blend-mode: screen;
}

.path-arrow {
  width: 150px;
  margin: -15px 0 -15px 0; /* Negative margins to compact the layout */
  mix-blend-mode: screen;
  opacity: 0.8;
  z-index: 1;
}

@media (max-width: 768px) {
  .journey-header h2 {
    font-size: 2rem;
  }

  .level-platform {
    width: 180px;
  }

  .chibi-img {
    width: 60px;
  }

  /* Pull characters inward to prevent horizontal overflow */
  .chibi-right {
    right: -10px;
  }

  .chibi-left {
    left: -10px;
  }

  .trophy-center {
    width: 50px;
    bottom: 30px;
  }

  .path-arrow {
    width: 100px;
  }
}
</style>
