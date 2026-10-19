<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const activeTabIndex = ref(0)
const tabNames = ['Requirements', 'Proposal', 'Mid-Project Journey', 'Funding']

const faqData = ref([
  {
    category: 'APPLICATION REQUIREMENTS',
    items: [
      {
        question: 'What are the basic requirements?',
        answer:
          'Youth-led: A Filipino group whose members are primarily 15-24 years old. Dedicated Project Team: Can designate at least 3 to 5 members and/or leaders for the duration of the program. Proven Experience: The group or the individuals involved must have experience and a proven track record based on the impact created in running local projects or campaigns.',
        isOpen: false,
      },
      {
        question: 'What are the selection criteria?',
        answer:
          '1. Youth Ownership & Team Dynamic: Truly youth-led with stable, committed core membership that cares for its community. 2. Openness to learn: Willingness to engage fully in a 9-month journey. 3. Strategic Issue Alignment: A clear, feasible plan aligned with human rights focus areas indicated by the organizers. 4. Creative Tech Integration: Technology should be part of your project proposal, either as part of the issue you are trying to address or as part of your proposed solution. 5. Equity & Inclusion: Priority is given to under-resourced and under-represented youth organizations/collectives.',
        isOpen: false,
      },
      {
        question: 'What is a truly youth-led group?',
        answer:
          'Those with committed leadership and a membership base aged 15-24. Their primary decision-makers must also be primarily composed of young people.',
        isOpen: false,
      },
      {
        question: "Who is considered a 'youth delegate'?",
        answer:
          'Each applying group must nominate 3 to 5 youth leaders between 15 and 24 years old who will serve as official delegates. These delegates will represent the organization in all online learning sessions, the in-person Youth Ideathon, mentorship calls, and campaign coordination.',
        isOpen: false,
      },
      {
        question: 'Can we apply if we formed our collective specifically for this project?',
        answer:
          'Yes, but your delegates must demonstrate prior experience in handling youth-led initiatives in the past.',
        isOpen: false,
      },
      {
        question: 'Can we apply if we are NOT Amnesty members?',
        answer: 'YES. Non-Amnesty members are welcome to apply.',
        isOpen: false,
      },
      {
        question: 'Can we apply if we are Amnesty members?',
        answer:
          'Amnesty student or local groups are not permitted to apply. HOWEVER, if you are an individual Amnesty member, you may apply representing a non-Amnesty youth organization. Please note that being formally affiliated with Amnesty DOES NOT affect your chances of getting accepted, whether positively or negatively. All applicants will be screened according to the selection criteria established by the organizers.',
        isOpen: false,
      },
      {
        question: 'Do we need to be legally registered to be able to apply?',
        answer:
          'NO. Legal registration is not required. You do not need SEC, NYP, YORP, or any other government accreditation to apply for Digital Movers. Unregistered youth organizations, youth collectives, student networks, and community-based youth groups are fully eligible.',
        isOpen: false,
      },
      {
        question: 'How do we apply?',
        answer: 'Applications must be submitted online through our official application form.',
        isOpen: false,
      },
      {
        question: 'Can we submit applications via email?',
        answer:
          'NO. Applications sent via email or direct message will not be entertained. All submissions must go through the official portal.',
        isOpen: false,
      },
      {
        question: 'Can we use Al during the application?',
        answer:
          'NO. To ensure a fair process for all candidates, use of Al Tools (such as ChatGPT or other LLMs) is strictly prohibited. We do not want perfection; we want diverse voices. Express your thoughts in your own words using the language that is most comfortable for you. Submissions that do not follow these guidelines will be disqualified.',
        isOpen: false,
      },
    ],
  },
  {
    category: 'PROJECT PROPOSAL',
    items: [
      {
        question: 'What project formats are accepted?',
        answer:
          'Projects can take the form of an advocacy campaign or a Human Rights Education (HRE) initiative. They can be online, in-person, or hybrid.',
        isOpen: false,
      },
      {
        question: 'Can we submit an existing project, or must it be brand new?',
        answer:
          'Both are welcome! You can submit a completely new project idea or a new phase/extension of an ongoing initiative, provided it meets the core criteria and timeline.',
        isOpen: false,
      },
      {
        question: 'What themes should our focus issue align with?',
        answer:
          "Project proposals should be within the following themes and must have a tech element: Civic Engagement & Youth Activism: Protest safety for youth activists, digital rights, digital security, anti red-tagging/harassment. Freedom of Expression & Press Freedom: Campus journalism, youth media literacy, anti-disinformation. Climate Justice: Youth climate action, environmental defenders, climate education. Indigenous People's Rights: IP youth-led ancestral domain protection, cultural/heritage protection. Anti-Discrimination & Inclusion: Promotion of SOGIESC, gender equality, disability rights. Sexual and Reproductive Health and Rights: Anti-tech-facilitated gender-based violence, SRHR education.",
        isOpen: false,
      },
      {
        question: 'What does the "Tech Element" requirement mean?',
        answer:
          'Your project proposal must integrate technology in one of two ways: 1. Addressing a digital rights issue (e.g., online harassment, data privacy, tech-facilitated violence, digital surveillance), OR 2. Using digital technology or platforms to address a human rights issue.',
        isOpen: false,
      },
    ],
  },
  {
    category: 'MID-PROJECT JOURNEY',
    items: [
      {
        question: 'What is the required time commitment?',
        answer:
          'Delegates should be prepared to commit approximately 6 to 8 hours per week on a voluntary basis from December 2026 to August 2027. Your active participation in all scheduled sessions and milestone deliverables is required so you can be ready for the launch in May 2027.',
        isOpen: false,
      },
      {
        question: 'Can our organization switch delegates midway through the program?',
        answer:
          'No. To preserve team safety and learning continuity, swapping delegates is not allowed. If a representative must leave the project for personal reasons, your organization may internally reassign tasks to another member, but that member will not participate officially in Digital Movers activities or receive program allowances.',
        isOpen: false,
      },
      {
        question: 'Does our campaign have to end when the program finishes in August 2027?',
        answer:
          'NO. The grant implementation covered under Digital Movers will run from May to July 2027. However, your organization is strongly encouraged to continue, adapt, and scale the project beyond graduation.',
        isOpen: false,
      },
      {
        question: 'What happens at the January Youth Ideathon?',
        answer:
          'The Level 2 Youth Ideathon runs from January 21-26, 2027 (inclusive of travel dates). All 6 finalist groups are required to attend the Youth Ideathon in person. AIPH will cover all air and land travel, lodging, meals, and incidentals in full.',
        isOpen: false,
      },
      {
        question: 'Where will the Youth Ideathon be held?',
        answer:
          'The Youth Ideathon venue will be assigned once the Top 6 have been selected. We want the location to be accessible to the delegates as much as possible.',
        isOpen: false,
      },
      {
        question: 'When do we pitch our project proposal?',
        answer:
          'Final project proposals will be pitched on the last day of the Youth Ideathon. Each group will be asked to pitch their final proposals to a panel from AIPH.',
        isOpen: false,
      },
    ],
  },
  {
    category: 'FUNDING, ALLOWANCES, & FINANCIAL MANAGEMENT',
    items: [
      {
        question: 'How much seed funding is available?',
        answer:
          'The Top 3 awardee groups will be granted up to Php 200,000.00 each to execute their 3-month project from May to July 2027.',
        isOpen: false,
      },
      {
        question: 'What if Php 200,000.00 is too large for our project scope?',
        answer:
          'Php 200,000.00 is the maximum accessible fund, but it is not a mandatory spend. Groups are encouraged to request a budget that realistically fits their capacity and campaign plan. Budget proposals will be refined and settled during the Youth Ideathon before any MOU and contract are signed.',
        isOpen: false,
      },
      {
        question: 'How are the seed grant funds managed and disbursed?',
        answer:
          "Grants will be disbursed in tranches, either through the group's bank account or that of their representative. Use and liquidation of approved project funds will follow AIPH guidelines.",
        isOpen: false,
      },
      {
        question: 'Do delegates receive allowances?',
        answer:
          'Level 1 (OLS): No monthly allowance will be provided at this level. Level 2 (Youth Ideathon): All Youth Ideathon-related expenses (travel, accommodation, and meals) are fully covered by AIPH. Level 3 to Level 4 (Feb-Aug 2027): Each individual youth delegate of the Top 3 groups/organizations/collectives will receive a monthly communications allowance of Php 2,500.00 to cover connectivity and local logistics.',
        isOpen: false,
      },
      {
        question: 'What if our organization is not selected as part of the Top 3?',
        answer:
          'For those not selected as one of the Top 3 groups, a solidarity stipend of Php 10,000 will be provided to cover their expenses for participating in the Youth Ideathon.',
        isOpen: false,
      },
      {
        question: 'Does our group need prior experience managing grants?',
        answer:
          'Not at all. You do not need grant writing or financial management experience to apply. We will guide your team through building a realistic project budget during the Youth Ideathon. A finalized budget will be required before seed funding is awarded, but we provide the mentorship to help you get there.',
        isOpen: false,
      },
    ],
  },
])

