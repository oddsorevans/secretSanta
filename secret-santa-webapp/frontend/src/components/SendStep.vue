<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-2">Review & Send</h2>
    <p class="text-gray-500 mb-8 text-lg">Review your configuration and send the Secret Santa emails.</p>

    <!-- Summary -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div class="p-6 bg-white rounded-2xl border border-blue-100 shadow-sm hover:shadow-md transition-all relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-20 h-20 bg-blue-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
        <div class="relative z-10">
          <div class="text-4xl font-bold text-blue-600 mb-1">{{ participants.length }}</div>
          <div class="text-sm font-bold text-gray-500 uppercase tracking-wide">Participants</div>
        </div>
      </div>
      <div class="p-6 bg-white rounded-2xl border border-purple-100 shadow-sm hover:shadow-md transition-all relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-20 h-20 bg-purple-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
        <div class="relative z-10">
          <div class="text-4xl font-bold text-purple-600 mb-1">{{ totalExclusions }}</div>
          <div class="text-sm font-bold text-gray-500 uppercase tracking-wide">Total Exclusions</div>
        </div>
      </div>
      <div class="p-6 bg-white rounded-2xl border border-green-100 shadow-sm hover:shadow-md transition-all relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-20 h-20 bg-green-50 rounded-bl-full -mr-4 -mt-4 transition-transform group-hover:scale-110"></div>
        <div class="relative z-10">
          <div class="text-4xl font-bold text-green-600 mb-1">{{ cardStyleName }}</div>
          <div class="text-sm font-bold text-gray-500 uppercase tracking-wide">Card Style</div>
        </div>
      </div>
    </div>

    <!-- Mode Display -->
    <div class="mb-8 p-6 border-2 rounded-2xl" :class="debugMode ? 'bg-purple-50/50 border-purple-200' : (emailDebugMode ? 'bg-amber-50/50 border-amber-200' : 'bg-blue-50/50 border-blue-200')">
      <div class="flex items-start gap-4">
        <div class="w-12 h-12 rounded-full flex items-center justify-center text-2xl shrink-0" :class="debugMode ? 'bg-purple-100 text-purple-600' : (emailDebugMode ? 'bg-amber-100 text-amber-600' : 'bg-blue-100 text-blue-600')">
          {{ debugMode ? '🔍' : (emailDebugMode ? '🔧' : '⚠️') }}
        </div>
        <div>
          <h3 class="font-bold text-lg mb-2" :class="debugMode ? 'text-purple-900' : (emailDebugMode ? 'text-amber-900' : 'text-blue-900')">
            {{ debugMode ? 'Preview Only Active' : (emailDebugMode ? 'Email Preview Only Active' : 'Important Notice') }}
          </h3>
          <p class="text-sm leading-relaxed" :class="debugMode ? 'text-purple-800' : (emailDebugMode ? 'text-amber-800' : 'text-blue-800')">
            <span v-if="debugMode">
              You're in preview-only mode! Clicking the button below will generate pairings and show you all the cards without sending any emails. Perfect for testing!
            </span>
            <span v-else-if="emailDebugMode">
              Test send is active! All emails will be sent to <strong>{{ smtpConfig.email }}</strong> instead of actual recipients.
              This lets you verify the emails are formatted correctly before sending to everyone.
              The pairings will NOT be shown to you - they remain secret!
            </span>
            <span v-else>
              Once you click "Send Emails", the Secret Santa pairings will be generated and sent immediately.
              The pairings will NOT be shown to you - they remain completely secret!
              Make sure all information is correct before proceeding.
            </span>
          </p>
        </div>
      </div>
    </div>

    <!-- Status Messages -->
    <div v-if="statusMessage" class="mb-8 p-6 rounded-2xl border" :class="statusClass">
      <p class="font-bold text-lg">{{ statusMessage }}</p>
      <p v-if="detailMessage" class="text-sm mt-2 opacity-90">{{ detailMessage }}</p>
    </div>

    <!-- Debug Mode Results with Card Previews -->
    <div v-if="debugMode && debugResults.length > 0" class="mb-8 space-y-6">
      <div class="p-6 bg-purple-50 border border-purple-100 rounded-2xl">
        <h3 class="font-bold text-purple-900 mb-2 text-lg">🔍 Preview Only Active - Pairings & Card Previews</h3>
        <p class="text-sm text-purple-700">
          Below are all the pairings and their corresponding email cards. No emails have been sent.
        </p>
      </div>

      <div
        v-for="(result, index) in debugResults"
        :key="index"
        class="border border-gray-200 rounded-2xl overflow-hidden bg-white shadow-sm hover:shadow-md transition-all"
      >
        <!-- Pairing Header -->
        <div class="bg-gray-50 px-6 py-4 border-b border-gray-100">
          <div class="flex justify-between items-center">
            <div>
              <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Pairing #{{ index + 1 }}</p>
              <h4 class="text-xl font-bold text-gray-800">
                {{ result.giver }} <span class="text-gray-400 mx-2">→</span> {{ result.recipient }}
              </h4>
            </div>
            <button
              @click="result.showCard = !result.showCard"
              class="px-5 py-2 bg-white border border-gray-200 text-gray-700 rounded-xl text-sm font-bold hover:border-modern-primary hover:text-modern-primary transition-all shadow-sm"
            >
              {{ result.showCard ? 'Hide Card' : 'View Card' }}
            </button>
          </div>
        </div>

        <!-- Card Preview -->
        <div v-if="result.showCard" class="p-6 bg-gray-50/50">
          <div class="mb-4 px-5 py-3 bg-white rounded-xl border border-gray-200 shadow-sm">
            <p class="text-sm text-gray-600">
              <strong class="text-gray-900">To:</strong> {{ result.giverEmail }}
              <span class="mx-3 text-gray-300">|</span>
              <strong class="text-gray-900">Subject:</strong> {{ emailSubject }}
            </p>
          </div>

          <div class="bg-white rounded-xl border border-gray-200 overflow-hidden shadow-lg">
            <div class="bg-gray-900 px-5 py-3 text-white text-xs font-mono flex justify-between items-center">
              <span>Email Card Preview</span>
              <button
                @click="downloadCardHTML(result)"
                class="px-3 py-1.5 bg-gray-700 hover:bg-gray-600 rounded-lg text-xs font-medium transition-colors"
              >
                Download HTML
              </button>
            </div>
            <div class="overflow-auto" style="max-height: 600px;">
              <iframe
                :srcdoc="result.cardHTML"
                sandbox=""
                class="w-full border-0"
                style="min-height: 600px;"
              ></iframe>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Send Button -->
    <div class="flex justify-center">
      <button
        v-if="!sent"
        @click="sendEmails"
        :disabled="sending || !canSend"
        class="px-10 py-5 bg-gradient-to-r from-modern-secondary to-modern-primary hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-full font-bold text-xl transition-all transform hover:-translate-y-1 hover:shadow-2xl shadow-lg"
      >
        <span v-if="!sending">{{ props.debugMode ? '🔍 Generate Debug Preview' : '🎅 Send Secret Santa Emails' }}</span>
        <span v-else>{{ props.debugMode ? 'Generating...' : 'Sending...' }}</span>
      </button>

      <div v-else class="text-center py-8">
        <div class="text-7xl mb-6 animate-bounce">🎉</div>
        <h3 class="text-3xl font-bold text-gray-800 mb-3">Emails Sent Successfully!</h3>
        <p class="text-gray-500 text-lg mb-8">All participants have received their Secret Santa assignments.</p>
        <button
          @click="resetApp"
          class="px-8 py-3 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-full font-bold transition-all"
        >
          Start Over
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

