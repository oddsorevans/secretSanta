<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-2">Email Template & Card Style</h2>
    <p class="text-gray-500 mb-8 text-lg">Choose a card style and customize your Secret Santa message.</p>

    <!-- Mode Selection -->
    <div class="mb-8 p-8 bg-gradient-to-br from-purple-50 to-blue-50 border-2 border-purple-100 rounded-2xl">
      <h3 class="font-bold text-gray-800 mb-6 text-lg">Choose Mode</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <button
          @click="debugMode = false"
          class="p-6 border-2 rounded-2xl transition-all text-left group relative overflow-hidden"
          :class="!debugMode
            ? 'border-modern-secondary bg-white shadow-lg scale-[1.02] ring-2 ring-modern-secondary/20'
            : 'border-gray-200 hover:border-modern-secondary/50 bg-white/50'"
        >
          <div class="relative z-10">
            <div class="flex items-center mb-3">
              <div class="w-10 h-10 rounded-full flex items-center justify-center text-xl mr-3" :class="!debugMode ? 'bg-modern-secondary text-white' : 'bg-gray-100 text-gray-500'">📧</div>
              <h4 class="font-bold text-lg text-gray-800">Send Real Emails</h4>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">
              Send actual Secret Santa emails to all participants. Pairings will remain secret!
            </p>
          </div>
          <div v-if="!debugMode" class="absolute top-4 right-4 text-modern-secondary">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
        </button>

        <button
          @click="debugMode = true"
          class="p-6 border-2 rounded-2xl transition-all text-left group relative overflow-hidden"
          :class="debugMode
            ? 'border-modern-primary bg-white shadow-lg scale-[1.02] ring-2 ring-modern-primary/20'
            : 'border-gray-200 hover:border-modern-primary/50 bg-white/50'"
        >
          <div class="relative z-10">
            <div class="flex items-center mb-3">
              <div class="w-10 h-10 rounded-full flex items-center justify-center text-xl mr-3" :class="debugMode ? 'bg-modern-primary text-white' : 'bg-gray-100 text-gray-500'">🔍</div>
              <h4 class="font-bold text-lg text-gray-800">Preview Only</h4>
            </div>
            <p class="text-sm text-gray-600 leading-relaxed">
              Generate test pairings and view every card without sending any email.
            </p>
          </div>
          <div v-if="debugMode" class="absolute top-4 right-4 text-modern-primary">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          </div>
        </button>
      </div>

      <div v-if="debugMode" class="mt-6 p-4 bg-purple-100/50 border border-purple-200 rounded-xl flex items-start gap-3">
        <span class="text-purple-600 text-xl">💡</span>
        <p class="text-sm text-purple-800 font-medium pt-0.5">
          <strong>Preview Only:</strong> No SMTP configuration needed. You'll be able to view all pairings and preview cards on the next step.
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
    <div v-if="!debugMode" class="mb-8 p-8 bg-gray-50 rounded-2xl border border-gray-100">
      <h3 class="font-bold text-gray-800 mb-6 text-lg">Email Configuration</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">SMTP Server</label>
          <input
            v-model="smtpConfig.server"
            type="text"
            placeholder="smtp.gmail.com"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">Port</label>
          <input
            v-model.number="smtpConfig.port"
            type="number"
            placeholder="587"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">Your Email</label>
          <input
            v-model="smtpConfig.email"
            type="email"
            placeholder="your.email@gmail.com"
            class="w-full px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
          />
        </div>
        <div>
          <label class="block text-sm font-bold text-gray-700 mb-2">App Password</label>
          <input
            v-model="smtpConfig.password"
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
            v-model="emailDebugMode"
            type="checkbox"
            class="mt-1 w-5 h-5 text-amber-600 border-amber-300 rounded focus:ring-2 focus:ring-amber-500 cursor-pointer"
          />
          <div class="flex-1">
            <div class="font-bold text-amber-900 mb-1 flex items-center gap-2">
              🔧 Send All Emails To Me (test)
            </div>
            <p class="text-sm text-amber-800 leading-relaxed">
              Send all emails to <strong>{{ smtpConfig.email || 'your email' }}</strong> instead of actual recipients.
              Check formatting and delivery before the real send. No one else gets an email.
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
          v-for="(style, key) in themes"
          :key="key"
          @click="cardStyle = key"
          class="p-4 border-2 rounded-2xl transition-all text-center hover:shadow-lg group"
          :class="cardStyle === key
            ? 'border-modern-primary bg-modern-primary/5 shadow-md'
            : 'border-gray-200 hover:border-modern-primary/50 bg-white'"
        >
          <div class="text-4xl mb-3 transform group-hover:scale-110 transition-transform duration-300">{{ style.emoji }}</div>
          <p class="font-bold text-sm text-gray-800">{{ style.name }}</p>
          <p class="text-xs text-gray-500 mt-1">{{ style.description }}</p>
        </button>
      </div>
    </div>

    <!-- Email Subject -->
    <div class="mb-6">
      <label class="block text-sm font-bold text-gray-700 mb-2">Email Subject</label>
      <input
        v-model="emailSubject"
        type="text"
        placeholder="Secret Santa"
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
        v-model="emailTemplate"
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
      </div>

      <div v-if="participants.length >= 2">
        <p class="font-semibold text-gray-800 mb-3 text-sm">Subject: {{ emailSubject }}</p>
        <div class="bg-white rounded-lg border border-gray-200 shadow-lg overflow-hidden">
          <div class="bg-gray-800 px-4 py-2 text-white text-sm font-mono">
            Email Preview (the server renders this exact HTML when sending)
          </div>
          <iframe :srcdoc="previewHtml" sandbox="" class="w-full border-0" style="height: 700px;"></iframe>
        </div>
      </div>

      <div v-else class="text-gray-500 italic text-center py-8">
        Add at least 2 participants to see a preview
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onBeforeUnmount } from 'vue'
import axios from 'axios'

const props = defineProps({ participants: Array, themes: Object })

const emailSubject = defineModel('emailSubject')
const emailTemplate = defineModel('emailTemplate')
const smtpConfig = defineModel('smtpConfig')
const cardStyle = defineModel('cardStyle')
const debugMode = defineModel('debugMode')
const emailDebugMode = defineModel('emailDebugMode')

const previewHtml = ref('')
let timer
let latest = 0

// Preview is rendered by the backend so it always matches what gets sent.
const refreshPreview = async () => {
  if (props.participants.length < 2) return
  const [giver, recipient] = props.participants
  const id = ++latest
  try {
    const { data } = await axios.post('/api/preview', {
      cardStyle: cardStyle.value,
      emailTemplate: emailTemplate.value,
      giver,
      recipient,
    })
    if (id === latest) previewHtml.value = data.html
  } catch (e) {
    if (id === latest) previewHtml.value = `<p style="font-family:sans-serif;color:#b00">Preview failed: ${e.message}</p>`
  }
}

watch([cardStyle, emailTemplate, () => props.participants], () => {
  clearTimeout(timer)
  timer = setTimeout(refreshPreview, 300)
}, { immediate: true, deep: true })

onBeforeUnmount(() => clearTimeout(timer))

const insertVariable = (variable) => {
  emailTemplate.value += variable
}
</script>
