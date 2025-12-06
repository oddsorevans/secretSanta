<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-2">Email Template & Card Style</h2>
    <p class="text-gray-500 mb-8 text-lg">Choose a card style and customize your Secret Santa message.</p>

    <!-- Mode Selection -->
    <div class="mb-8 p-8 bg-gradient-to-br from-purple-50 to-blue-50 border-2 border-purple-100 rounded-2xl">
      <h3 class="font-bold text-gray-800 mb-6 text-lg">Choose Mode</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <button
          @click="localDebugMode = false"
          class="p-6 border-2 rounded-2xl transition-all text-left group relative overflow-hidden"
          :class="!localDebugMode
            ? 'border-modern-secondary bg-white shadow-lg scale-[1.02] ring-2 ring-modern-secondary/20'
            : 'border-gray-200 hover:border-modern-secondary/50 bg-white/50'"
        >
          <div class="relative z-10">
            <div class="flex items-center mb-3">
              <div class="w-10 h-10 rounded-full flex items-center justify-center text-xl mr-3" :class="!localDebugMode ? 'bg-modern-secondary text-white' : 'bg-gray-100 text-gray-500'">📧</div>
              <h4 class="font-bold text-lg text-gray-800">Send Real Emails</h4>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">
              Send actual Secret Santa emails to all participants. Pairings will remain secret!
            </p>
          </div>
          <div v-if="!localDebugMode" class="absolute top-4 right-4 text-modern-secondary">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
        </button>

        <button
          @click="localDebugMode = true"
          class="p-6 border-2 rounded-2xl transition-all text-left group relative overflow-hidden"
          :class="localDebugMode
            ? 'border-modern-primary bg-white shadow-lg scale-[1.02] ring-2 ring-modern-primary/20'
            : 'border-gray-200 hover:border-modern-primary/50 bg-white/50'"
        >
          <div class="relative z-10">
            <div class="flex items-center mb-3">
              <div class="w-10 h-10 rounded-full flex items-center justify-center text-xl mr-3" :class="localDebugMode ? 'bg-modern-primary text-white' : 'bg-gray-100 text-gray-500'">🔍</div>
              <h4 class="font-bold text-lg text-gray-800">Debug Mode</h4>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">
              Test pairings and preview cards without sending. Perfect for testing!
            </p>
          </div>
          <div v-if="localDebugMode" class="absolute top-4 right-4 text-modern-primary">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
        </button>
      </div>

      <div v-if="localDebugMode" class="mt-6 p-4 bg-purple-100/50 border border-purple-200 rounded-xl flex items-start gap-3">
        <span class="text-purple-600 text-xl">💡</span>
        <p class="text-sm text-purple-800 font-medium pt-0.5">
          <strong>Debug Mode:</strong> No SMTP configuration needed. You'll be able to view all pairings and preview cards on the next step.
        </p>
      </div>
      <div v-else class="mt-6 p-4 bg-blue-100/50 border border-blue-200 rounded-xl flex items-start gap-3">
        <span class="text-blue-600 text-xl">ℹ️</span>
        <p class="text-sm text-blue-800 font-medium pt-0.5">
          <strong>Real Send Mode:</strong> SMTP configuration required below. Emails will be sent to all participants.
        </p>
      </div>
    </div>

    <!-- SMTP Configuration (only shown if NOT debug mode) -->
    <div v-if="!localDebugMode" class="mb-8 p-8 bg-gray-50 rounded-2xl border border-gray-100">
      <h3 class="font-bold text-gray-800 mb-6 text-lg">Email Configuration</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">SMTP Server</label>
          <input
            v-model="localSmtpConfig.server"
            type="text"
            placeholder="smtp.gmail.com"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">Port</label>
          <input
            v-model.number="localSmtpConfig.port"
            type="number"
            placeholder="587"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">Your Email</label>
          <input
            v-model="localSmtpConfig.email"
            type="email"
            placeholder="your.email@gmail.com"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">App Password</label>
          <input
            v-model="localSmtpConfig.password"
            type="password"
            placeholder="App-specific password"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
      </div>
      <p class="text-xs text-gray-500 mt-4 font-medium flex items-center gap-1">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        For Gmail, use an App Password: Google Account → Security → 2-Step Verification → App passwords
      </p>

      <!-- Email Debug Mode Toggle -->
      <div class="mt-6 p-5 bg-amber-50 border-2 border-amber-200 rounded-xl">
        <label class="flex items-start gap-3 cursor-pointer group">
          <input
            v-model="localEmailDebugMode"
            type="checkbox"
            class="mt-1 w-5 h-5 text-amber-600 border-amber-300 rounded focus:ring-2 focus:ring-amber-500 cursor-pointer"
          />
          <div class="flex-1">
            <div class="font-bold text-amber-900 mb-1 flex items-center gap-2">
              🔧 Email Debug Mode
            </div>
            <p class="text-sm text-amber-800 leading-relaxed">
              Send all emails to <strong>{{ localSmtpConfig.email || 'your email' }}</strong> instead of actual recipients.
              Perfect for testing the email formatting and delivery before the real send!
            </p>
          </div>
        </label>
      </div>
    </div>

    <!-- Card Style Selection -->
    <div class="mb-8">
      <h3 class="font-bold text-gray-800 mb-6 text-lg">Choose Card Style</h3>
      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        <button
          v-for="(style, key) in cardStyles"
          :key="key"
          @click="selectedCardStyle = key"
          class="p-4 border-2 rounded-2xl transition-all text-center hover:shadow-lg group"
          :class="selectedCardStyle === key
            ? 'border-modern-primary bg-modern-primary/5 shadow-md'
            : 'border-gray-200 hover:border-modern-primary/50 bg-white'"
        >
          <div class="text-4xl mb-3 transform group-hover:scale-110 transition-transform duration-300">{{ style.preview }}</div>
          <p class="font-bold text-sm text-gray-800">{{ style.name }}</p>
          <p class="text-xs text-gray-500 mt-1">{{ style.description }}</p>
        </button>
      </div>
    </div>

    <!-- Email Subject -->
    <div class="mb-6">
      <label class="block text-sm font-bold text-gray-700 mb-2">Email Subject</label>
      <input
        v-model="localEmailSubject"
        type="text"
        placeholder="Secret Santa 2024"
        class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
      />
    </div>

    <!-- Email Template Editor -->
    <div class="mb-6">
      <div class="flex justify-between items-center mb-2">
        <label class="block text-sm font-bold text-gray-700">Message Content</label>
        <div class="text-xs text-gray-500 font-medium">
          Available variables:
          <code class="bg-gray-100 px-2 py-1 rounded mx-1 text-modern-primary border border-gray-200">{giver_name}</code>
          <code class="bg-gray-100 px-2 py-1 rounded mx-1 text-modern-primary border border-gray-200">{recipient_name}</code>
          <code class="bg-gray-100 px-2 py-1 rounded mx-1 text-modern-primary border border-gray-200">{recipient_interests}</code>
          <code class="bg-gray-100 px-2 py-1 rounded mx-1 text-modern-primary border border-gray-200">{recipient_address}</code>
        </div>
      </div>
      <textarea
        v-model="localEmailTemplate"
        rows="10"
        placeholder="Write your message here (this will be placed inside the styled card)..."
        class="w-full px-5 py-4 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent font-mono text-sm outline-none transition-all shadow-sm"
      ></textarea>
      <div class="flex gap-2 mt-3 flex-wrap">
        <button
          @click="insertVariable('{giver_name}')"
          class="px-3 py-1.5 text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg font-medium transition-colors"
        >
          + {giver_name}
        </button>
        <button
          @click="insertVariable('{recipient_name}')"
          class="px-3 py-1.5 text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg font-medium transition-colors"
        >
          + {recipient_name}
        </button>
        <button
          @click="insertVariable('{recipient_interests}')"
          class="px-3 py-1.5 text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg font-medium transition-colors"
        >
          + {recipient_interests}
        </button>
        <button
          @click="insertVariable('{recipient_address}')"
          class="px-3 py-1.5 text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg font-medium transition-colors"
        >
          + {recipient_address}
        </button>
      </div>
    </div>

    <!-- Preview -->
    <div class="p-8 bg-gray-50 rounded-2xl border border-gray-100">
      <div class="flex justify-between items-center mb-6">
        <h3 class="font-bold text-gray-800 text-lg">Card Preview</h3>
        <button
          @click="showFullPreview = !showFullPreview"
          class="px-5 py-2 bg-white border border-gray-200 hover:border-modern-primary text-gray-700 hover:text-modern-primary rounded-xl text-sm font-bold transition-all shadow-sm"
        >
          {{ showFullPreview ? 'Hide Full Preview' : 'Show Full Preview' }}
        </button>
      </div>

      <div v-if="participants.length >= 2">
        <div v-if="!showFullPreview" class="bg-white p-6 rounded-lg border border-gray-200 shadow-sm">
          <p class="font-semibold text-gray-800 mb-1">Subject: {{ localEmailSubject }}</p>
          <hr class="my-4" />
          <div class="text-center mb-4">
            <span class="text-4xl">{{ cardStyles[selectedCardStyle].preview }}</span>
            <p class="text-sm text-gray-600 mt-2">{{ cardStyles[selectedCardStyle].name }}</p>
          </div>
          <div class="whitespace-pre-wrap text-gray-700 text-sm">{{ previewText }}</div>
        </div>

        <!-- Full HTML Preview -->
        <div v-else class="bg-white rounded-lg border border-gray-200 shadow-lg overflow-hidden">
          <div class="bg-gray-800 px-4 py-2 text-white text-sm font-mono">
            Email Preview (as recipient will see it)
          </div>
          <div class="overflow-auto" style="max-height: 600px;">
            <iframe
              :srcdoc="fullPreviewHTML"
              class="w-full border-0"
              style="min-height: 600px;"
              @load="resizeIframe"
            ></iframe>
          </div>
        </div>
      </div>

      <div v-else class="text-gray-500 italic text-center py-8">
        Add at least 2 participants to see a preview
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { cardStyles, generateEmailCard } from '../cardTemplates.js'

