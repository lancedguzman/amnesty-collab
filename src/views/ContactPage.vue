<script setup>
import NavBar from './components/NavBar.vue'
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
  height: calc(100vh - 76px);
  position: relative;
  background: #0b1a40;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* Removed bottom padding (set to 0) so the pole can sit completely flush */
  padding: 8vh clamp(24px, 6vw, 80px) 0;
  overflow: hidden;
  font-family: 'Geist Pixel', sans-serif;
}

/* Static Star Background */
.stars-overlay {
  position: absolute;
  inset: 0;
  background-image:
    radial-gradient(1px 1px at 10% 10%, white 100%, transparent),
    radial-gradient(1px 1px at 30% 50%, white 100%, transparent),
    radial-gradient(2px 2px at 80% 20%, white 100%, transparent),
    radial-gradient(1px 1px at 60% 80%, white 100%, transparent);
  background-size: 200px 200px;
  opacity: 0.5;
  pointer-events: none;
  z-index: 0;
}

.content-wrapper {
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
  flex-direction: column; /* Allows vertical justification */
  justify-content: flex-end; /* Anchors the pole directly to the bottom edge */
  align-items: center;
  height: 100%;
}

.pole-container {
  position: relative;
  display: inline-block;
  height: 75vh;
}

.traffic-pole {
  height: 100%;
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

.sign-faq {
  top: 12%;
  left: 47%;
  transform: rotate(5deg);
}

.sign-email {
  top: 32%;
  left: 46%;
  transform: rotate(5deg);
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
  left: 49%;
  transform: translate(-50%, -50%) rotate(-16deg);
  width: 85%;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: clamp(1.4rem, 2vh, 1.4rem);
  text-align: center;
  font-weight: bold;
  line-height: 1.4;
  white-space: nowrap;
  text-shadow: 2px 2px 0px #092d5d;
}

.small-text {
  left: 46%;
  font-size: clamp(0.9rem, 1.5vh, 1.1rem);
  transform: translate(-50%, -50%) rotate(-16deg);
}

/* RESPONSIVE LAYOUT */
@media (max-width: 860px) {
  .page-container {
    height: auto;
    min-height: calc(100vh - 76px);
    overflow-y: auto;
    padding-top: 40px;
    padding-bottom: 0; /* Keeps it flush at the bottom on mobile too */
  }

  .content-wrapper {
    flex-direction: column;
    margin-top: 0;
    height: auto;
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
    margin-top: 48px;
    height: 60vh;
  }
}
</style>
