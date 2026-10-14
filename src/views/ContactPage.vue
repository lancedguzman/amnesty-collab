<script setup>
import { onMounted, onBeforeUnmount } from 'vue'
import NavBar from './components/NavBar.vue'

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
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="stars-overlay"></div>

    <div class="content-wrapper">
      <!-- Left Side: Header and Box -->
      <div class="left-panel">
        <h1 class="page-title">CONTACT US</h1>

        <div class="contact-box">
          <p>Have questions or need assistance with your application?</p>
        </div>
      </div>

      <!-- Right Side: Traffic Pole and Signs -->
      <div class="right-panel">
        <div class="pole-container">
          <img src="../../media/assets/traffic-pole.png" alt="Traffic Pole" class="traffic-pole" />

          <!-- Sign 1: FAQ Guide -->
          <router-link to="/faqs" class="sign-link sign-faq">
            <img
              src="../../media/assets/empty-sign-right-1.png"
              alt="Sign Background"
              class="sign-bg"
            />
            <span class="sign-text">Applicant FAQ Guide</span>
          </router-link>

          <!-- Sign 2: Email -->
          <a href="mailto:cydphilippines@amnesty.org.ph" class="sign-link sign-email">
            <img
              src="../../media/assets/empty-sign-right-1.png"
              alt="Sign Background"
              class="sign-bg"
            />
            <span class="sign-text small-text">cydphilippines@amnesty.org.ph</span>
          </a>
        </div>
      </div>
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
  padding: 64px clamp(24px, 6vw, 80px);
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
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  width: 100%;
  max-width: 1100px;
  gap: clamp(32px, 5vw, 64px);
  margin-top: 8vh;
}

/* LEFT PANEL */
.left-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 32px;
  max-width: 500px;
}

.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4.5vw, 4.5rem);
  color: #fff;
  margin: 0;
  text-align: left;
  line-height: 1.1;
  letter-spacing: 12px;
  word-spacing: 16px;
}

.contact-box {
  background: rgba(14, 38, 86, 0.8);
  border-radius: 16px;
  border: 2px solid #1a4a8c;
  padding: clamp(24px, 4vw, 32px);
  box-shadow: 0 0 30px rgba(32, 165, 251, 0.2);
  width: 100%;
}

.contact-box p {
  font-size: clamp(1.1rem, 2vw, 1.4rem);
  line-height: 1.6;
  margin: 0;
  color: #d0e5ff;
}

/* RIGHT PANEL */
.right-panel {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.pole-container {
  position: relative;
  display: inline-block;
  max-height: 75vh;
  margin-top: -3vh;
}

.traffic-pole {
  height: 75vh;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
}

/* SIGNS */
.sign-link {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  width: clamp(200px, 28vh, 300px);
  text-decoration: none;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
}

/* Adjusted placement to align the first sign properly with the crossbar */
.sign-faq {
  top: 12%;
  left: 47%;
  transform: rotate(4deg);
}

.sign-email {
  top: 31%;
  left: 46%;
  transform: rotate(4deg);
}

.sign-link:hover {
  filter: drop-shadow(0px 0px 15px rgba(250, 225, 27, 0.8));
  transform: scale(1.05);
  z-index: 2;
}

.sign-bg {
  width: 100%;
  height: auto;
  display: block;
}

.sign-text {
  position: absolute;
  top: 48%;
  left: 47%;
  transform: translate(-50%, -50%) rotate(-16deg);
  width: 85%;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  /* Scaled down to fit one line */
  font-size: clamp(1rem, 2.4vw, 1.5rem);
  text-align: center;
  font-weight: bold;
  line-height: 1.4;
  white-space: nowrap; /* Forces text to stay on a single line */
  text-shadow: 2px 2px 0px #092d5d;
}

.small-text {
  /* Scaled down further to fit the longer email address */
  font-size: clamp(1rem, 1.1vh, 0.9rem);
}

/* RESPONSIVE LAYOUT */
@media (max-width: 860px) {
  .content-wrapper {
    flex-direction: column;
    margin-top: 2vh;
  }

  .left-panel {
    align-items: center;
    text-align: center;
  }

  .page-title {
    text-align: center;
  }

  .contact-box {
    text-align: center;
  }

  .pole-container {
    margin-top: 24px;
    max-height: 60vh;
  }

  .traffic-pole {
    height: 60vh;
  }
}
</style>
