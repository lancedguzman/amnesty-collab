<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="content-wrapper">
      <!-- Updated header banner path -->
      <div class="header-banner">
        <img
          src="../../media/assets/application-header.png"
          alt="Digital Movers - Apply to Start"
        />
      </div>

      <h1 class="page-title">Digital Movers Application</h1>
      <p class="intro-text">
        Applications must be submitted online through our official application form.
      </p>

      <div class="form-container">
        <a
          href="https://forms.cloud.microsoft/e/JERQfXvmLg"
          target="_blank"
          rel="noopener noreferrer"
          class="pixel-apply-btn"
        >
          Go to MS Form Application
        </a>
      </div>
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
  text-align: center;
}

/* Header Banner styling */
.header-banner {
  width: 100%;
  max-width: 800px;
  border: 4px solid #fff;
  box-shadow:
    8px 8px 0 #063c70,
    0 0 12px 3px rgba(255, 255, 255, 0.45);
  overflow: hidden;
  margin-bottom: 1.5rem;
  line-height: 0;
}

.header-banner img {
  width: 100%;
  height: auto;
  display: block;
}

.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(4rem, 4.5vw, 5rem);
  color: #fff;
  text-shadow: 3px 4px 0 #20a5fb;
  margin: 0 0 1rem 0;
  line-height: 0.8;
}

.intro-text {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  line-height: 1.4;
  color: #fff;
  margin: 0;
}

.form-container {
  margin-top: 2rem;
}

.pixel-apply-btn {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  padding: 15px 30px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  text-decoration: none;
  color: #000;
  background: #fae11b;
  border: 3px solid #fae11b;
  box-shadow: 7px 7px 0 #fff;
  cursor: pointer;
  transition:
    transform 0.1s,
    box-shadow 0.1s;
}

.pixel-apply-btn:hover {
  transform: translate(3px, 3px);
  box-shadow: 4px 4px 0px #fff;
}

.pixel-apply-btn:focus-visible {
  outline: 3px solid #fae11b;
  outline-offset: 3px;
}
</style>
