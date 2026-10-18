<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'
import NavBar from './components/NavBar.vue'
import confetti from 'canvas-confetti'
import bubbleEquity from '../../media/assets/bubble-equity.png'
import bubbleStratigic from '../../media/assets/bubble-stratigic.png'
import bubbleYouth from '../../media/assets/bubble-youth.png'
import bubbleOpenness from '../../media/assets/bubble-openness.png'
import bubbleCreative from '../../media/assets/bubble-creative.png'

const bubbleImages = {
  equity: bubbleEquity,
  stratigic: bubbleStratigic,
  youth: bubbleYouth,
  openness: bubbleOpenness,
  creative: bubbleCreative,
}

const asset = (name) => new URL(`../../media/assets/${name}`, import.meta.url).href

const altTexts = [
  'Youth-Led: A Filipino group, organization, or collective whose members are primarily 25 years old and below',
  'Defined Organizational Structure: consistent membership and leadership setup',
  'Dedicated Project Team: can delegate 3 to 5 young leaders (aged 15-24)',
  'Proven Experience: proven track record of running local projects or campaigns',
  "Focus Areas: human rights, digital rights, children's rights, indigenous people's rights, climate justice, anti-discrimination and inclusion, sexual and reproductive health and rights",
  'Philippines-based',
]
const cards = altTexts.map((alt, i) => ({ src: asset(`attribute-${i + 1}.png`), alt }))

const index = ref(0)
const perView = ref(3)

const updateView = () => {
  perView.value = window.innerWidth < 768 ? 1 : window.innerWidth < 1024 ? 2 : 3
  index.value = Math.min(index.value, Math.max(0, cards.length - perView.value))
}
const next = () => {
  if (index.value < cards.length - perView.value) index.value++
}
const prev = () => {
  if (index.value > 0) index.value--
}

let startX = 0
const onTouchStart = (e) => {
  startX = e.touches[0].clientX
}
const onTouchEnd = (e) => {
  const dx = e.changedTouches[0].clientX - startX
  if (Math.abs(dx) > 40) dx < 0 ? next() : prev()
}

onMounted(() => {
  updateView()
  window.addEventListener('resize', updateView)

  if (!localStorage.getItem('hasVisitedLandingPage')) {
    confetti({
      particleCount: 150,
      spread: 80,
      origin: { y: 0.6 },
      colors: ['#ffdf01', '#9addf7', '#092d5d', '#ffffff'],
    })
    localStorage.setItem('hasVisitedLandingPage', 'true')
  }

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  window.addEventListener('scroll', updateScrollTarget, { passive: true })
  updateScrollTarget()
  scrollCurrent = scrollTarget
  animateStars()
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', updateScrollTarget)
  cancelAnimationFrame(animationFrame)
  document.documentElement.style.removeProperty('--bg-x')
  document.documentElement.style.removeProperty('--bg-y')
  document.documentElement.style.removeProperty('--bg-stretch')
})

const activeSign = ref(null)

let scrollTarget = 0
let scrollCurrent = 0
let stretchSmooth = 0
let animationFrame

const updateScrollTarget = () => {
  scrollTarget = window.scrollY
}

const animateStars = () => {
  scrollCurrent += (scrollTarget - scrollCurrent) * 0.035

  const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight)
  const progress = Math.min(1, Math.max(0, scrollCurrent / maxScroll))
  const velocity = scrollTarget - scrollCurrent
  const stretchTarget = Math.min(0.05, Math.abs(velocity) * 0.0005)
  stretchSmooth += (stretchTarget - stretchSmooth) * 0.06

  const rootStyle = document.documentElement.style
  rootStyle.setProperty('--bg-y', `${-progress * window.innerHeight * 0.2}px`)
  rootStyle.setProperty('--bg-x', `${-progress * window.innerWidth * 0.08}px`)
  rootStyle.setProperty('--bg-stretch', 1 + stretchSmooth)

  animationFrame = requestAnimationFrame(animateStars)
}

