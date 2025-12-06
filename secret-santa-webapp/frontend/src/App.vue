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
          <ParticipantsStep
            v-if="currentStep === 0"
            :participants="participants"
            @update:participants="participants = $event"
          />

          <ExclusionsStep
            v-if="currentStep === 1"
            :participants="participants"
            :exclusions="exclusions"
            @update:exclusions="exclusions = $event"
          />

          <EmailTemplateStep
            v-if="currentStep === 2"
            :emailSubject="emailSubject"
            :emailTemplate="emailTemplate"
            :smtpConfig="smtpConfig"
            :participants="participants"
            :cardStyle="cardStyle"
            :debugMode="debugMode"
            :emailDebugMode="emailDebugMode"
            @update:emailSubject="emailSubject = $event"
            @update:emailTemplate="emailTemplate = $event"
            @update:smtpConfig="smtpConfig = $event"
            @update:cardStyle="cardStyle = $event"
            @update:debugMode="debugMode = $event"
            @update:emailDebugMode="emailDebugMode = $event"
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
import { ref, computed } from 'vue'
import StepIndicator from './components/StepIndicator.vue'
import ParticipantsStep from './components/ParticipantsStep.vue'
import ExclusionsStep from './components/ExclusionsStep.vue'
import EmailTemplateStep from './components/EmailTemplateStep.vue'
import SendStep from './components/SendStep.vue'

const steps = ['Participants', 'Exclusions', 'Email Template', 'Send']
const currentStep = ref(0)

const participants = ref([])
const exclusions = ref({})
const cardStyle = ref('classic')
const debugMode = ref(false)
const emailDebugMode = ref(false)
const emailSubject = ref('Friends Secret Santa 2024')
const emailTemplate = ref(`Welcome to our 3rd Annual Secret Santa! Thank you for participating {giver_name}!

Before I tell you who you are buying for, let me remind you of the rules:
1) $25 spending limit
2) Remember, it's a secret!
3) These will be given out at the Christmas Party on December 26th!
4) You cannot buy for your s/o. This shouldn't happen, but if you receive your s/o please let me know so we can reroll.

Now for the big reveal! You will be purchasing for {recipient_name}! Their interests include {recipient_interests}.

Their address is: {recipient_address}

Have fun and see you soon!`)

const smtpConfig = ref({
  server: 'smtp.gmail.com',
  port: 587,
  email: '',
  password: ''
})

const canProceed = computed(() => {
  if (currentStep.value === 0) {
    return participants.value.length >= 3
  }
  if (currentStep.value === 2) {
    // Only require SMTP config if NOT in debug mode
    if (debugMode.value) {
      return true
    }
    return smtpConfig.value.email && smtpConfig.value.password
  }
  return true
})

const nextStep = () => {
  if (canProceed.value && currentStep.value < steps.length - 1) {
    currentStep.value++
  }
}
</script>
