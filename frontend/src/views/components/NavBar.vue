<script setup>
import { ref } from 'vue'

const open = ref(false)
const links = ['Home', 'Our Approach', 'What We Look For', 'Timeline', 'FAQs', 'Contact']

function navigateTo(link) {
    open.value = false

    if (link === 'What We Look For') {
        document.getElementById('section3')?.scrollIntoView({ behavior: 'smooth' })
    }
}
</script>

<template>
    <header class="nav-bar">
        <div id="left-align"></div>

        <div id="right-align">
            <!-- Hamburger: only visible on small screens -->
            <button
                class="menu-toggle"
                :aria-expanded="open"
                aria-controls="nav-links"
                aria-label="Toggle navigation menu"
                @click="open = !open"
            >
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </button>

            <nav id="nav-links" :class="{ open }">
                <button v-for="link in links" :key="link" class="nav-buttons" @click="navigateTo(link)">
                    {{ link }}
                </button>
            </nav>

            <button class="apply-button">APPLY</button>
        </div>
    </header>
</template>

<style>
    .nav-bar {
        position: relative;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 15px clamp(16px, 6vw, 80px);
        gap: 16px;
        background: #000000;
        z-index: 8;
    }

    #left-align {
        flex: 1 1 auto;
        min-width: 0;
    }

    #right-align {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: clamp(8px, 1.5vw, 24px);
        flex: 0 1 auto;
    }

    #nav-links {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: clamp(4px, 1.2vw, 20px);
    }

    .nav-buttons {
        font-family: 'Geist Pixel', sans-serif;
        font-weight: 400;
        font-size: clamp(14px, 1.2vw + 6px, 16px);
        line-height: 1.4;
        text-transform: capitalize;
        white-space: nowrap;
        color: #FFFFFF;
        background-color: transparent;
        border: none;
        padding: 6px 8px;
        cursor: pointer;
    }

    .nav-buttons:hover {
        color: #FAE11B;
    }

    .apply-button {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px clamp(16px, 2.5vw, 30px);
        font-family: 'Geist Pixel', sans-serif;
        font-size: clamp(14px, 1.2vw + 6px, 18px);
        font-weight: 700;
        white-space: nowrap;
        color: #000000;
        background: #FAE11B;
        border: 3px solid #FAE11B;
        box-shadow: 7px 7px 0px #FFFFFF;
        cursor: pointer;
        transition: transform 0.1s, box-shadow 0.1s;
    }

    .apply-button:hover {
        transform: translate(3px, 3px);
        box-shadow: 4px 4px 0px #FFFFFF;
    }

    .nav-buttons:focus-visible,
    .apply-button:focus-visible,
    .menu-toggle:focus-visible {
        outline: 3px solid #FAE11B;
        outline-offset: 3px;
    }

    /* Hamburger hidden by default (desktop) */
    .menu-toggle {
        display: none;
        flex-direction: column;
        justify-content: center;
        gap: 5px;
        width: 44px;
        height: 44px;
        padding: 0 10px;
        background: transparent;
        border: none;
        cursor: pointer;
    }

    .menu-toggle .bar {
        display: block;
        height: 3px;
        width: 100%;
        background: #FFFFFF;
    }

    /* Tablet: tighten spacing so all links still fit */
    @media (max-width: 1024px) {
        .nav-buttons {
            padding: 6px 4px;
        }
    }

    /* Mobile / small tablet: links slide in from the right, full screen height */
    @media (max-width: 860px) {
        .menu-toggle {
            display: flex;
        }

        #right-align {
            gap: 12px;
        }

        /* Reorder: APPLY first, then hamburger on the far right */
        .apply-button {
            order: 1;
            box-shadow: 5px 5px 0px #FFFFFF;
        }

        .menu-toggle {
            order: 2;
            /* stays above the panel so it can close it */
            position: relative;
            z-index: 2;
        }

        #nav-links {
            position: fixed;
            top: 0;
            right: 0;
            z-index: 1;
            width: min(320px, 80vw);
            height: 100vh;
            height: 100dvh;
            flex-direction: column;
            align-items: stretch;
            gap: 0;
            padding: 90px 24px 24px;
            background: #000000;
            border-left: none;
            overflow-y: auto;

            /* closed: off-screen to the right */
            transform: translateX(100%);
            visibility: hidden;
            transition: transform 0.3s ease, visibility 0s linear 0.3s;
        }

        #nav-links.open {
            transform: translateX(0);
            visibility: visible;
            transition: transform 0.3s ease, visibility 0s linear 0s;
        }

        .nav-buttons {
            text-align: left;
            font-size: 18px;
            padding: 14px 0;
            border-bottom: 1px solid #333333;
        }
    }

    /* Very small phones */
    @media (max-width: 380px) {
        .apply-button {
            padding: 8px 14px;
            font-size: 14px;
        }
    }
</style>