function activate(sign) {
  activeSign.value = activeSign.value === sign ? null : sign
}
</script>

<template>
  <NavBar />

  <div class="scrolling-container">
    <div class="section-panel section1">
      <div class="stars-overlay"></div>
      <img class="hero-skyline" src="../../media/assets/bg-skyscrapers.png" alt="" />
      <div class="content-wrapper">
        <div id="left-align">
          <div id="landing-heading">
            <div id="landing-heading1">let's make the</div>
            <div id="landing-heading2" data-text="MOVE">MOVE</div>
          </div>
          <div id="landing-description">
            An Amnesty International Philippines Capacity-building and Seed Funding Program for
            Youth Organizations
          </div>
          <RouterLink to="/application" id="apply-button">APPLY NOW!</RouterLink>
        </div>

        <div id="right-align">
          <img
            src="../../media/assets/digital-movers-poster.png"
            alt="Digital Movers Poster"
            class="hero-poster"
          />
        </div>
      </div>
    </div>

    <div class="section-panel section2">
      <img class="s2-cloud s2-cloud-1" src="../../media/assets/cloud-1.png" alt="" />
      <img class="s2-cloud s2-cloud-2" src="../../media/assets/cloud-2.png" alt="" />
      <img class="s2-cloud s2-cloud-3" src="../../media/assets/cloud-3.png" alt="" />
      <img
        class="s2-arrow s2-arrow-2"
        src="../../media/assets/Copy of DIgital Movers Project Timeline _20260930_070215_0000.png"
        alt=""
      />
      <img
        class="s2-arrow s2-arrow-1"
        src="../../media/assets/Copy of DIgital Movers Project Timeline _20260930_070215_0001.png"
        alt=""
      />
      <div class="content-wrapper">
        <img
          class="s2-logo"
          src="../../media/assets/logo-digital movers.png"
          alt="Digital Movers"
        />
        <img
          class="s2-search"
          src="../../media/assets/textbox-search.png"
          alt="What is Digital Movers?"
        />
      </div>
      <img
        class="s2-windows"
        src="../../media/assets/group1.png"
        alt="Digital Movers is a capacity-building and seed funding program by Amnesty International Philippines (AIPH). We support Filipino youth-led groups and grassroots collectives to launch creative Human Rights Education (HRE) or campaign initiatives. Six youth collectives will start the journey together through online learning and a fully-funded national youth hackathon (Nov 2026 - Jan 2027). Following a pitch showcase at the youth hackathon, the Top 3 finalist groups will receive seed funding and mentorship to run their campaigns through August 2027."
      />
    </div>

    <div class="section-panel section3">
      <img class="s3-cloud s3-cloud-1" src="../../media/assets/cloud-1.png" alt="" />
      <img class="s3-cloud s3-cloud-2" src="../../media/assets/cloud-2.png" alt="" />

      <div class="content-wrapper bottom-padding">
        <div class="header">
          <div class="heading text-yellow">What We Look For</div>
          <div class="s3-desc">
            Digital Movers supports youth-led groups with new or ongoing campaign ideas that need
            financial resourcing and capacity building
          </div>
        </div>

        <div class="carousel">
          <button class="c-arrow" :disabled="index === 0" @click="prev" aria-label="Previous">
            <img src="../../media/assets/arrow2.png" alt="" />
          </button>

          <div class="c-viewport" @touchstart.passive="onTouchStart" @touchend.passive="onTouchEnd">
            <div class="c-track" :style="{ transform: `translateX(-${index * (100 / perView)}%)` }">
              <div
                class="c-slide"
                v-for="(c, i) in cards"
                :key="i"
                :style="{ flexBasis: 100 / perView + '%' }"
              >
                <img :src="c.src" :alt="c.alt" />
              </div>
            </div>
          </div>

          <button
            class="c-arrow"
            :disabled="index >= cards.length - perView"
            @click="next"
            aria-label="Next"
          >
            <img src="../../media/assets/arrow1.png" alt="" />
          </button>
        </div>

        <div class="s3-grass"></div>
      </div>

      <div class="content-wrapper bottom-padding">
        <div class="heading text-yellow mt-large">Selection Criteria</div>
        <div class="selection-cards">
          <div class="items pixel-corners white-box">
            <div class="top light-blue-box subheader-dark">Equity & Inclusion</div>
            <div class="bottom">
              Priority is given to under-resourced and under-represented youth collectives
            </div>
          </div>
          <div class="items pixel-corners white-box">
            <div class="top light-blue-box subheader-dark">Strategic Issue Alignment</div>
            <div class="bottom">
              A clear, feasible campaign plan aligned with human rights focus areas
            </div>
          </div>
          <div class="items pixel-corners white-box">
            <div class="top light-blue-box subheader-dark">Youth Ownership & Team Dynamic</div>
            <div class="bottom">
              Truly youth-led with a stable, committed core membership that cares for its community
            </div>
          </div>
          <div class="items pixel-corners white-box">
            <div class="top light-blue-box subheader-dark">Openness To Learn</div>
            <div class="bottom">Willingness to engage fully in a 9-month journey</div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-panel section4">
      <img class="s4-cloud s4-cloud-1" src="../../media/assets/cloud-2.png" alt="" />
      <img class="s4-cloud s4-cloud-2" src="../../media/assets/cloud-1.png" alt="" />
      <img
        class="s4-buildings"
        src="../../media/assets/Selection 2026-09-09T12.11.02_20260917_192645_0000 1.png"
        alt=""
      />
      <img class="s4-chibi" src="../../media/assets/chibi-pink-floating.png" alt="" />

      <div class="content-wrapper">
        <img
          class="s4-title"
          src="../../media/assets/accessibility-title.png"
          alt="Accessibility & Inclusion"
        />
        <p class="s4-desc"></p>
        <div class="selection-criteria">
          <div class="stars-overlay"></div>

          <div class="left-align">
            <div class="heading text-yellow">Selection Criteria</div>
            <img
              v-if="activeSign"
              class="selection-bubble"
              :src="bubbleImages[activeSign]"
              alt="Selected criterion details"
            />

            <img
              src="../../media/assets/chibi-blue-motivated.png"
              class="chibi-blue-motivated"
              alt=""
            />

            <img src="../../media/assets/trophy.png" class="trophy" alt="" />
          </div>
          <div class="right-align">
            <div class="pole-container">
              <img src="../../media/assets/traffic-pole.png" class="traffic-pole" alt="" />
              <div class="left-buttons">
                <button
                  class="sign-button equity"
                  :class="{ 'is-active': activeSign === 'equity' }"
                  @click="activate('equity')"
                >
                  <img src="../../media/assets/sign-equity.png" class="base-img" />
                  <img src="../../media/assets/sign-equity-hover.png" class="hover-img" />
                  <img src="../../media/assets/sign-equity-active.png" class="active-img" />
                </button>

                <button
                  class="sign-button stratigic"
                  :class="{ 'is-active': activeSign === 'stratigic' }"
                  @click="activate('stratigic')"
                >
                  <img src="../../media/assets/sign-stratigic.png" class="base-img" />
                  <img src="../../media/assets/sign-stratigic-hover.png" class="hover-img" />
                  <img src="../../media/assets/sign-stratigic-active.png" class="active-img" />
                </button>
              </div>

              <div class="right-buttons">
                <button
                  class="sign-button youth"
                  :class="{ 'is-active': activeSign === 'youth' }"
                  @click="activate('youth')"
                >
                  <img src="../../media/assets/sign-youth.png" class="base-img" />
                  <img src="../../media/assets/sign-youth-hover.png" class="hover-img" />
                  <img src="../../media/assets/sign-youth-active.png" class="active-img" />
                </button>

                <button
                  class="sign-button openness"
                  :class="{ 'is-active': activeSign === 'openness' }"
                  @click="activate('openness')"
                >
                  <img src="../../media/assets/sign-openness.png" class="base-img" />
                  <img src="../../media/assets/sign-openness-hover.png" class="hover-img" />
                  <img src="../../media/assets/sign-openness-active.png" class="active-img" />
                </button>

                <button
                  class="sign-button creative"
                  :class="{ 'is-active': activeSign === 'creative' }"
                  @click="activate('creative')"
                >
                  <img src="../../media/assets/sign-creative.png" class="base-img" />
                  <img src="../../media/assets/sign-creative-hover.png" class="hover-img" />
                  <img src="../../media/assets/sign-creative-active.png" class="active-img" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="heading text-yellow mt-large">INCLUSION</div>
        <div class="accessibility-description text-light">
          We value community connection, clear intent, and readiness to learn together over
          corporate or academic perfection.
        </div>

        <div class="s4-cards">
          <img
            src="../../media/assets/textbox-blue-2.png"
            alt="No Legal Registration Required: You do not need SEC, NYC, YORP, or government accreditation. Unregistered youth collectives, student networks, and community-based youth groups are fully eligible."
          />
          <img
            src="../../media/assets/textbox-blue-3.png"
            alt="Language Equity: Applications do not need to be in academic or perfect English. You are welcome to write your application in Cebuano, Ilocano, Tagalog, Taglish, English, or your mother tongue."
          />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.text-yellow {
  color: #ffdf01 !important;
  text-shadow: 2px 3px 0px rgba(0, 0, 0, 0.3) !important;
}
.subheader-dark {
  color: #092d5d !important;
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: 1.5rem;
}
.mt-large {
  margin-top: 4rem;
}