const toggleAccordion = (item) => {
  item.isOpen = !item.isOpen
}
</script>

<template>
  <NavBar />
  <div class="page-container">
    <!-- Decorative Clouds -->
    <img src="../../media/assets/cloud-1.png" class="cloud cloud-tl" alt="cloud" />
    <img src="../../media/assets/cloud-3.png" class="cloud cloud-tr" alt="cloud" />
    <img src="../../media/assets/cloud-3.png" class="cloud cloud-bl" alt="cloud" />

    <div class="content-wrapper">
      <h1 class="page-title">Frequently<br />Asked Questions</h1>

      <div class="faq-board">
        <!-- Layered Backgrounds for the pixel shadow effect -->
        <img src="../../media/assets/faqs-bg-darkblue.png" class="bg-layer shadow-layer" alt="" />
        <img src="../../media/assets/faqs-bg-yellow.png" class="bg-layer yellow-layer" alt="" />

        <!-- Interactive Board Content -->
        <div class="board-inner">
          <!-- Interactive HTML/CSS Tabs replacing the static image -->
          <div class="tabs-container">
            <button
              v-for="(tab, index) in tabNames"
              :key="index"
              class="faq-tab"
              :class="{ active: activeTabIndex === index }"
              @click="activeTabIndex = index"
            >
              {{ tab }}
            </button>
          </div>

          <div class="blue-container">
            <img src="../../media/assets/faqs-bg-blue.png" class="bg-layer blue-layer" alt="" />

            <div class="questions-list">
              <!-- Dynamically render the items array from the selected index -->
              <div v-for="(item, i) in faqData[activeTabIndex].items" :key="i" class="faq-item">
                <button class="accordion-button" @click="toggleAccordion(item)">
                  <h3>{{ item.question.toUpperCase() }}</h3>
                  <span class="accordion-icon">{{ item.isOpen ? '−' : '+' }}</span>
                </button>

                <div class="accordion-content" v-show="item.isOpen">
                  <p>{{ item.answer }}</p>
                </div>
              </div>
            </div>
          </div>
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
  display: flex;
  justify-content: center;
  padding: 40px clamp(16px, 4vw, 40px) 100px;
  background: linear-gradient(180deg, #ffffff 0%, #d8f0ff 30%, #44aaf9 100%);
  overflow: hidden;
}