const props = defineProps({
  participants: Array,
  exclusions: Object,
  emailSubject: String,
  emailTemplate: String,
  smtpConfig: Object,
  cardStyle: String,
  debugMode: Boolean,
  emailDebugMode: Boolean,
  themes: Object
})

const sending = ref(false)
const sent = ref(false)
const statusMessage = ref('')
const detailMessage = ref('')
const emailsSent = ref(0)
const debugResults = ref([])
const failed = ref([])

const totalExclusions = computed(() => {
  return Object.values(props.exclusions).reduce((sum, arr) => sum + arr.length, 0)
})

const cardStyleName = computed(() => {
  return props.themes?.[props.cardStyle]?.name || props.cardStyle
})

const canSend = computed(() => {
  if (props.debugMode) {
    return props.participants.length >= 3
  }
  return props.participants.length >= 3 &&
         props.smtpConfig.email &&
         props.smtpConfig.password &&
         props.emailTemplate &&
         props.emailSubject
})

const statusClass = computed(() => {
  if (statusMessage.value.includes('Success') || statusMessage.value.includes('Complete')) {
    return 'bg-green-100 border border-green-300 text-green-800'
  } else if (statusMessage.value.includes('Error') || statusMessage.value.includes('Failed')) {
    return 'bg-red-100 border border-red-300 text-red-800'
  }
  return 'bg-blue-100 border border-blue-300 text-blue-800'
})

const sendEmails = async () => {
  if (!canSend.value) return

  sending.value = true
  emailsSent.value = 0
  statusMessage.value = props.debugMode ? 'Generating pairings...' : 'Generating pairings...'
  detailMessage.value = ''
  debugResults.value = []

  try {
    // Only send SMTP config if NOT in debug mode
    const payload = {
      participants: props.participants,
      exclusions: props.exclusions,
      emailSubject: props.emailSubject,
      emailTemplate: props.emailTemplate,
      cardStyle: props.cardStyle,
      testMode: props.debugMode,
      emailDebugMode: props.emailDebugMode
    }

    // Only include SMTP config for real send mode
    if (!props.debugMode) {
      payload.smtpConfig = props.smtpConfig
    }

    const response = await axios.post('/api/send', payload)

    if (props.debugMode) {
      // Debug mode: show pairings with card previews
      debugResults.value = response.data.pairings.map(p => ({
        giver: p.giver,
        recipient: p.recipient,
        giverEmail: p.giverEmail,
        cardHTML: p.html,
        showCard: false
      }))

      statusMessage.value = 'Debug Mode Complete'
      detailMessage.value = `Generated ${debugResults.value.length} pairings with card previews. No emails were sent.`
      sending.value = false
    } else {
      emailsSent.value = response.data.emailsSent
      failed.value = response.data.failed || []
      sent.value = failed.value.length === 0
      statusMessage.value = sent.value ? 'Success! All emails sent.' : 'Failed: some emails were not sent'
      detailMessage.value = sent.value
        ? `${emailsSent.value} participants received their Secret Santa assignments.`
        : `${emailsSent.value} sent. Failed for: ${failed.value.join(', ')}. Starting over will reshuffle pairings, so check with everyone first.`
      sending.value = false
    }
  } catch (error) {
    statusMessage.value = 'Error sending emails'
    detailMessage.value = error.response?.data?.error || error.message || 'Unknown error occurred'
    emailsSent.value = error.response?.data?.emailsSent || 0
    failed.value = error.response?.data?.failed || []
    console.error('Send error:', error)
    sending.value = false
  }
}

const downloadCardHTML = (result) => {
  const blob = new Blob([result.cardHTML], { type: 'text/html' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `secret-santa-card-${result.giver}.html`
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}

const resetApp = () => {
  window.location.reload()
}
</script>
