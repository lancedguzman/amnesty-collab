<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import NavBar from './components/NavBar.vue'

const revealObserver =
  typeof IntersectionObserver !== 'undefined'
    ? new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add('is-visible')
              revealObserver.unobserve(entry.target)
            }
          })
        },
        { threshold: 0.15 },
      )
    : null

const vReveal = {
  mounted(el) {
    if (revealObserver) revealObserver.observe(el)
    else el.classList.add('is-visible')
  },
}

const getImageUrl = (filename) => {
  return new URL(`../../media/assets/${filename}`, import.meta.url).href
}

const data = ref({
  application_timeline: [
    { date: 'Oct. 26, 2026', event: 'Applications Open' },
    { date: 'Nov. 14, 2026', event: 'Virtual Info Session' },
    { date: 'Nov. 20, 2026', event: 'Applications Close' },
    { date: 'Nov. 4-25, 2026', event: 'Interview with shortlisted groups' },
    { date: 'Nov. 27, 2026', event: 'Finalizing of Top 6 groups' },
    { date: 'Dec. 1, 2026', event: 'Announcement of Top 6 groups' },
  ],
  journey_levels: [
    {
      level: 'LEVEL ONE',
      name: 'ONLINE LEARNING SERIES',
      summary:
        'Welcome gathering, campaign essentials, Theory of Change (TOC) drafting, and self-paced modules on Amnesty Academy.',
      chibi: 'chibi-blue.png',
      chibiClass: 'chibi-right',
      platform: 'light-blue-cloud.png',
      platformHue: '0deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0000.png',
    },
    {
      level: 'LEVEL TWO',
      name: 'NATIONAL YOUTH IDEATHON',
      summary:
        'A 6-day in-person workshop in the Philippines covering creative activism, module design, safeguarding, and final project and budget pitching.',
      chibi: null,
      platform: 'dark-blue-cloud.png',
      platformHue: '0deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0001.png',
    },
    {
      level: 'LEVEL THREE',
      name: 'MENTORSHIP & PROJECT DEVELOPMENT',
      summary:
        'Monthly virtual coaching to complete mandatory campaign deliverables: MEL framework and Risk Mitigation Plan (Feb-Mar), Communications Plan and Branding Kit (Mar), Work Plan, and Budget Requests Plan (Apr).',
      chibi: 'chibi-pink.png',
      chibiClass: 'chibi-right',
      platform: 'dark-blue-cloud.png',
      platformHue: '280deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0002.png',
    },
    {
      level: 'LEVEL FOUR',
      name: 'CAMPAIGN ROLLOUT',
      summary: 'Implementation of your 3-month youth-led campaign or HRE initiative.',
      chibi: 'chibi-green.png',
      chibiClass: 'chibi-left',
      platform: 'dark-blue-cloud.png',
      platformHue: '320deg',
      arrow: 'Copy of DIgital Movers Project Timeline _20260930_070215_0003.png',
    },
    {
      level: 'LEVEL FIVE',
      name: 'GRADUATION & RETREAT',
      summary:
        'Reflection on collective growth, impact evaluation, project sustainability planning, and celebration.',
      chibi: 'trophy.png',
      chibiClass: 'trophy-center',
      platform: 'orange-cloud.png',
      platformHue: '0deg',
      arrow: null,
    },
  ],
})

let target = 0
let current = 0
let stretchSmooth = 0
let raf

const onScroll = () => {
  target = window.scrollY
}

const loop = () => {
  current += (target - current) * 0.035

  const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight)
  const progress = Math.min(1, Math.max(0, current / maxScroll))

  const velocity = target - current
  const stretchTarget = Math.min(0.05, Math.abs(velocity) * 0.0005)
  stretchSmooth += (stretchTarget - stretchSmooth) * 0.06

  const root = document.documentElement.style
  root.setProperty('--bg-y', `${-progress * window.innerHeight * 0.2}px`)
  root.setProperty('--bg-x', `${-progress * window.innerWidth * 0.08}px`)
  root.setProperty('--bg-stretch', 1 + stretchSmooth)

  raf = requestAnimationFrame(loop)
}

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
  current = target
  loop()
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
  cancelAnimationFrame(raf)
  revealObserver?.disconnect()
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="stars-overlay"></div>
    <div class="content-wrapper">
      <div class="header-logos">
        <img
          src="../../media/assets/amnesty-logo.png"
          alt="Amnesty International"
          class="dm-logo amnesty-size"
        />
        <img
          src="../../media/assets/digital-mover-logo.png"
          alt="Digital Movers"
          class="dm-logo dm-size"
        />
      </div>

      <section class="app-timeline-box reveal" v-reveal>
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

      <div class="start-section">
        <img
          src="../../media/assets/start-header.png"
          alt="Start Platform"
          class="start-header-img"
        />
        <div class="platform-container divider-wall">
          <img
            class="level-platform"
            src="../../media/assets/DIgital Movers Project Timeline _20260929_231005_0000.png"
            alt="Cloud Platform"
          />
        </div>
      </div>

      <div class="journey-header reveal" v-reveal>
        <h2>DIGITAL MOVERS JOURNEY</h2>
        <p class="journey-dates">NOV 2026 - AUG 2027</p>
      </div>

      <section class="timeline-levels">
        <div v-for="(level, index) in data.journey_levels" :key="index" class="level-block">
          <div class="level-content reveal" v-reveal>
            <span class="level-label">{{ level.level }}</span>
            <h3 class="level-name">{{ level.name }}</h3>
            <p class="level-desc">{{ level.summary }}</p>
          </div>

          <div class="platform-container reveal" v-reveal>
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

          <img
            v-if="level.arrow"
            :src="getImageUrl(level.arrow)"
            class="path-arrow reveal"
            v-reveal
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
  padding: 40px clamp(12px, 3vw, 48px) 80px;
  overflow: hidden;
  font-family: 'Geist Pixel', sans-serif;
}