.pixel-corners {
  clip-path: polygon(
    4px 0,
    calc(100% - 4px) 0,
    100% 4px,
    100% calc(100% - 4px),
    calc(100% - 4px) 100%,
    4px 100%,
    0 calc(100% - 4px),
    0 4px
  );
}
.white-box {
  background: #fff;
  color: #092d5d;
}
.light-blue-box {
  background: #9addf7;
  color: #092d5d;
}

.scrolling-container {
  position: relative;
}

.section-panel {
  position: sticky;
  top: 70px;
  min-height: calc(100vh - 70px);
  background: #092d5d;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100px clamp(24px, 6vw, 80px);
  box-shadow: 0 -15px 30px rgba(0, 0, 0, 0.4);
  overflow: hidden;
}

@media (max-width: 899px) {
  .section-panel {
    padding: 60px clamp(16px, 4vw, 40px);
  }
}

.content-wrapper {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 48px;
  width: min(100%, 1120px);
}

.heading {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4.5vw, 4rem);
}

/* Section 1 */
.section1 {
  z-index: 1;
  box-sizing: border-box;
  background: linear-gradient(#1b2f5e 0%, #0e2a66 60%, #2f5fc4 100%);
  min-height: calc(100vh - 70px);
  justify-content: center;
  padding: clamp(40px, 6vw, 70px) clamp(12px, 2vw, 32px) clamp(60px, 14vw, 180px);
}

.section1 .content-wrapper {
  gap: clamp(24px, 4vw, 64px);
  align-items: center;
  width: min(100%, 1500px);
}

.stars-overlay {
  position: fixed;
  inset: -25vh -12vw;
  background-image:
    radial-gradient(2px 2px at 10% 10%, white 100%, transparent),
    radial-gradient(2px 2px at 30% 50%, white 100%, transparent),
    radial-gradient(3px 3px at 80% 20%, #9addf7 100%, transparent),
    radial-gradient(2px 2px at 60% 80%, white 100%, transparent),
    radial-gradient(2px 2px at 45% 25%, #9addf7 100%, transparent),
    radial-gradient(2px 2px at 90% 65%, white 100%, transparent);
  background-size: 260px 260px;
  opacity: 0.6;
  pointer-events: none;
  z-index: 0;
}

.hero-skyline {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: auto;
  pointer-events: none;
  z-index: 0;
}

#left-align {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px;
  flex: 1;
  min-width: 0;
  z-index: 2;
}

#landing-heading {
  display: flex;
  flex-direction: column;
  gap: 6px;
  width: 100%;
}

#landing-heading1 {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(1.5rem, 3.2vw, 3rem);
  color: #fff;
}

