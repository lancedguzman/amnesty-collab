<script setup>
import { ref } from 'vue'
import NavBar from './components/NavBar.vue'

const faqData = ref([
  {
    category: 'APPLICATION REQUIREMENTS',
    items: [
      {
        question: 'What are the basic requirements?',
        answer:
          'Youth-led: A Filipino group whose members are primarily 15-24 years old. Dedicated Project Team: Can designate at least 3 to 5 members and/or leaders for the duration of the program. Proven Experience: The group or the individuals involved must have experience and a proven track record based on the impact created in running local projects or campaigns.',
      },
      {
        question: 'What are the selection criteria?',
        answer:
          '1. Youth Ownership & Team Dynamic: Truly youth-led with stable, committed core membership that cares for its community. 2. Openness to learn: Willingness to engage fully in a 9-month journey. 3. Strategic Issue Alignment: A clear, feasible plan aligned with human rights focus areas indicated by the organizers. 4. Creative Tech Integration: Technology should be part of your project proposal, either as part of the issue you are trying to address or as part of your proposed solution. 5. Equity & Inclusion: Priority is given to under-resourced and under-represented youth organizations/collectives.',
      },
      {
        question: 'What is a truly youth-led group?',
        answer:
          'Those with committed leadership and a membership base aged 15-24. Their primary decision-makers must also be primarily composed of young people.',
      },
      {
        question: "Who is considered a 'youth delegate'?",
        answer:
          'Each applying group must nominate 3 to 5 youth leaders between 15 and 24 years old who will serve as official delegates. These delegates will represent the organization in all online learning sessions, the in-person Youth Ideathon, mentorship calls, and campaign coordination.',
      },
      {
        question: 'Can we apply if we formed our collective specifically for this project?',
        answer:
          'Yes, but your delegates must demonstrate prior experience in handling youth-led initiatives in the past.',
      },
      {
        question: 'Can we apply if we are NOT Amnesty members?',
        answer: 'YES. Non-Amnesty members are welcome to apply.',
      },
      {
        question: 'Can we apply if we are Amnesty members?',
        answer:
          'Amnesty student or local groups are not permitted to apply. HOWEVER, if you are an individual Amnesty member, you may apply representing a non-Amnesty youth organization. Please note that being formally affiliated with Amnesty DOES NOT affect your chances of getting accepted, whether positively or negatively. All applicants will be screened according to the selection criteria established by the organizers.',
      },
      {
        question: 'Do we need to be legally registered to be able to apply?',
        answer:
          'NO. Legal registration is not required. You do not need SEC, NYP, YORP, or any other government accreditation to apply for Digital Movers. Unregistered youth organizations, youth collectives, student networks, and community-based youth groups are fully eligible.',
      },
      {
        question: 'How do we apply?',
        answer: 'Applications must be submitted online through our official application form.',
      },
      {
        question: 'Can we submit applications via email?',
        answer:
          'NO. Applications sent via email or direct message will not be entertained. All submissions must go through the official portal.',
      },
      {
        question: 'Can we use Al during the application?',
        answer:
          'NO. To ensure a fair process for all candidates, use of Al Tools (such as ChatGPT or other LLMs) is strictly prohibited. We do not want perfection; we want diverse voices. Express your thoughts in your own words using the language that is most comfortable for you. Submissions that do not follow these guidelines will be disqualified.',
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
      },
      {
        question: 'Can we submit an existing project, or must it be brand new?',
        answer:
          'Both are welcome! You can submit a completely new project idea or a new phase/extension of an ongoing initiative, provided it meets the core criteria and timeline.',
      },
      {
        question: 'What themes should our focus issue align with?',
        answer:
          "Project proposals should be within the following themes and must have a tech element: Civic Engagement & Youth Activism, Freedom of Expression & Press Freedom, Climate Justice, Indigenous People's Rights, Anti-Discrimination & Inclusion, and Sexual and Reproductive Health and Rights.",
      },
      {
        question: "What does the 'Tech Element' requirement mean?",
        answer:
          'Your project proposal must integrate technology in one of two ways: 1. Addressing a digital rights issue (e.g., online harassment, data privacy, tech-facilitated violence, digital surveillance), OR 2. Using digital technology or platforms to address a human rights issue.',
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
      },
      {
        question: 'Can our organization switch delegates midway through the program?',
        answer:
          'No. To preserve team safety and learning continuity, swapping delegates is not allowed. If a representative must leave the project for personal reasons, your organization may internally reassign tasks to another member, but that member will not participate officially in Digital Movers activities or receive program allowances.',
      },
      {
        question: 'Does our campaign have to end when the program finishes in August 2027?',
        answer:
          'NO. The grant implementation covered under Digital Movers will run from May to July 2027. However, your organization is strongly encouraged to continue, adapt, and scale the project beyond graduation.',
      },
      {
        question: 'What happens at the January Youth Ideathon?',
        answer:
          'The Level 2 Youth Ideathon runs from January 21-26, 2027 (inclusive of travel dates). All 6 finalist groups are required to attend the Youth Ideathon in person. AIPH will cover all air and land travel, lodging, meals, and incidentals in full.',
      },
      {
        question: 'Where will the Youth Ideathon be held?',
        answer:
          'The Youth Ideathon venue will be assigned once the Top 6 have been selected. We want the location to be accessible to the delegates as much as possible.',
      },
      {
        question: 'When do we pitch our project proposal?',
        answer:
          'Final project proposals will be pitched on the last day of the Youth Ideathon. Each group will be asked to pitch their final proposals to a panel from AIPH.',
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
      },
      {
        question: 'What if Php 200,000.00 is too large for our project scope?',
        answer:
          'Php 200,000.00 is the maximum accessible fund, but it is not a mandatory spend. Groups are encouraged to request a budget that realistically fits their capacity and campaign plan. Budget proposals will be refined and settled during the Youth Ideathon before any MOU and contract are signed.',
      },
      {
        question: 'How are the seed grant funds managed and disbursed?',
        answer:
          "Grants will be disbursed in tranches, either through the group's bank account or that of their representative. Use and liquidation of approved project funds will follow AIPH guidelines.",
      },
      {
        question: 'Do delegates receive allowances?',
        answer:
          'Level 1 (OLS): No monthly allowance will be provided at this level. Level 2 (Youth Ideathon): All Youth Ideathon-related expenses (travel, accommodation, and meals) are fully covered by AIPH. Level 3 to Level 4 (Feb-Aug 2027): Each individual youth delegate of the Top 3 groups/organizations/collectives will receive a monthly communications allowance of Php 2,500.00 to cover connectivity and local logistics.',
      },
      {
        question: 'What if our organization is not selected as part of the Top 3?',
        answer:
          'For those not selected as one of the Top 3 groups, a solidarity stipend of Php 10,000 will be provided to cover their expenses for participating in the Youth Ideathon.',
      },
      {
        question: 'Does our group need prior experience managing grants?',
        answer:
          'Not at all. You do not need grant writing or financial management experience to apply. We will guide your team through building a realistic project budget during the Youth Ideathon. A finalized budget will be required before seed funding is awarded, but we provide the mentorship to help you get there.',
      },
    ],
  },
  {
    category: 'HAVE MORE QUESTIONS?',
    items: [
      {
        question: 'Where can we send additional inquiries?',
        answer:
          'For any inquiries not addressed in this guide, please email the Amnesty International Philippines youth team at cydphilippines@amnesty.org.ph.',
      },
    ],
  },
])
</script>

