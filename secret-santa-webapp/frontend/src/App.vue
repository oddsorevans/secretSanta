<template>
  <div class="min-h-screen py-8 px-4">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-6xl font-extrabold text-white mb-4 tracking-tight drop-shadow-md">
          🎅 Secret Santa
        </h1>
        <p class="text-white/90 text-xl font-light">The modern way to exchange gifts</p>
      </div>

      <!-- Progress Steps -->
      <div class="bg-white/80 backdrop-blur-xl rounded-3xl shadow-glass p-8 mb-8 border border-white/20">
        <div class="flex justify-between items-center mb-12 px-4">
          <StepIndicator
            v-for="(step, index) in steps"
            :key="index"
            :number="index + 1"
            :title="step"
            :active="currentStep === index"
            :completed="currentStep > index"
            :isLast="index === steps.length - 1"
          />
        </div>

        <!-- Step Content -->
        <div class="mt-8">
          <ParticipantsStep v-if="currentStep === 0" v-model:participants="participants" />

          <ExclusionsStep
            v-if="currentStep === 1"
            v-model:exclusions="exclusions"
            :participants="participants"
          />

          <EmailTemplateStep
            v-if="currentStep === 2"
            v-model:emailSubject="emailSubject"
            v-model:emailTemplate="emailTemplate"
            v-model:smtpConfig="smtpConfig"
            v-model:cardStyle="cardStyle"
            v-model:debugMode="debugMode"
            v-model:emailDebugMode="emailDebugMode"
            :participants="participants"
            :themes="themes"
          />

          <SendStep
            v-if="currentStep === 3"
            :participants="participants"
            :exclusions="exclusions"
            :emailSubject="emailSubject"
            :emailTemplate="emailTemplate"
            :smtpConfig="smtpConfig"
            :cardStyle="cardStyle"
            :debugMode="debugMode"
            :emailDebugMode="emailDebugMode"
            :themes="themes"
          />
        </div>

        <!-- Navigation Buttons -->
        <div class="flex justify-between mt-12 pt-6 border-t border-gray-100">
          <button
            v-if="currentStep > 0"
            @click="currentStep--"
            class="px-8 py-3 bg-gray-100 hover:bg-gray-200 text-gray-600 rounded-full font-semibold transition-all transform hover:-translate-y-0.5"
          >
            ← Back
          </button>
          <div v-else></div>

          <button
            v-if="currentStep < steps.length - 1"
            @click="nextStep"
            :disabled="!canProceed"
            class="px-8 py-3 bg-gradient-to-r from-modern-secondary to-modern-primary hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-full font-bold shadow-lg transition-all transform hover:-translate-y-0.5 hover:shadow-xl"
          >
            Next Step →
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios'
import StepIndicator from './components/StepIndicator.vue'
import ParticipantsStep from './components/ParticipantsStep.vue'
import ExclusionsStep from './components/ExclusionsStep.vue'
import EmailTemplateStep from './components/EmailTemplateStep.vue'
import SendStep from './components/SendStep.vue'

const steps = ['Participants', 'Exclusions', 'Email Template', 'Send']
const STORAGE_KEY = 'secret-santa-draft'
const year = new Date().getFullYear()

const defaults = {
  participants: [],
  exclusions: {},
  cardStyle: 'dossier',
  emailSubject: `Secret Santa ${year}`,
  emailTemplate: `Welcome to our Secret Santa! Thank you for participating {giver_name}!

Before I tell you who you are buying for, let me remind you of the rules:
1) $25 spending limit
2) Remember, it's a secret!
3) Gifts will be exchanged at the Christmas Party on December 26th!
4) You cannot buy for your s/o. This shouldn't happen, but if you receive your s/o please let me know so we can reroll.

Now for the big reveal! You will be purchasing for {recipient_name}! Their interests include {recipient_interests}.

Their address is: {recipient_address}

Have fun and see you soon!`,
  smtpServer: 'smtp.gmail.com',
  smtpPort: 587,
  smtpEmail: '',
}

// Restore the draft (never the password)
let saved = {}
try { saved = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {} } catch { /* no storage, use defaults */ }
const init = { ...defaults, ...saved }

const currentStep = ref(0)
const participants = ref(init.participants)
const exclusions = ref(init.exclusions)
const cardStyle = ref(init.cardStyle)
const emailSubject = ref(init.emailSubject)
const emailTemplate = ref(init.emailTemplate)
const debugMode = ref(false)
const emailDebugMode = ref(false)
const smtpConfig = ref({ server: init.smtpServer, port: init.smtpPort, email: init.smtpEmail, password: '' })
const themes = ref({})

onMounted(async () => {
  try {
    const { data } = await axios.get('/api/themes')
    themes.value = Object.fromEntries(data.map(t => [t.key, t]))
    if (!themes.value[cardStyle.value]) cardStyle.value = data[0].key
  } catch (e) {
    console.error('Could not load themes - is the backend running?', e)
  }
})

// Drop exclusions that refer to people who were removed
watch(participants, (list) => {
  const names = new Set(list.map(p => p.name))
  const pruned = {}
  for (const [giver, blocked] of Object.entries(exclusions.value)) {
    if (names.has(giver)) pruned[giver] = blocked.filter(n => names.has(n))
  }
  exclusions.value = pruned
}, { deep: true })

watch([participants, exclusions, cardStyle, emailSubject, emailTemplate, smtpConfig], () => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      participants: participants.value,
      exclusions: exclusions.value,
      cardStyle: cardStyle.value,
      emailSubject: emailSubject.value,
      emailTemplate: emailTemplate.value,
      smtpServer: smtpConfig.value.server,
      smtpPort: smtpConfig.value.port,
      smtpEmail: smtpConfig.value.email,
    }))
  } catch { /* storage unavailable */ }
}, { deep: true })

const canProceed = computed(() => {
  if (currentStep.value === 0) return participants.value.length >= 3
  if (currentStep.value === 2) {
    return debugMode.value || !!(smtpConfig.value.email && smtpConfig.value.password)
  }
  return true
})

const nextStep = () => {
  if (canProceed.value && currentStep.value < steps.length - 1) currentStep.value++
}
</script>
