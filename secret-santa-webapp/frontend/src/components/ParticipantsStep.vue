<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-2">Add Participants</h2>
    <p class="text-gray-500 mb-8 text-lg">Add participants manually or import from a CSV file.</p>

    <!-- CSV Import -->
    <div class="mb-8 p-8 bg-blue-50/50 border-2 border-dashed border-blue-200 rounded-2xl hover:border-blue-400 transition-colors group">
      <label class="block mb-3 text-sm font-bold text-gray-700 uppercase tracking-wide">Import from CSV</label>
      <div class="flex items-center gap-4">
        <input
          type="file"
          @change="handleFileUpload"
          accept=".csv"
          class="block w-full text-sm text-gray-500 file:mr-4 file:py-3 file:px-6 file:rounded-full file:border-0 file:text-sm file:font-bold file:bg-blue-500 file:text-white hover:file:bg-blue-600 cursor-pointer transition-all"
        />
      </div>
      <p class="text-xs text-gray-400 mt-3 font-medium">Header row with Name, Email, Interests, Address (any order; Address optional). Imported people are added to the list; duplicate emails are skipped.</p>
      <p v-if="importMessage" class="text-sm text-gray-600 mt-2 font-medium">{{ importMessage }}</p>
    </div>

    <!-- Manual Add Form -->
    <div class="mb-8 p-8 bg-gray-50 rounded-2xl shadow-sm">
      <h3 class="font-bold text-gray-700 mb-6 text-lg">Add Participant Manually</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        <input
          v-model="newParticipant.name"
          type="text"
          placeholder="Name"
          class="px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
        />
        <input
          v-model="newParticipant.email"
          type="email"
          placeholder="Email"
          class="px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
        />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <input
          v-model="newParticipant.interests"
          type="text"
          placeholder="Interests (comma separated)"
          class="px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
        />
        <input
          v-model="newParticipant.address"
          type="text"
          placeholder="Address"
          class="px-5 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-modern-primary focus:border-transparent outline-none transition-all shadow-sm"
        />
      </div>
      <p v-if="duplicateName" class="text-sm text-red-500 mb-3">Someone named "{{ newParticipant.name.trim() }}" is already on the list - names must be unique.</p>
      <button
        @click="addParticipant"
        :disabled="!canAddParticipant"
        class="w-full md:w-auto px-8 py-3 bg-gradient-to-r from-green-400 to-green-600 hover:from-green-500 hover:to-green-700 disabled:from-gray-300 disabled:to-gray-400 disabled:cursor-not-allowed text-white rounded-xl font-bold shadow-md hover:shadow-lg transition-all transform hover:-translate-y-0.5"
      >
        + Add Participant
      </button>
    </div>

    <!-- Participants List -->
    <div v-if="participants.length > 0">
      <h3 class="font-bold text-gray-700 mb-6 text-lg flex items-center gap-2">
        Participants <span class="bg-gray-200 text-gray-600 px-2 py-1 rounded-lg text-xs">{{ participants.length }}</span>
      </h3>
      <div class="grid grid-cols-1 gap-4">
        <div
          v-for="(participant, index) in participants"
          :key="index"
          class="flex items-center justify-between p-5 bg-white border border-gray-100 rounded-xl shadow-sm hover:shadow-md transition-all group"
        >
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-1">
              <div class="w-8 h-8 rounded-full bg-gradient-to-br from-modern-primary to-modern-secondary flex items-center justify-center text-white font-bold text-xs">
                {{ participant.name.charAt(0) }}
              </div>
              <p class="font-bold text-gray-800">{{ participant.name }}</p>
            </div>
            <p class="text-sm text-gray-500 ml-11">{{ participant.email }}</p>
            <p class="text-sm text-gray-400 italic ml-11 mt-1">{{ participant.interests }}</p>
            <p v-if="participant.address" class="text-sm text-gray-400 ml-11 mt-1">📍 {{ participant.address }}</p>
          </div>
          <button
            @click="removeParticipant(index)"
            class="ml-4 px-4 py-2 bg-red-50 text-red-500 hover:bg-red-100 rounded-lg text-sm font-bold transition-all"
          >
            Remove
          </button>
        </div>
      </div>
    </div>
    <div v-else class="text-center py-16 bg-gray-50 rounded-2xl border-2 border-dashed border-gray-200">
      <p class="text-gray-400 font-medium">No participants yet. Add at least 3 to continue.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const participants = defineModel('participants', { required: true })

const blank = () => ({ name: '', email: '', interests: '', address: '' })
const newParticipant = ref(blank())
const importMessage = ref('')

const duplicateName = computed(() => {
  const name = newParticipant.value.name.trim()
  return !!name && participants.value.some(p => p.name === name)
})

const canAddParticipant = computed(() => {
  const p = newParticipant.value
  return p.name.trim() && p.email.trim() && p.interests.trim() && !duplicateName.value
})

const addParticipant = () => {
  if (!canAddParticipant.value) return
  const p = Object.fromEntries(Object.entries(newParticipant.value).map(([k, v]) => [k, v.trim()]))
  participants.value = [...participants.value, p]
  newParticipant.value = blank()
}

const removeParticipant = (index) => {
  participants.value = participants.value.filter((_, i) => i !== index)
}

const splitCsvLine = (line) =>
  line.split(/,(?=(?:(?:[^"]*"){2})*[^"]*$)/).map(p => p.trim().replace(/^"|"$/g, ''))

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = (e) => {
    const [header, ...rows] = e.target.result.split(/\r?\n/).filter(l => l.trim())
    const cols = splitCsvLine(header || '').map(h => h.toLowerCase())
    const idx = Object.fromEntries(['name', 'email', 'interests', 'address'].map(k => [k, cols.indexOf(k)]))
    if (idx.name < 0 || idx.email < 0 || idx.interests < 0) {
      importMessage.value = 'CSV needs a header row with Name, Email and Interests columns.'
      return
    }

    const names = new Set(participants.value.map(p => p.name))
    const emails = new Set(participants.value.map(p => p.email.toLowerCase()))
    const added = []
    let skipped = 0
    for (const row of rows) {
      const parts = splitCsvLine(row)
      const person = {
        name: parts[idx.name] || '',
        email: parts[idx.email] || '',
        interests: parts[idx.interests] || '',
        address: idx.address >= 0 ? parts[idx.address] || '' : '',
      }
      if (!person.name || !person.email || names.has(person.name) || emails.has(person.email.toLowerCase())) {
        skipped++
        continue
      }
      names.add(person.name)
      emails.add(person.email.toLowerCase())
      added.push(person)
    }
    participants.value = [...participants.value, ...added]
    importMessage.value = `Added ${added.length}${skipped ? `, skipped ${skipped} (incomplete or duplicate)` : ''}.`
  }
  reader.readAsText(file)
  event.target.value = '' // allow re-importing the same file
}
</script>
