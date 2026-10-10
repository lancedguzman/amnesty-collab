<script setup>
    import NavBar from './components/NavBar.vue'

</script>
<template>
    <NavBar />

    <div class="section1">
        <div class="content1">

            <div id="left-align">
                <div id="landing-heading">
                    <div id="landing-heading1">let's make the</div>
                    <div id="landing-heading2" data-text="MOVE">MOVE</div>
                </div>
                <div id="landing-description">An Amnesty International Philippines Capacity-building and Seed Funding Program for Youth Organizations</div>
                <button id="apply-button">APPLY</button>
            </div>

            <div id="right-align">
            </div>
        </div>
    </div>

    <div class="section2">
        <div class="content2">

            <div class="header">
                <div class="heading">Digital Movers</div>
                <div class="description">Capacity-building and Seed Funding Program</div>
            </div>

            <div class="description">
                <div class="center">

                    <div class="heading">What is Digital movers?</div>
                    <div class="description">Digital Movers is a capacity-building and seed funding program by Amnesty International Philippines (AIPH). We support Filipino youth-led groups and grassroots collectives to launch creative Human Rights Education (HRE) or campaign initiatives.
                        <br> <br> Six youth collectives will start the journey together through online learning and a fully-funded national youth hackathon (Nov 2026 - Jan 2027).
                        <br> <br> Following a pitch showcase at the youth hackathon, the Top 3 finalist groups will receive seed funding and mentorship to run their campaigns through August 2027.
                    </div>

                </div>

                <div class="content2-right"></div>

            </div>

            <div class="card-deck">
                <div class="card-item">
                    <div class="heading">Evolving Digital Landscape</div>
                    <div class="description">Digital platforms are now a primary civic space for children and young people across the Philippines. However, heavy online engagement also exposes youth to privacy violations, online harm, and state surveillance.</div>
                </div>

                <div class="card-item">
                    <div class="heading">The Importance of Youth-Led Advocacy</div>
                    <div class="description">The Philippines is home to diverse youth-led groups that champion human rights in their communities. Recognizing young people as experts in their own experiences, the Digital Movers program aims to boost their impact through technical guidance and resources so they can advance their advocacies safely.</div>
                </div>
                
            </div>
        </div>
    </div>

    <div id="section3" class="section3">
        <div class="content3">
            <div class="header">What We Look For</div>
            <div class="description">Digital Movers supports youth-led groups with new or ongoing campaign 
                ideas that need financial resourcing and capacity building
            </div>

            <div class="message-tab">
                <div class="popup-controls"></div>
                <div class="left-align"></div>
                <div class="right-align">
                    <div class="header">Eligibility Requirements</div>
                    <div class="description">
                        <ul class="eligibility-list">
                            <li>Youth-Led: A Filipino group/organization/collective whose members are primarily 25 years old and below</li>
                            <li>Defined Organizational Structure: consistent membership and leadership setup</li>
                            <li>Dedicated Project Team: can delegate 3 to 5 young leaders (aged 15-24)</li>
                            <li>Proven Experience: proven track record of running local projects or campaigns</li>
                            <li>Focus Areas: human rights, digital rights, children's rights, indigenous people's rights, climate justice, anti-discrimination and inclusion, sexual and reproductive health and rights.</li>
                            <li>Philippines-based</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="yellow-heading">Selection Criteria</div>
            <div class="selection-cards" tabindex="0" aria-label="Selection criteria cards">
                <div class="items">
                    <div class="top">Equity & Inclusion</div>
                    <div class="mid"></div>
                    <div class="bottom">Priority is given to under-resourced and under-represented youth collectives</div>
                </div>

                <div class="items">
                    <div class="top">Strategic Issue Alignment</div>
                    <div class="mid"></div>
                    <div class="bottom">A clear, feasible campaign plan aligned with human rights focus areas</div>
                </div>

                <div class="items">
                    <div class="top">Youth Ownership & Team Dynamic</div>
                    <div class="mid"></div>
                    <div class="bottom">Truly youth-led with a stable, committed core membership that cares for its community</div>
                </div>

                <div class="items">
                    <div class="top">Openness To Learn</div>
                    <div class="mid"></div>
                    <div class="bottom">Willingness to engage fully in a 9-month journey (you do not need to be experts yet!)</div>
                </div>
            </div>

            <div class="yellow-heading">Accessibility & Inclusion</div>
            <div class="accessibility-description">We value community connection, clear intent, and readiness to learn together over corporate or academic perfection.</div>
            
            <div class="accessibility-card">
                <div class="accessibility-item">
                    <div class="heading">No Legal Registration Required</div>
                    <div class="description">You do not need SEC, NYC, YORP, or government accreditation. Unregistered youth collectives, student networks, and community-based youth groups are fully eligible.</div>
                </div>
                <div class="accessibility-item">
                    <div class="heading">Language Equity</div>
                    <div class="description">Applications do not need to be in academic or perfect English. You are welcome to write your application in Cebuano, Ilocano, Tagalog, Taglish, English, or your mother tongue.</div>
                </div>
            </div>
        </div>
    </div>

