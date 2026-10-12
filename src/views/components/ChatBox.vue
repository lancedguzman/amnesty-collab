<template>
    <button
        id="chat-box-button"
        type="button"
        aria-label="Open chat"
        aria-haspopup="dialog"
        @click="openChat"
    >
        ?
    </button>
    <dialog
        v-if="isOpen"
        ref="chatDialog"
        class="chat-dialog"
        aria-labelledby="chat-dialog-title"
        @click.self="closeChat"
        @close="isOpen = false"
    >
        <header class="chat-dialog-header">
            <h2 id="chat-dialog-title">Chat support</h2>
            <button class="chat-close" type="button" aria-label="Close chat" @click="closeChat">
                &times;
            </button>
        </header>

        <p class="chat-intro">What would you like help with?</p>
        <section v-if="conversation.length" class="conversation" aria-label="Conversation" aria-live="polite">
            <div
                v-for="message in conversation"
                :key="message.id"
                class="conversation-message"
                :class="`conversation-message--${message.role}`"
            >
                {{ message.text }}
            </div>
        </section>
        <div class="chat-options">
            <button
                class="chat-option"
                v-for="option in chatOptions"
                :key="option.label"
                type="button"
                @click="send(option)"
            >
                <span>{{ option.label }}</span>
                <span class="chat-option-arrow" aria-hidden="true">&rarr;</span>
            </button>
        </div>
    </dialog>
</template>

<script setup>
import { nextTick, ref } from 'vue'

const isOpen = ref(false)
const chatDialog = ref(null)
const chatOptions = [
    {
        label: 'General question',
        reply: 'Thanks for reaching out. Tell us a little more about your question and we’ll do our best to help.'
    },
    {
        label: 'Technical support',
        reply: 'We can help with technical issues. Describe what happened, what you expected, and any error message you saw.'
    }
]
const conversation = ref([])
let nextMessageId = 0

async function openChat() {
    isOpen.value = true
    await nextTick()
    chatDialog.value?.showModal()
}

function closeChat() {
    chatDialog.value?.close()
    isOpen.value = false
}

function send(option) {
    conversation.value.push(
        { id: nextMessageId++, role: 'user', text: option.label },
        { id: nextMessageId++, role: 'assistant', text: option.reply }
    )
}
</script>

<style>
#chat-box-button {
    position: fixed;
    right: max(1rem, env(safe-area-inset-right, 0px));
    bottom: max(1rem, env(safe-area-inset-bottom, 0px));
    z-index: 1000;
    width: clamp(3.25rem, 12vw, 4rem);
    height: clamp(3.25rem, 12vw, 4rem);
    padding: 0;
    border: 0.35rem solid #000;
    border-radius: 5%;
    background-color: #fae11b;
    color: white;
    cursor: pointer;
    box-shadow: 4px 4px 0 #000000;
    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
    
    font-family: 'Geist Pixel', sans-serif;
    font-size: clamp(1.5rem, 4vw, 2rem);
    text-shadow: 
        1.6px  1.6px 0 #000,
        -1.6px -1.6px 0 #000,  
        1.6px -1.6px 0 #000,
        -1.6px  1.6px 0 #000;
}

#chat-box-button:hover {
    transform: translateY(-3px);
    box-shadow: 6px 7px 0 #000000;
    text-shadow: 
        1.6px  1.6px 0 #000,
        -1.6px -1.6px 0 #000,  
        1.6px -1.6px 0 #000,
        -1.6px  1.6px 0 #000;
}

#chat-box-button:focus-visible,
.chat-close:focus-visible,
.chat-option:focus-visible {
    outline: 3px solid #20a5fb;
    outline-offset: 3px;
}

.chat-dialog {
    position: fixed;
    inset: auto max(1rem, env(safe-area-inset-right, 0px))
        calc(clamp(3.25rem, 12vw, 4rem) + 1.5rem + env(safe-area-inset-bottom, 0px)) auto;
    box-sizing: border-box;
    width: min(
        24rem,
        calc(100vw - 2rem - env(safe-area-inset-left, 0px) - env(safe-area-inset-right, 0px))
    );
    max-height: 50vh;
    max-height: min(
        50dvh,
        calc(100dvh - clamp(3.25rem, 12vw, 4rem) - 2.5rem - env(safe-area-inset-bottom, 0px))
    );
    overflow-y: auto;
    overscroll-behavior: contain;
    margin: 0;
    padding: clamp(0.75rem, 4vw, 1.5rem);
    border: 3px solid #000000;
    border-radius: 1rem;
    background: rgb(255 255 255 / 95%);
    color: #092d5d;
    font-family: 'Geist Pixel', sans-serif;
}
.chat-dialog-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
}

.chat-dialog-header h2 {
    margin: 0;
    font-family: 'ByteBounce', sans-serif;
    font-size: clamp(0.8rem, 6vw, 1rem);
    line-height: 1.2;
}

.chat-eyebrow {
    color: #1767a7;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
}

.chat-close {
    display: grid;
    width: clamp(2rem, 10vw, 2.25rem);
    height: clamp(2rem, 10vw, 2.25rem);
    padding: 0;
    flex: 0 0 auto;
    place-items: center;
    border: 2px solid #092d5d;
    border-radius: 50%;
    background: #fff;
    color: #092d5d;
    font-size: 1.5rem;
    line-height: 1;
    cursor: pointer;
    transition:
        background-color 0.2s ease,
        color 0.2s ease;
}

.chat-close:hover {
    background: #092d5d;
    color: #fff;
}

.chat-intro {
    margin: 0rem 0 0.75rem;
    font-size: 0.95rem;
}

.conversation {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.conversation-message {
    max-width: 90%;
    padding: 0.65rem 0.8rem;
    border: 1px solid #092d5d;
    border-radius: 0.6rem;
    overflow-wrap: anywhere;
    line-height: 1.4;
}

.conversation-message--user {
    align-self: flex-end;
    background: #fff8c7;
}

.conversation-message--assistant {
    align-self: flex-start;
    background: #f1f7fc;
}

.chat-options {
    display: flex;
    flex-direction: column;
    gap: 0.65rem;
}

.chat-option {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    width: 100%;
    padding: 0.65rem clamp(0.65rem, 4vw, 1rem);
    border: 2px solid #092d5d;
    border-radius: 0.6rem;
    background: #fff;
    color: #092d5d;
    font: inherit;
    text-align: left;
    cursor: pointer;
    transition:
        transform 0.2s ease,
        background-color 0.2s ease,
        box-shadow 0.2s ease;
}

.chat-option:hover {
    transform: translate(-2px, -2px);
    background: #fff8c7;
    box-shadow: 3px 3px 0 #092d5d;
}

.chat-option-arrow {
    color: #1767a7;
    font-size: 1.25rem;
}

.chat-note span {
    width: 0.55rem;
    height: 0.55rem;
    border-radius: 50%;
    background: #31a36a;
}

@media (prefers-reduced-motion: reduce) {
    #chat-box-button,
    .chat-close,
    .chat-option {
        transition: none;
    }
}
</style>