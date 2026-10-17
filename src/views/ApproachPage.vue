<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const data = ref({
  title: 'Revolutionizing Youth Engagement In the PH',
  intro:
    'Young people want real decision-making power, not tokenistic participation! We’re not interested in creating mini-adults. Rather, we support genuine youth-led and youth-owned initiatives that challenge dominant narratives with creative, accessible, and hopeful messages.',
  lead: 'You’ll enjoy working with us if you want to:',
  boxAlt:
    'Shift from participation to shared power, ensuring children and youth influence decision-making processes. Build safe and enabling environments with strong safeguarding protocols, particularly for children and youth. Develop age-appropriate engagement approaches tailored specifically to children and youth. Counter harmful narratives by promoting children and young people’s rights, agency, and participation. Integrate well-being and resilience into engagement strategies. Localize approaches to reflect diverse contexts and lived realities.',
})
</script>

<template>
  <NavBar />
  <div class="page-container">
    <img class="ap-heart" src="../../media/assets/approach-heart.png" alt="" />
    <img class="ap-buildings" src="../../media/assets/approach-buildings.png" alt="" />

    <div class="content-wrapper">
      <img class="ap-pill" src="../../media/assets/approach-pill.png" alt="Our Approach" />

      <h1 class="page-title">{{ data.title }}</h1>

      <div class="text-block">
        <p class="intro-text">{{ data.intro }}</p>
        <p class="intro-text">{{ data.lead }}</p>
      </div>

      <img class="ap-box" src="../../media/assets/approach-box.png" :alt="data.boxAlt" />
    </div>
  </div>
</template>

<style scoped>
.page-container {
  position: relative;
  box-sizing: border-box;
  min-height: calc(100vh - 76px);
  padding: 56px clamp(24px, 6vw, 80px) 72px;
  background: linear-gradient(#9fd0fb 0%, #5ea2f3 45%, #0f1c3d 100%);
  color: #fff;
  overflow: hidden;
}

.content-wrapper {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 28px;
  width: min(100%, 1200px);
  margin: 0 auto;
}

.ap-pill {
  width: clamp(200px, 26vw, 340px);
  height: auto;
}

.page-title {
  margin: 0;
  max-width: 1300px;
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-weight: normal;
  font-size: clamp(2rem, 5.2vw, 4rem);
  line-height: 1.3;
  color: #fff;
  text-align: left;
  text-shadow:
    -3px -3px 0 #092d5d, 3px -3px 0 #092d5d,
    -3px 3px 0 #092d5d, 3px 3px 0 #092d5d,
    0 4px 0 #092d5d;
}

.text-block {
  display: flex;
  flex-direction: column;
  gap: 24px;
  max-width: 740px;
}

.intro-text {
  margin: 0;
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1.05rem, 1.5vw, 2rem);
  line-height: 1.35;
  color: #fff;
  text-align: left;
}

.ap-box {
  width: min(100%, 760px);
  height: auto;
  margin-top: 16px;
}

.ap-heart {
  position: absolute;
  top: 7%;
  right: 12%;
  width: clamp(60px, 8vw, 120px);
  height: auto;
  z-index: 0;
  pointer-events: none;
}

.ap-buildings {
  position: absolute;
  right: 0;
  bottom: 0;
  height: min(110%, 1200px);
  width: auto;
  z-index: 0;
  pointer-events: none;
}

@media (max-width: 1023px) {
  .page-container {
    padding: 40px clamp(16px, 4vw, 32px) 56px;
  }

  .ap-box {
    width: 100%;
  }

  .ap-buildings {
    height: 45%;
    opacity: 0.35;
  }

  .ap-heart {
    top: 3%;
    right: 6%;
  }
}

@media (max-width: 767px) {
  .content-wrapper {
    gap: 18px;
  }

  .ap-pill {
    width: clamp(150px, 48vw, 220px);
  }

  .page-title {
    font-size: clamp(1.1rem, 6.2vw, 2rem);
    line-height: 1.3;
    text-shadow:
      -2px -2px 0 #092d5d, 2px -2px 0 #092d5d,
      -2px 2px 0 #092d5d, 2px 2px 0 #092d5d,
      0 3px 0 #092d5d;
  }

  .intro-text {
    font-size: clamp(0.95rem, 4vw, 1.1rem);
    line-height: 1.4;
  }

  .ap-heart {
    top: 1.5%;
    right: 4%;
    width: clamp(44px, 12vw, 70px);
  }
}
</style>