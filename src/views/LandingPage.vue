<script setup>
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />

  <div class="scrolling-container">
    <!-- SECTION 1 -->
    <div class="section-panel section1">
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
          <button id="apply-button">APPLY NOW!</button>
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

    <!-- SECTION 2 -->
    <div class="section-panel section2">
      <div class="content-wrapper">
        <div class="header">
          <div class="heading text-yellow">Digital Movers</div>
          <div class="description text-light">Capacity-building and Seed Funding Program</div>
        </div>

        <div class="description-grid">
          <div class="center">
            <div class="heading subheader-blue">What is Digital movers?</div>
            <div class="description text-light">
              Digital Movers is a capacity-building and seed funding program by Amnesty
              International Philippines (AIPH). We support Filipino youth-led groups and grassroots
              collectives to launch creative Human Rights Education (HRE) or campaign initiatives.
              <br />
              <br />
              Six youth collectives will start the journey together through online learning and a
              fully-funded national youth hackathon (Nov 2026 - Jan 2027). <br />
              <br />
              Following a pitch showcase at the youth hackathon, the Top 3 finalist groups will
              receive seed funding and mentorship to run their campaigns through August 2027.
            </div>
          </div>
          <div class="content2-right"></div>
        </div>

        <div class="card-deck">
          <div class="card-item pixel-corners white-box">
            <div class="heading subheader-blue">Evolving Digital Landscape</div>
            <div class="description">
              Digital platforms are now a primary civic space for children and young people across
              the Philippines. However, heavy online engagement also exposes youth to privacy
              violations, online harm, and state surveillance.
            </div>
          </div>

          <div class="card-item pixel-corners white-box">
            <div class="heading subheader-blue">The Importance of Youth-Led Advocacy</div>
            <div class="description">
              The Philippines is home to diverse youth-led groups that champion human rights in
              their communities. Recognizing young people as experts in their own experiences, the
              Digital Movers program aims to boost their impact through technical guidance and
              resources so they can advance their advocacies safely.
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SECTION 3 -->
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

        <div class="heading text-yellow mt-large">Accessibility & Inclusion</div>
        <div class="accessibility-description text-light">
          We value community connection, clear intent, and readiness to learn together over
          corporate or academic perfection.
        </div>

        <div class="accessibility-card">
          <div class="accessibility-item">
            <div class="heading subheader-blue">No Legal Registration Required</div>
            <div class="description text-light">
              You do not need SEC, NYC, YORP, or government accreditation. Unregistered youth
              collectives, student networks, and community-based youth groups are fully eligible.
            </div>
          </div>
          <div class="accessibility-item">
            <div class="heading subheader-blue">Language Equity</div>
            <div class="description text-light">
              Applications do not need to be in academic or perfect English. You are welcome to
              write your application in Cebuano, Ilocano, Tagalog, Taglish, English, or your mother
              tongue.
            </div>
          </div>
        </div>
      </div>

      <!-- Skyline added to the bottom of the page -->
      <div class="skyline-footer"></div>
    </div>
  </div>
</template>

<style scoped>
/* GLOBAL STYLES & FONTS */
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

/* PIXEL CORNERS */
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

/* PANEL OVERRIDE ANIMATION (Sticky Sections) */
.scrolling-container {
  position: relative;
}

.section-panel {
  position: sticky;
  top: 70px; /* Sits just below the navbar */
  min-height: calc(100vh - 70px);
  background: #092d5d; /* Uniform dark blue bg */
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100px clamp(24px, 6vw, 80px); /* Increased spacing */
  box-shadow: 0 -15px 30px rgba(0, 0, 0, 0.4); /* Shadow for overlapping effect */
  overflow: hidden;
}

.section1 {
  z-index: 1;
}
.section2 {
  z-index: 2;
}
.section3 {
  z-index: 3;
  padding-bottom: 0;
}

.section1::before {
  position: absolute;
  inset: 0;
  z-index: 0;
  background-image: url('../../../media/assets/StarsLanding.png');
  background-repeat: repeat;
  background-size: 768px 768px;
  content: '';
  pointer-events: none;
  opacity: 0.5;
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
  padding-bottom: 250px; /* Space for the skyline */
}

/* SECTION 1 CONTENT */
#left-align {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 24px;
  flex: 1 1 0;
}
#landing-heading {
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%;
}
#landing-heading1 {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(1.5rem, 5vw, 4rem);
  color: #fff;
}
#landing-heading2 {
  font-family: 'Arcade Bit', 'ByteBounce', sans-serif;
  font-size: clamp(2.5rem, 20cqi, 9rem);
  color: #9addf7;
  text-shadow: 4px 6px 0 #063c70;
}

#landing-description {
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  line-height: 1.5;
  color: #fff;
  max-width: 700px;
}

#apply-button {
  padding: 15px 30px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  background: #ffdf01;
  border: 4px solid #fff;
  color: #000;
  cursor: pointer;
  transition: transform 0.1s;
}
#apply-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 4px 0 #fff;
}

#right-align {
  flex: 0 1 440px;
  display: flex;
  justify-content: center;
}
.hero-poster {
  width: 100%;
  object-fit: contain;
  filter: drop-shadow(4px 4px 0px rgba(0, 0, 0, 0.4));
}

@media (min-width: 900px) {
  .section1 .content-wrapper {
    flex-direction: row;
  }
}

/* SECTION 2 CONTENT */
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

.description-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 700px) minmax(0, 1fr);
  gap: 24px;
  width: 100%;
}
.description-grid .center {
  grid-column: 2;
  text-align: center;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.content2-right {
  grid-column: 3;
  background-image: url('../../../media/assets/GreenCharLanding.png');
  background-position: right bottom;
  background-repeat: no-repeat;
  background-size: contain;
  width: 100%;
  aspect-ratio: 2/3;
}

.card-deck {
  display: flex;
  gap: 24px;
  width: 100%;
}
.card-item {
  flex: 1;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.card-item .description {
  text-align: left;
}

@media (max-width: 1100px) {
  .description-grid {
    grid-template-columns: 1fr;
  }
  .description-grid .center,
  .content2-right {
    grid-column: 1;
  }
  .card-deck {
    flex-direction: column;
  }
}

/* SECTION 3 CONTENT */
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
  align-items: center;
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

/* SKYLINE FOOTER */
.skyline-footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 200px;
  background-image: url('../../../media/assets/CityLanding.png');
  background-position: bottom center;
  background-repeat: repeat-x;
  background-size: auto 100%;
  pointer-events: none;
  z-index: 0;
}
</style>