#landing-heading2 {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 8vw, 7rem);
  line-height: 1;
  color: #9addf7;
  text-shadow: 4px 6px 0 #063c70;
}

#landing-description {
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1.15rem, 1.9vw, 1.75rem);
  line-height: 1.5;
  color: #fff;
  max-width: 500px;
}

#apply-button {
  display: inline-block;
  padding: 15px 30px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  background: #ffdf01;
  border: 4px solid #fff;
  color: #000;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  transition: transform 0.1s;
}

#apply-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 0 #fff;
}

#right-align {
  flex: 1;
  display: flex;
  justify-content: center;
  width: 100%;
  max-width: 518px;
}

.hero-poster {
  width: 100%;
  height: auto;
  object-fit: contain;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
}

@media (min-width: 1024px) {
  .section1 .content-wrapper {
    flex-direction: row;
    justify-content: space-between;
  }
  #left-align {
    align-items: flex-start;
    text-align: left;
  }
}

/* Section 2 */
.section2 {
  z-index: 2;
  background: linear-gradient(#20a5fb, #87d0ff);
  padding-top: 24px;
}

.section2 .content-wrapper {
  gap: 20px;
}

.s2-cloud {
  position: absolute;
  width: clamp(140px, 22vw, 340px);
  height: auto;
  pointer-events: none;
  z-index: 0;
}
.s2-cloud-1 {
  top: 5%;
  left: 6%;
}
.s2-cloud-2 {
  top: 38%;
  right: -3%;
}
.s2-cloud-3 {
  bottom: 25%;
  left: 16%;
  width: clamp(140px, 21vw, 340px);
}

.s2-arrow {
  position: absolute;
  height: auto;
  pointer-events: none;
  z-index: 0;
}
.s2-arrow-1 {
  top: 10%;
  left: 64.5%;
  width: 20%;
}
.s2-arrow-2 {
  top: 39%;
  left: 5%;
  width: 22%;
}

.s2-logo {
  width: clamp(200px, 24vw, 340px);
  height: auto;
}
.s2-search {
  width: min(100%, 600px);
  height: auto;
}
.s2-windows {
  position: relative;
  z-index: 1;
  display: block;
  width: min(100%, 700px);
  height: auto;
}

/* Section 3 */
.section3,
.section4 {
  position: relative;
  top: auto;
}

.section3 {
  z-index: 3;
  padding-bottom: 0;
  background: linear-gradient(#7eccfe, #20a5fb);
}
.section3 .bottom-padding {
  padding-bottom: clamp(60px, 10vw, 140px);
}

.header {
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-align: center;
}
.s3-desc {
  margin: 0 auto;
  max-width: 1000px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1rem, 1.4vw, 2rem);
  line-height: 1.3;
  color: #092d5d;
  text-align: center;
}

.carousel {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
}
.c-viewport {
  flex: 1;
  overflow: hidden;
}
.c-track {
  display: flex;
  transition: transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1);
  will-change: transform;
}
.c-slide {
  flex: 0 0 33.333%;
  box-sizing: border-box;
  padding: 0 12px;
}
.c-slide img {
  display: block;
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: calc(100vh - 300px);
  margin: 0 auto;
}
.c-arrow {
  flex: 0 0 auto;
  width: clamp(24px, 4vw, 48px);
  padding: 0;
  background: none;
  border: 0;
  cursor: pointer;
}
.c-arrow img {
  display: block;
  width: 100%;
}
.c-arrow:disabled {
  opacity: 0.35;
  cursor: default;
}