const props = defineProps({
  emailSubject: String,
  emailTemplate: String,
  smtpConfig: Object,
  participants: Array,
  cardStyle: String,
  debugMode: Boolean,
  emailDebugMode: Boolean
})

const emit = defineEmits(['update:emailSubject', 'update:emailTemplate', 'update:smtpConfig', 'update:cardStyle', 'update:debugMode', 'update:emailDebugMode'])

const localEmailSubject = ref(props.emailSubject)
const localEmailTemplate = ref(props.emailTemplate)
const localSmtpConfig = ref({ ...props.smtpConfig })
const selectedCardStyle = ref(props.cardStyle || 'classic')
const localDebugMode = ref(props.debugMode || false)
const localEmailDebugMode = ref(props.emailDebugMode || false)
const showFullPreview = ref(false)

watch(localEmailSubject, (newVal) => {
  emit('update:emailSubject', newVal)
})

watch(localEmailTemplate, (newVal) => {
  emit('update:emailTemplate', newVal)
})

watch(localSmtpConfig, (newVal) => {
  emit('update:smtpConfig', newVal)
}, { deep: true })

watch(selectedCardStyle, (newVal) => {
  emit('update:cardStyle', newVal)
})

watch(localDebugMode, (newVal) => {
  emit('update:debugMode', newVal)
})

watch(localEmailDebugMode, (newVal) => {
  emit('update:emailDebugMode', newVal)
})

const previewText = computed(() => {
  if (props.participants.length < 2) return ''

  const giver = props.participants[0]
  const recipient = props.participants[1]

  return localEmailTemplate.value
    .replace(/{giver_name}/g, giver.name)
    .replace(/{recipient_name}/g, recipient.name)
    .replace(/{recipient_interests}/g, recipient.interests)
    .replace(/{recipient_address}/g, recipient.address || 'No address provided')
})

const fullPreviewHTML = computed(() => {
  if (props.participants.length < 2) return ''

  const giver = props.participants[0]
  const recipient = props.participants[1]

  return generateEmailCard(
    selectedCardStyle.value,
    giver.name,
    recipient.name,
    recipient.interests,
    recipient.address || '',
    previewText.value
  )
})

const insertVariable = (variable) => {
  localEmailTemplate.value += variable
}

const resizeIframe = (event) => {
  const iframe = event.target
  if (iframe.contentDocument) {
    iframe.style.height = iframe.contentDocument.body.scrollHeight + 'px'
  }
}
</script>