.stars-overlay {
  position: fixed;
  inset: -25vh -12vw;
  background-image:
    radial-gradient(1px 1px at 10% 10%, white 100%, transparent),
    radial-gradient(1px 1px at 30% 50%, white 100%, transparent),
    radial-gradient(2px 2px at 80% 20%, white 100%, transparent),
    radial-gradient(1px 1px at 60% 80%, white 100%, transparent);
  background-size: 200px 200px;
  opacity: 0.5;
  pointer-events: none;
  z-index: 0;
  transform: translate3d(var(--bg-x, 0px), var(--bg-y, 0px), 0) scaleY(var(--bg-stretch, 1));
  will-change: transform;
}

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1200px;
}

.header-logos {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  margin-bottom: clamp(24px, 4vw, 48px);
}

.dm-logo {
  width: auto;
  max-width: 100%;
  object-fit: contain;
  filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.5));
}

.amnesty-size {
  height: clamp(40px, 12vw, 70px);
}

.dm-size {
  height: clamp(140px, 45vw, 360px);
}

.app-timeline-box {
  width: 100%;
  max-width: 900px;
  background: rgba(14, 38, 86, 0.8);
  border-radius: 16px;
  border: 2px solid #1a4a8c;
  padding: clamp(16px, 3vw, 36px);
  margin-bottom: clamp(16px, 3vw, 40px);
  box-shadow: 0 0 30px rgba(32, 165, 251, 0.2);
}

.box-title {
  text-align: center;
  font-size: clamp(1.25rem, 2.6vw, 2.25rem);
  letter-spacing: 2px;
  margin-bottom: 15px;
}

.pixel-table {
  width: 100%;
  border-collapse: collapse;
  font-size: clamp(1rem, 1.9vw, 1.6rem);
}

.pixel-table td {
  padding: clamp(8px, 1.4vw, 16px);
  border-bottom: 1px solid #1a4a8c;
}

.date-col {
  width: 38%;
  color: #fae11b;
  font-weight: bold;
}

.start-section {
  width: 100%;
  text-align: center;
  margin-bottom: 10px;
}

.start-header-img {
  display: block;
  width: min(60%, 600px);
  height: auto;
  margin: 0 auto;
  mix-blend-mode: screen;
}

.journey-header {
  text-align: center;
  margin: clamp(16px, 3vw, 40px) 0 clamp(16px, 3vw, 32px);
}

.journey-header h2 {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(1.5rem, 4vw, 3.25rem);
  margin: 0;
  text-shadow: 2px 2px 0 #20a5fb;
}

.journey-dates {
  color: #fae11b;
  font-size: clamp(1.4rem, 3vw, 2.6rem);
  margin-top: 5px;
}

.timeline-levels {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
}

.level-block {
  --cloud-pull: -32%;
  text-align: center;
  width: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.level-block:nth-child(even) {
  align-items: flex-end;
}

.level-content {
  position: relative;
  z-index: 3;
}

.level-content,
.platform-container {
  width: 62%;
  max-width: none;
  margin: 0;
}

.level-label {
  color: #20a5fb;
  font-size: clamp(1.1rem, 2vw, 1.75rem);
  letter-spacing: 2px;
}

.level-name {
  font-size: clamp(1.5rem, 3.6vw, 3.25rem);
  margin: 8px 0;
  text-transform: uppercase;
}

.level-desc {
  font-size: clamp(1.2rem, 2.2vw, 1.9rem);
  line-height: 1.5;
  color: #d0e5ff;
  margin-top: 0;
  margin-bottom: 8px;
  transform: translateY(-12px);
}

.platform-container {
  position: relative;
  display: flex;
  justify-content: center;
  z-index: 2;
  margin-top: var(--cloud-pull);
}

.platform-container.divider-wall {
  width: 85%;
  margin-left: auto;
  margin-right: auto;
}

.level-platform {
  width: 100%;
  height: auto;
  mix-blend-mode: screen;
}

.chibi-img {
  position: absolute;
  width: clamp(56px, 12vw, 170px);
  bottom: 40%;
  transform: scaleX(-1);
}

.chibi-right {
  right: -20%;
}

.chibi-left {
  left: -20%;
}

.trophy-center {
  width: clamp(50px, 10vw, 140px);
  bottom: 52%;
  left: 40%;
  mix-blend-mode: screen;
}

.path-arrow {
  width: clamp(200px, 40vw, 480px);
  margin: -45% 0 -12%;
  mix-blend-mode: screen;
  opacity: 0.8;
  z-index: 1;
}

.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition:
    opacity 0.8s ease,
    transform 0.8s ease;
}

.reveal.is-visible {
  opacity: 1;
  transform: none;
}

.platform-container.reveal {
  transition-delay: 0.15s;
}

.path-arrow.reveal.is-visible {
  opacity: 0.8;
}

@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }

  .path-arrow.reveal {
    opacity: 0.8;
  }
}

@media (max-width: 600px) {
  .level-block {
    --cloud-pull: -40%;
  }

  .level-content,
  .platform-container {
    width: 82%;
  }

  .app-timeline-box {
    width: 88%;
  }
}
</style>