.s3-cloud {
  position: absolute;
  height: auto;
  pointer-events: none;
  z-index: 0;
}
.s3-cloud-1 {
  top: 22%;
  left: -3%;
  width: clamp(180px, 30vw, 420px);
}
.s3-cloud-2 {
  top: 2%;
  right: -3%;
  width: clamp(140px, 22vw, 320px);
}

.s3-grass {
  position: absolute;
  left: 50%;
  bottom: 24px;
  width: 100vw;
  height: clamp(50px, 7vw, 100px);
  transform: translateX(-50%);
  background: url('../../../media/assets/grass.png') bottom left / auto 100% repeat-x;
  pointer-events: none;
  z-index: 0;
}

.selection-cards {
  display: flex;
  gap: 24px;
  width: 100%;
  overflow-x: auto;
  padding-bottom: 10px;
}
.selection-cards .items {
  flex: 1;
  min-width: 220px;
  display: flex;
  flex-direction: column;
}
.selection-cards .top {
  padding: 16px;
  text-align: center;
  font-weight: bold;
}
.selection-cards .bottom {
  padding: 16px;
  text-align: center;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  line-height: 1.4;
  flex-grow: 1;
}

/* Section 4 */
.section4 {
  z-index: 4;
  min-height: 0;
  padding-top: 50px;
  padding-bottom: clamp(200px, 26vw, 250px);
  background: linear-gradient(#20a5fb 0%, #fff 100%);
}
.section4 .content-wrapper {
  gap: 24px;
  width: min(100%, 1200px);
}

.s4-title {
  width: min(100%, 1000px);
  height: auto;
}
.s4-desc {
  margin: 0;
  max-width: 900px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1rem, 1.6vw, 1.5rem);
  line-height: 1.4;
  color: #fff;
  text-align: center;
}