.cloud {
  position: absolute;
  z-index: 1;
  image-rendering: pixelated;
  opacity: 0.9;
}
.cloud-tl {
  top: 50px;
  left: 20px;
  width: clamp(120px, 15vw, 200px);
}
.cloud-tr {
  top: 250px;
  right: 20px;
  width: clamp(80px, 10vw, 150px);
}
.cloud-bl {
  bottom: 80px;
  left: 20px;
  width: clamp(100px, 12vw, 180px);
}

.content-wrapper {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  width: min(100%, 800px);
}

.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(2rem, 3vw, 2rem);
  color: #11335f;
  margin: 0 0 1rem 0;
  text-align: center;
  line-height: 1.2;
  letter-spacing: 2px;
  text-transform: uppercase;
}

.faq-board {
  position: relative;
  width: 100%;
  margin-top: 10px;
}
.bg-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: fill;
  image-rendering: pixelated;
}
.shadow-layer {
  top: 12px;
  left: 12px;
  z-index: 1;
}
.yellow-layer {
  top: 0;
  left: 0;
  z-index: 2;
}

.board-inner {
  position: relative;
  z-index: 3;
  padding: 16px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* CSS implementation of the pixel tabs */
.tabs-container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 6px;
  width: 100%;
  margin-bottom: -4px;
  position: relative;
  z-index: 4;
  padding-left: 12px;
}

.faq-tab {
  background-color: #0b2f5c; /* Dark blue for inactive tabs */
  color: #ffffff;
  border: none;
  font-family: 'Geist Pixel', 'ByteBounce', sans-serif;
  font-size: clamp(1.5rem, 2.5vw, 1.5rem);
  font-weight: bold;
  padding: 12px 20px 16px 20px;
  cursor: pointer;
  /* Simulating pixel corners with clip-path */
  clip-path: polygon(6px 0, calc(100% - 6px) 0, 100% 6px, 100% 100%, 0 100%, 0 6px);
  transition: background-color 0.2s;
  letter-spacing: 0.5px;
}

.faq-tab.active {
  background-color: #2ea5fa; /* Matches the faqs-bg-blue background */
  color: #ffffff;
}

.blue-container {
  position: relative;
  width: 100%;
  box-sizing: border-box;
  min-height: 300px;
  padding: 16px;
  margin-top: -2px;
}
.blue-layer {
  top: 0;
  left: 0;
  z-index: 1;
  border-radius: 4px;
}

.questions-list {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.faq-item {
  background-color: #ffffff;
  border-radius: 4px;
  padding: 2px 16px;
  box-shadow: inset 0 -2px 0 rgba(0, 0, 0, 0.05);
}

.accordion-button {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  background: transparent;
  border: none;
  padding: 12px 0;
  cursor: pointer;
  text-align: left;
}

.faq-item h3 {
  font-family: 'Geist Pixel', 'ByteBounce', sans-serif;
  font-size: clamp(1.5em, 2.2vw, 1.4rem);
  color: #11335f;
  margin: 0;
  line-height: 1.3;
  padding-right: 1rem;
  font-weight: 700;
  letter-spacing: 0.5px;
}

.accordion-icon {
  font-size: 1.5rem;
  color: #20a5fb;
  font-weight: bold;
}

.accordion-content {
  padding-bottom: 1rem;
}

.faq-item p {
  font-family: 'Geist Pixel', sans-serif;
  line-height: 1.5;
  color: #333;
  font-size: 1.5rem;
  margin: 0;
}
</style>
