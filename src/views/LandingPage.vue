<script setup>
import { onMounted } from 'vue'
import NavBar from './components/NavBar.vue'
import confetti from 'canvas-confetti'

onMounted(() => {
  // Check localStorage to see if the user has visited before
  const hasVisited = localStorage.getItem('hasVisitedLandingPage')

  if (!hasVisited) {
    // Trigger the confetti effect
    confetti({
      particleCount: 150,
      spread: 80,
      origin: { y: 0.6 },
      colors: ['#ffdf01', '#9addf7', '#092d5d', '#ffffff'], // Matches your brand colors
    })

    // Set the flag so it doesn't trigger on future reloads
    localStorage.setItem('hasVisitedLandingPage', 'true')
  }
})
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
        <img class="s2-logo" src="../../media/assets/logo-digital movers.png" alt="Digital Movers" />
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
      <div class="content-wrapper bottom-padding">
        <div class="header">
          <div class="heading text-yellow">What We Look For</div>
          <div class="description text-light">
            Digital Movers supports youth-led groups with new or ongoing campaign ideas that need
            financial resourcing and capacity building
          </div>
        </div>

        <div class="message-tab pixel-corners light-blue-box">
          <div class="popup-controls"></div>
          <div class="left-align"></div>
          <div class="right-align pixel-corners white-box">
            <div class="heading subheader-blue">Eligibility Requirements</div>
            <div class="description">
              <ul class="eligibility-list">
                <li>
                  Youth-Led: A Filipino group/organization/collective whose members are primarily 25
                  years old and below
                </li>
                <li>
                  Defined Organizational Structure: consistent membership and leadership setup
                </li>
                <li>Dedicated Project Team: can delegate 3 to 5 young leaders (aged 15-24)</li>
                <li>
                  Proven Experience: proven track record of running local projects or campaigns
                </li>
                <li>
                  Focus Areas: human rights, digital rights, children's rights, indigenous people's
                  rights, climate justice, anti-discrimination and inclusion, sexual and
                  reproductive health and rights.
                </li>
                <li>Philippines-based</li>
              </ul>
            </div>
          </div>
        </div>

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

        <div class="heading text-yellow mt-large">INCLUSION</div>
        <div class="accessibility-description text-light">
          We value community connection, clear intent, and readiness to learn together over
          corporate or academic perfection.
        </div>

        <div class="accessibility-card">
          <div class="accessibility-item">
            <div class="heading subheader-blue">NO LEGAL REGISTRATION REQUIRED</div>
            <div class="description text-light">
              You do not need SEC, NYC, YORP, or government accreditation. Unregistered youth
              collectives, student networks, and community-based youth groups are fully eligible.
            </div>
          </div>
          <div class="accessibility-item">
            <div class="heading subheader-blue">LANGUAGE EQUITY</div>
            <div class="description text-light">
              Applications do not need to be in academic or perfect English. You are welcome to
              write your application in Cebuano, Ilocano, Tagalog, Taglish, English, or your mother
              tongue.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.text-light {
  color: #fff !important;
}
.text-yellow {
  color: #ffdf01 !important;
  text-shadow: 2px 3px 0px rgba(0, 0, 0, 0.3) !important;
}
.subheader-blue {
  color: #9addf7 !important;
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: 2rem;
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

.section3 {
  z-index: 3;
  padding-bottom: 0;
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

.bottom-padding {
  padding-bottom: 60px;
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
  transform: translate3d(var(--bg-x, 0px), var(--bg-y, 0px), 0) scaleY(var(--bg-stretch, 1));
  will-change: transform;
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
.header {
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.heading {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4.5vw, 4rem);
}
.description {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  line-height: 1.5;
  text-align: center;
}

.message-tab {
  display: flex;
  gap: 24px;
  width: 100%;
  padding: 24px;
}
.message-tab .left-align {
  flex: 0 0 25%;
  background-image: url('../../../media/assets/PinkCharLanding.png');
  background-position: center bottom;
  background-repeat: no-repeat;
  background-size: contain;
}
.message-tab .right-align {
  flex: 1;
  padding: 24px;
}

.eligibility-list {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  margin: 0;
  padding-left: 1.5rem;
  text-align: left;
}
.eligibility-list li {
  margin-bottom: 8px;
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

.accessibility-description {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  line-height: 1.5;
  text-align: center;
  max-width: 800px;
}
.accessibility-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  width: 100%;
}
.accessibility-item {
  padding: 24px 0;
  border-top: 4px solid #ffdf01;
  border-bottom: 4px solid #ffdf01;
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  word-break: break-word;
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
</style>