.s4-cards {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(16px, 3vw, 48px);
  width: min(100%, 1100px);
  margin-top: 16px;
}
.s4-cards img {
  display: block;
  width: 100%;
  height: auto;
}

.s4-cloud {
  position: absolute;
  height: auto;
  pointer-events: none;
  z-index: 0;
}
.s4-cloud-1 {
  top: 12%;
  right: -3%;
  width: clamp(110px, 16vw, 240px);
}
.s4-cloud-2 {
  top: 45%;
  left: -3%;
  width: clamp(90px, 12vw, 180px);
}

.s4-buildings {
  position: absolute;
  left: 3%;
  bottom: 0;
  height: clamp(180px, 30vw, 440px);
  width: auto;
  pointer-events: none;
  z-index: 0;
}
.s4-chibi {
  position: absolute;
  right: 6%;
  bottom: 0;
  height: clamp(160px, 26vw, 380px);
  width: auto;
  pointer-events: none;
  z-index: 0;
  /* selection criteria */
}

.selection-criteria .left-align {
  position: relative;
  container-type: inline-size;
  flex: 0 0 42%;
  box-sizing: border-box;
  height: clamp(360px, 42vw, 560px);
  min-width: 0;
  text-align: left;
}

.selection-criteria .left-align > .heading {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  font-size: clamp(1.25rem, 8cqi, 3.5rem);
  line-height: 1.15;
  overflow-wrap: anywhere;
  text-shadow:
    2px 3px 0 rgba(0, 0, 0, 0.3),
    0 0 8px #ffdf01,
    0 0 20px rgba(255, 223, 1, 0.75) !important;
  z-index: 1;
}

.selection-bubble {
  position: absolute;
  top: 35%;
  left: 30%;
  width: 80%;
  max-height: 40%;
  object-fit: contain;
}

