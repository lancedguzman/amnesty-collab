<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <footer class="site-footer">
    <!-- Background Layers -->
    <div class="footer-bg-container">
      <img src="../../../media/assets/bg-footer.png" class="bg-gradient" alt="" />
    </div>

    <div class="footer-content">
      <!-- Left Section: Characters & Bubble -->
      <div class="left-section">
        <!-- Moved glow directly behind the chibis -->
        <div class="glow">
          <img src="../../../media/assets/bg-light.png" class="bg-glow" alt="" />
        </div>

        <img
          src="../../../media/assets/chat_bubble.png"
          alt="Apply and join by November 9!"
          class="chat-bubble"
        />
        <img
          src="../../../media/assets/chibis-group.png"
          alt="Digital Movers Team Chibis"
          class="chibis"
        />
      </div>

      <!-- Right Section: Navigation & Contact -->
      <div class="right-section">
        <nav class="nav-links">
          <div class="nav-column">
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/approach">Our Approach</RouterLink>
            <RouterLink to="/criteria">What We Look For</RouterLink>
          </div>
          <div class="nav-column">
            <RouterLink to="/timeline">Timeline</RouterLink>
            <RouterLink to="/faqs">FAQs</RouterLink>
            <RouterLink to="/contact">Contact</RouterLink>
          </div>
        </nav>

        <img
          src="../../../media/assets/email.png"
          alt="cydphilippines@amnesty.org.ph search bar"
          class="email-input"
        />

        <div class="social-links">
          <a href="https://www.facebook.com/amnestyph" aria-label="Facebook">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
            </svg>
          </a>
          <a href="https://www.instagram.com/amnesty_ph" aria-label="Instagram">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>
          <a href="https://www.tiktok.com/@amnesty?lang=en" aria-label="TikTok">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5"></path>
            </svg>
          </a>
          <a href="https://www.youtube.com/aiphilippines" aria-label="YouTube">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            >
              <path
                d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"
              ></path>
              <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
            </svg>
          </a>
          <a href="https://www.linkedin.com/company/amnestyph/" aria-label="LinkedIn">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"
              ></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>
          </a>
        </div>
      </div>
    </div>

    <!-- Bottom Section: Full Width Copyright Bar -->
    <div class="footer-bottom">
      <img
        src="../../../media/assets/copyright.png"
        alt="Copyright © 2026 Amnesty International"
        class="copyright-img"
      />
    </div>
  </footer>
</template>

<style scoped>
.site-footer {
  display: flex;
  flex-direction: column;
  width: 100%;
  position: relative;
  z-index: 10;
  padding-top: clamp(40px, 8vw, 80px);
  font-family: 'Geist Pixel', sans-serif;
  color: #ffffff;
  margin: 0;
  
}

/* Background Implementation */
.footer-bg-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
}

.bg-gradient {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
}

.footer-content {
  display: flex;
  justify-content: center; /* Changed to center to use precise gaping */
  gap: clamp(
    60px,
    10vw,
    160px
  ); /* Creates the specific large space between left and right sections */
  align-items: flex-end;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 clamp(24px, 6vw, 80px) 0;
 
}

/* Left Section */
.left-section {
  position: relative;
  z-index: 1; /* Establishes a stacking context for the glow */
}

.glow {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
}

.bg-glow {
  position: absolute;
  top: 45%; /* Adjusted vertically to perfectly frame the chibis */
  left: 50%;
  transform: translate(-50%, -50%);
  width: 180%; /* Scales relative to the size of the chibis container */
  max-width: 800px;
  height: auto;
  mix-blend-mode: screen;
  opacity: 0.95;
  pointer-events: none;
  z-index: 0;
}

.chat-bubble {
  position: absolute;
  bottom: 95%;
  left: 15%;
  width: clamp(180px, 22vw, 280px);
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.25));
  animation: float 3.5s ease-in-out infinite;
  z-index: 3;
}

.chibis {
  width: clamp(220px, 32vw, 400px);
  height: auto;
  display: block;
  z-index: 2;
  position: relative;
}

/* Right Section */
.right-section {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1.5rem;
  margin-bottom: 2rem;
  z-index: 2;
}

.avatar-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5rem;
}

.avatar-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  background-color: #20a5fb;
  border: 3px solid #7eccfe;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  /* Optional: replace background-color with a background-image if you export the avatar head */
}

.nav-links {
  display: grid;
  grid-template-columns: auto auto;
  gap: 1.5rem 4.5rem;
}

.nav-column {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.nav-column a {
  color: #ffffff;
  text-decoration: none;
  font-size: clamp(0.9rem, 1.5vw, 1.15rem);
  letter-spacing: 1px;
  transition: color 0.2s ease;
}

.nav-column a:hover {
  color: #9addf7;
  text-shadow: 0 0 5px rgba(154, 221, 247, 0.5);
}

.email-input {
  width: min(100%, 380px);
  height: auto;
  margin-top: 0.5rem;
  cursor: text;
  transition: transform 0.2s;
}

.email-input:hover {
  transform: scale(1.02);
}

.social-links {
  display: flex;
  gap: 1.25rem;
  padding-left: 0.5rem;
}

.social-links a {
  color: #b5c7e0;
  display: flex;
  align-items: center;
  justify-content: center;
  transition:
    transform 0.2s ease,
    color 0.2s ease;
}

.social-links a:hover {
  color: #ffffff;
  transform: translateY(-3px);
}

/* Bottom Section */
.footer-bottom {
  width: 100%;
  background-color: #161a26;
  display: flex;
}

.copyright-img {
  width: 100%;
  height: auto;
  display: block;
}

/* Animations */
@keyframes float {
  0%,
  100% {
    transform: translateY(8px);
  }
  50% {
    transform: translateY(-8px);
  }
}

/* Responsive Styles */
@media (max-width: 899px) {
  .footer-content {
    flex-direction: column;
    align-items: center;
    gap: 4rem;
  }

  .left-section {
    order: 2;
  }

  .right-section {
    order: 1;
    align-items: center;
    text-align: center;
  }

  .nav-links {
    gap: 1.5rem 3rem;
  }

  .email-input {
    width: min(100%, 320px);
  }

  .social-links {
    padding-left: 0;
  }
}

@media (max-width: 480px) {
  .nav-links {
    grid-template-columns: 1fr;
    gap: 1.25rem;
    text-align: center;
  }

  .chat-bubble {
    left: 10%;
    bottom: 90%;
  }
}
</style>