</template>

<style scoped>
/* SECTION 3 */
.section3 {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  padding: 64px clamp(24px, 6vw, 80px);
  background: #092d5d;
  color: #fff;
}

.content3 {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  width: min(100%, 1120px);
}

.popup-controls {
  position: absolute;
  z-index: 1;
  top: 12px;
  right: 16px;
  width: clamp(96px, 12vw, 140px);
  aspect-ratio: 3 / 2;
  background-image: url('../../../media/assets/PopUp.png');
  background-position: top right;
  background-repeat: no-repeat;
  background-size: contain;
  pointer-events: none;
}
.content3 > .header {
  position: static;
  width: 100%;
  height: auto;
  color: #fff;
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(4rem, 4.5vw, 5rem);
  font-weight: 400;
  line-height: 0.6;
  text-align: center;
  text-shadow: 3px 4px 0 #20a5fb;
}

.content3 > .description {
  width: min(100%, 700px);
  height: auto;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.35;
  text-align: center;
}

.message-tab {
  position: relative;
  box-sizing: border-box;
  display: flex;
  align-items: stretch;
  gap: clamp(16px, 4vw, 36px);
  width: 100%;
  min-height: clamp(300px, 36vw, 420px);
  margin-top: 2px;
  padding: clamp(16px, 3vw, 30px);
  border: 6px solid #087fc4;
  background: #0872b5;
  box-shadow:
    inset 0 0 0 4px #07508a,
    8px 8px 0 #063c70,
    0 0 12px 3px rgba(255, 255, 255, 0.45);
}

.message-tab .left-align {
  flex: 0 0 27%;
  align-self: stretch;
  min-height: 0;
  margin-top: 42px;
  background-image: url('../../../media/assets/PinkCharLanding.png');
  background-position: center bottom;
  background-repeat: no-repeat;
  background-size: contain;
}

.message-tab .right-align {
  box-sizing: border-box;
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
  margin-top: 42px;
  padding: 16px;
  border: 4px solid #fff;
  background: #063c70;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
}

.message-tab .right-align .header {
  width: 100%;
  height: auto;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.3;
}

.message-tab .right-align .description {
  width: 100%;
  height: auto;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.35;
}

.eligibility-list {
  margin: 0;
  padding-left: 1.2em;
}

.eligibility-list li + li {
  margin-top: 2px;
}

.yellow-heading {
  width: 100%;
  color: #fae11b;
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(3rem, 4vw, 4rem);
  font-weight: 400;
  line-height: 0.65;
  text-align: center;
  padding: 15px 0 0 0;
  text-shadow: 0 0 10px #fae11b;
}

.selection-cards {
  box-sizing: border-box;
  display: flex;
  justify-content: safe center;
  align-items: stretch;
  gap: clamp(24px, 4vw, 42px);
  width: 100%;
  padding: 15px 0 10px;
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scrollbar-color: #20a5fb #092d5d;
  scrollbar-width: thin;
  -webkit-overflow-scrolling: touch;
}

.selection-cards:focus-visible {
  outline: 2px solid #20a5fb;
  outline-offset: 4px;
}