.chibi-blue-motivated {
  position: absolute;
  bottom: 0;
  left: 19%;
  width: clamp(96px, 18vw, 210px);
  max-width: 40%;
  max-height: 38%;
  object-fit: contain;
  object-position: bottom left;
}

.trophy {
  position: absolute;
  bottom: 0;
  right: 2%;
  width: clamp(68px, 12vw, 140px);
  max-width: 28%;
  max-height: 32%;
  object-fit: contain;
  object-position: bottom right;
  animation: trophy-float 2.4s ease-in-out infinite;
}

@keyframes trophy-float {
  0%,
  100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-12px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .trophy {
    animation: none;
  }
}
.selection-criteria .right-align {
  flex: 1 1 58%;
  align-self: stretch;
  position: relative;
  min-width: 0;
  display: flex;
  flex-direction: column; /* Allows vertical justification */
  align-items: center;
}

.right-align .pole-container {
  position: absolute;
  bottom: 0;
  left: 50%;
  height: 100%;
  width: auto;
  aspect-ratio: 845 / 1965;
  transform: translateX(-50%);
}

.left-buttons,
.right-buttons {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.sign-button {
  position: absolute;
  width: 80%;
  height: 20%;
  box-sizing: border-box;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  transition: all 0.2s ease-in-out;
  cursor: pointer;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
  pointer-events: auto;
  background: none;
  border: none;
}
.traffic-pole {
  position: absolute;
  left: 50%;
  bottom: 0;
  display: block;
  width: auto;
  height: 100%;
  transform: translateX(-50%);
  object-fit: contain;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
}

.sign-button img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  position: absolute;
  top: 0;
  left: 0;
}

.equity {
  top: 17%;
  left: -38%;
}

.stratigic {
  top: 37%;
  left: -30%;
}

.youth {
  top: 3%;
  left: 65%;
}

.openness {
  top: 22%;
  left: 70%;
}

.creative {
  top: 50%;
  left: 69%;
}
.sign-button .hover-img,
.sign-button .active-img {
  opacity: 0;
}

.sign-button .hover-img {
  transition: opacity 0.3s ease-in-out;
}

.sign-button:hover .hover-img {
  opacity: 1;
}

.sign-button .active-img {
  transition: opacity 0.3s ease-in-out;
}