<template>
  <NavBar />
  <div class="page-container">
    <div class="content-wrapper">
      <h1 class="page-title">Frequently Asked Questions</h1>

      <div class="faq-container">
        <div v-for="(section, index) in faqData" :key="index" class="faq-section">
          <h2 class="yellow-heading">{{ section.category }}</h2>
          <div v-for="(item, i) in section.items" :key="i" class="faq-item">
            <h3>{{ item.question }}</h3>
            <p>{{ item.answer }}</p>
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
  width: min(100%, 900px);
}
.page-title {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(4rem, 4.5vw, 5rem);
  color: #fff;
  text-shadow: 3px 4px 0 #20a5fb;
  margin: 0 0 2rem 0;
  text-align: center;
  line-height: 0.8;
}
.faq-container {
  width: 100%;
}
.faq-section {
  margin-bottom: 3rem;
  background: #063c70;
  border: 4px solid #fff;
  padding: 2rem;
}
.yellow-heading {
  font-family: 'ByteBounce', sans-serif;
  font-size: clamp(2.5rem, 3.5vw, 3.5rem);
  color: #fae11b;
  text-shadow: 0 0 10px #fae11b;
  margin: 0 0 1.5rem 0;
  line-height: 0.8;
  border-bottom: 2px solid #20a5fb;
  padding-bottom: 1rem;
}
.faq-item {
  margin-bottom: 1.5rem;
  font-family: 'Geist Pixel', sans-serif;
}
.faq-item h3 {
  font-size: 1.25rem;
  color: #fae11b;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}
.faq-item p {
  line-height: 1.5;
  color: #fff;
  font-size: 1.125rem;
  margin: 0;
}
</style>
