<template>
  <div class="page-container">
    <img
      src="../../media/assets/digital-mover-logo.png"
      alt="Digital Movers Logo"
      class="overlay-logo-movers"
    />

    <a
      href="https://forms.cloud.microsoft/e/JERQfXvmLg"
      target="_blank"
      rel="noopener noreferrer"
      class="overlay-apply-link"
    >
      <img src="../../media/assets/apply-now-btn.png" alt="Apply Now" class="overlay-apply-btn" />
    </a>

    <img
      src="../../media/assets/amnesty-logo.png"
      alt="Amnesty Logo"
      class="overlay-logo-amnesty"
    />
  </div>
</template>

<style scoped>
.page-container {
  box-sizing: border-box;
  min-height: calc(100vh - 76px); /* Adjust based on your nav height */
  width: 100%; /* Ensures it spans the full width */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 64px clamp(24px, 6vw, 80px);
  position: relative; /* Constrains absolutely positioned child images */

  /* Background image properties to cover the entire container */
  background-image: url('../../media/assets/application-page.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

  color: #fff;
}

/* Updated overlay image styles based on application-header.jpg layout */
.overlay-logo-movers {
  position: absolute;
  top: 12%;
  right: 15%;
  width: clamp(350px, 135vw, 600px);
  height: auto;
}

.overlay-apply-link {
  position: absolute;
  top: 58%;
  right: 24%;
  transform: translateY(-50%);
  transition: transform 0.1s;
}

.overlay-apply-link:hover {
  transform: translateY(-50%) scale(1.05);
}

.overlay-apply-btn {
  width: clamp(150px, 20vw, 250px);
  height: auto;
}

.overlay-logo-amnesty {
  position: absolute;
  bottom: 6%;
  right: 4%;
  width: clamp(120px, 15vw, 200px);
  height: auto;
  background-color: #ffffff; /* Added white background to match the reference */
  padding: 8px 12px;
}

/* Original styles below */
.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4vw, 4.5rem);
  color: #fff;
  text-shadow: 2px 3px 0 #20a5fb;
  margin: 0 0 1rem 0;
  text-align: center;
  line-height: 1.1;
  word-spacing: 0.5rem;
  letter-spacing: 2px;
}

.intro-text {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  line-height: 1.4;
  color: #fff;
  margin: 0;
  text-shadow: 1px 1px 2px #000;
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

@media (max-width: 768px) {
  .page-container {
    padding: 40px clamp(16px, 4vw, 32px);
  }
}
</style>