.sign-button.is-active .active-img {
  opacity: 1;
  z-index: 2;
}
.selection-criteria {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: row;
  align-items: stretch; /* Stretches left and right panels to full height */
  justify-content: space-between;
  width: 100%;
  height: 100%;
  max-width: 1100px;
  gap: clamp(32px, 5vw, 64px);
  margin-top: 0;
}
.selection-criteria .stars-overlay {
  position: absolute;
  inset: 0 auto 0 50%;
  width: 100vw;
  margin-left: -50vw;
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

@media (max-width: 860px) {
  .selection-criteria {
    flex-direction: column;
    height: auto;
    gap: 0;
  }

  .selection-criteria .left-align {
    flex: none;
    width: 100%;
    height: clamp(360px, 72vw, 500px);
    align-items: center;
    text-align: center;
  }

  .selection-criteria .left-align > .heading {
    left: 50%;
    width: 100%;
    transform: translateX(-50%);
    text-align: center;
  }

  .selection-bubble {
    left: 50%;
    width: min(80%, 500px);
    transform: translateX(-50%);
  }

  .selection-criteria .right-align {
    flex: none;
    align-self: auto;
    width: 100%;
    position: relative;
    height: clamp(320px, 65svh, 520px);
    margin-top: 24px;
  }

  .right-align .pole-container {
    bottom: 0;
    width: auto;
  }
}

@media (max-width: 768px) {
  .message-tab {
    flex-direction: column;
  }
  .message-tab .left-align {
    min-height: 200px;
  }
  .accessibility-card {
    grid-template-columns: 1fr;
  }
  .selection-criteria .left-align {
    height: clamp(340px, 92vw, 440px);
  }

  .selection-bubble {
    width: 78%;
    max-height: 38%;
  }

  .chibi-blue-motivated {
    width: clamp(92px, 30vw, 145px);
    max-width: 40%;
  }

  .trophy {
    width: clamp(64px, 20vw, 100px);
    max-width: 28%;
  }
}

/* Tablet and mobile */
@media (max-width: 1023px) {
  .section1 {
    position: relative;
    top: auto;
    box-sizing: border-box;
    height: calc(100vh - 70px);
    height: calc(100svh - 70px);
    min-height: 0;
    padding-top: clamp(36px, 7vh, 64px);
    padding-bottom: clamp(30px, 8vw, 60px);
  }

  .section1 .content-wrapper {
    height: 100%;
    gap: 8px;
    justify-content: flex-start;
  }

  .hero-skyline {
    height: clamp(80px, 22vw, 150px);
    object-fit: cover;
    object-position: center bottom;
  }

  #left-align {
    flex: 0 0 auto;
    gap: 10px;
  }
  #landing-heading1 {
    font-size: clamp(1rem, 4vw, 1.5rem);
  }
  #landing-heading2 {
    font-size: clamp(2.5rem, 13vw, 4.5rem);
  }
  #landing-description {
    font-size: clamp(0.75rem, 2.8vw, 0.95rem);
    line-height: 1.3;
  }
  #apply-button {
    padding: 10px 20px;
    font-size: 0.95rem;
  }

  #right-align {
    flex: 1 1 0;
    min-height: 0;
    width: 100%;
    max-width: 100%;
    align-items: flex-start;
    margin-top: 20px;
  }
  .hero-poster {
    width: 100%;
    height: 100%;
    max-width: none;
    object-fit: contain;
    object-position: center top;
  }

  .s2-logo {
    width: min(72vw, 340px);
    max-width: 100%;
    flex-shrink: 0;
  }
}

@media (max-width: 767px) {
  .mt-large {
    margin-top: 1.5rem;
  }

  .section3 {
    padding: 32px 16px 0;
  }
  .section3 .content-wrapper {
    gap: 20px;
  }
  .section3 .bottom-padding {
    padding-bottom: 90px;
  }
  .section3 .heading {
    font-size: clamp(1.5rem, 8vw, 2.2rem);
  }
  .s3-desc {
    font-size: 1rem;
    line-height: 1.4;
  }

  .carousel {
    gap: 4px;
  }
  .c-arrow {
    width: 24px;
  }
  .c-viewport {
    touch-action: pan-y;
  }
  .c-slide {
    padding: 0 6px;
  }
  .c-slide img {
    max-width: 78%;
    max-height: 62vh;
  }

  .selection-cards {
    flex-direction: column;
    gap: 14px;
    overflow: visible;
  }
  .selection-cards .items {
    min-width: 0;
  }

  .s3-cloud-1 {
    top: 260px;
    left: -20px;
    width: 110px;
  }
  .s3-cloud-2 {
    top: 1%;
    width: 100px;
  }
  .s3-grass {
    height: 50px;
  }

  .section4 {
    padding: 40px 16px 0;
  }
  .section4 .content-wrapper {
    padding-bottom: 150px;
  }
  .s4-cards {
    grid-template-columns: 1fr;
    width: 75%;
    margin-top: 0;
    gap: 14px;
  }
  .s4-buildings {
    left: -12%;
    height: 270px;
  }
  .s4-chibi {
    left: 50%;
    right: auto;
    height: 230px;
  }
  .s4-cloud-1 {
    top: 190px;
    right: -20px;
    width: 100px;
  }
  .s4-cloud-2 {
    top: 300px;
    left: -24px;
    width: 120px;
  }
}
</style>