.selection-cards .items {
  box-sizing: border-box;
  display: grid;
  flex: 0 0 clamp(190px, 22vw, 214px);
  grid-template-rows: 22% 43% 35%;
  min-width: 0;
  height: clamp(360px, 43vw, 410px);
  overflow: hidden;
  background: #fff;
  border: 2px solid #1a191c;
  scroll-snap-align: start;
}

.items .top {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 12px;
  border-bottom: 2px solid #1a191c;
  background: #0897fd;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.4;
  text-align: center;
}

.items .mid {
  min-height: 0;
  background: #fff;
}

.items .bottom {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 12px;
  border-top: 2px solid #1a191c;
  background: #0897fd;
  color: rgba(255, 255, 255, 0.85);
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.4;
  text-align: center;
}
@media (max-width: 700px) {
  .message-tab {
    flex-direction: column;
    gap: 12px;
    padding: 18px;
  }

  .message-tab .left-align {
    flex: 0 0 auto;
    width: 100%;
    min-height: clamp(180px, 55vw, 280px);
    margin-top: 28px;
  }

  .message-tab .right-align {
    flex: 0 0 auto;
    margin-top: 0;
    padding: 12px;
  }
}

.accessibility-description {
  width: min(100%, 700px);
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.35;
  text-align: center;
}

.accessibility-card {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0 24px;
  width: 100%;
}

.accessibility-item {
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  min-width: 0;
  min-height: 106px;
  padding: 14px 12px;
  border-top: 2px solid #fae11b;
  border-bottom: 2px solid #fae11b;
  text-align: center;
}

.accessibility-item .heading {
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.3;
  text-shadow: 1px 2px 0 #0897fd;
}

.accessibility-item .description {
  color: rgba(255, 255, 255, 0.85);
  font-family: 'Geist Pixel', sans-serif;
  font-size: 0.75rem;
  font-weight: 400;
  line-height: 1.35;
  text-align: center;
}

@media (max-width: 600px) {
  .accessibility-card {
    grid-template-columns: 1fr;
    gap: 12px;
  }
}
/* SECTION 2*/
.section2 {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  padding: 64px clamp(24px, 6vw, 80px) 72px;
  background: #9addf7;
  background-image: url('../../../media/assets/CityLanding.png');
  background-size: auto 50%;
  background-position: bottom center;
  background-repeat: repeat-x;
}

.content2 {
  display: flex;
  flex-direction: column;
  gap: 0px;
  width: min(100%, 1120px);
}

.content2 .header {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  text-align: center;
}

.header .heading {
  position: static;
  flex: none;
  background: none;
  color: #fff;
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(4rem, 4.5vw, 5rem);
  font-weight: 400;
  line-height: 0.6;
  text-shadow: 3px 4px 0 #092d5d;
}

.header .description {
  flex: none;
  align-self: auto;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.3;
  text-align: center;
  text-shadow: 1px 2px 0 #092d5d;
}

.content2 > .description {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 700px) minmax(0, 1fr);
  align-items: center;
  box-sizing: border-box;
  gap: 16px;
  width: 100%;
  height: auto;
  padding: 0;
  margin: 0;
}

.content2 > .description > .center {
  display: flex;
  grid-column: 2;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 100%;
  max-width: 700px;
  min-width: 0;
  height: auto;
  margin: 0;
  padding:0;
}

.center .heading {
  flex: none;
  align-self: stretch;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.3;
  text-align: center;
  text-shadow: 1px 2px 0 #092d5d;
  text-transform: none;
}

.center .description {
  display: block;
  flex: none;
  align-self: stretch;
  color: #172036;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.4;
  text-align: center;
  white-space: pre-line;
  padding-top: 5%;
  margin-bottom: 5%
}

.card-deck {
  display: flex;
  align-items: stretch;
  gap: 24px;
  width: 100%;
  margin:0;
  padding: 0% 0 15% 0;
}

.card-item {
  box-sizing: border-box;
  display: flex;
  flex: 1 1 0;
  flex-direction: column;
  gap: 4px;
  min-width: 0;
  padding: 10px;
  background: rgba(255, 223, 1, 0.8);
}

.card-item .heading {
  width: 100%;
  height: auto;
  color: #fff;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  font-weight: 400;
  line-height: 1.3;
  text-shadow: 1px 2px 0 #092d5d;
}

.card-item .description {
  width: 100%;
  height: auto;
  color: #172036;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.4;
  text-align: justify;
}

.content2-right {
  grid-column: 3;
  align-self: center;
  width: min(240px, 100%);
  aspect-ratio: 240 / 382;
  justify-self: end;
  background-image: url('../../../media/assets/GreenCharLanding.png');
  background-position: right bottom;
  background-repeat: no-repeat;
  background-size: contain;
}

@media (max-width: 1100px) {
  .content2 > .description {
    grid-template-columns: minmax(0, 1fr);
  }

  .content2 > .description > .center,
  .content2-right {
    grid-column: 1;
  }

  .content2-right {
    justify-self: end;
  }
}

@media (max-width: 600px) {
  .section2 {
    padding: 48px 24px;
  }

  .card-deck {
    flex-direction: column;
  }
}

/* SECTION 1 */
.section1 {
  position: relative;
  isolation: isolate;
  box-sizing: border-box;
  min-height: calc(100vh - 76px);
  display: flex;
  justify-content: center;
  padding: 0 clamp(24px, 6vw, 80px);
  background: #092d5d;
  color: #fff;
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
  transform: scaleX(-1);
}

.content1 {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  gap: clamp(24px, 4vw, 48px);
  width: min(100%, 1120px);
  min-height: 550px;
  padding: 64px 0;
}

#left-align {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 36px;
  flex: 1 1 0;
  min-width: 0;
  width: min(100%, 725px);
}

#landing-heading {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0;
  width: 100%;
  container-type: inline-size;
}

#landing-heading1,
#landing-heading2 {
  font-family: 'ByteBounce', sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 0.55;
}

#landing-heading1 {
  font-size: clamp(2rem, 8vw, 6.5rem);
  letter-spacing: 0.02em;
  color: #fff;
}

#landing-heading2 {
  position: relative;
  max-width: 100%;
  font-size: clamp(2.5rem, 20cqi, 9rem);
  white-space: nowrap;
  color: #20a5fb;
  text-shadow: clamp(2px, 0.8cqi, 6px) clamp(3px, 1.1cqi, 8px) 0 #087fc4;
}

#landing-heading2::after {
  position: absolute;
  inset: 0;
  content: attr(data-text);
  color: transparent;
  background: repeating-linear-gradient(
    to bottom,
    #fff 0 4px,
    transparent 4px 14px
  );
  background-clip: text;
  -webkit-background-clip: text;
  clip-path: inset(0 0 42% 0);
  pointer-events: none;
}

#landing-description {
  max-width: 725px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.25rem;
  font-weight: 400;
  line-height: 1.3;
  color: #fff;
}

#apply-button {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 59px;
  padding: 10px 30px;
  font-family: 'Geist Pixel', sans-serif;
  font-size: 1.125rem;
  background: #fae11b;
  border: 3px solid #fae11b;
  box-shadow: 7px 7px 0 #fff;
  cursor: pointer;
  transition: transform 0.1s, box-shadow 0.1s;
}

#apply-button:hover {
    transform: translate(3px, 3px);
    box-shadow: 4px 4px 0px #FFFFFF;
}
.apply-button:focus-visible {
    outline: 3px solid #FAE11B;
    outline-offset: 3px;
}

#right-align {
  flex: 0 1 440px;
  width: min(40%, 440px);
  aspect-ratio: 4 / 5;
  background-image: url(../../../media/assets/DigitalMoversPoster.png);
  background-position: center;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}

@media (max-width: 900px) {
  .section1 {
    min-height: calc(100vh - 76px);
    min-height: calc(100dvh - 76px);
  }

  .content1 {
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 48px;
    min-height: 0;
    padding: 48px 0 56px;
  }

  #left-align {
    flex: 0 1 auto;
    width: min(100%, 725px);
    gap: 28px;
  }

  #right-align {
    flex: 0 0 auto;
    width: min(100%, 440px);
  }
}
</style>