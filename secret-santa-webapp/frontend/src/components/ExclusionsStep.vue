<template>
  <div>
    <h2 class="text-3xl font-bold text-gray-800 mb-2">Set Exclusions</h2>
    <p class="text-gray-500 mb-8 text-lg">Specify which participants should not be paired together.</p>

    <!-- Mutual Exclusion Toggle -->
    <div v-if="participants.length > 0" class="mb-8 p-6 bg-indigo-50/50 border border-indigo-100 rounded-2xl">
      <div class="flex items-center justify-between">
        <div>
          <label class="flex items-center cursor-pointer group">
            <div class="relative">
              <input
                v-model="autoMutual"
                type="checkbox"
                class="sr-only peer"
              />
              <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-indigo-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-indigo-600"></div>
            </div>
            <span class="ml-3 font-bold text-gray-700 group-hover:text-indigo-700 transition-colors">Auto-Mutual Exclusions</span>
          </label>
          <p class="text-xs text-gray-500 mt-2 ml-14 font-medium">
            When enabled, excluding A→B automatically excludes B→A
          </p>
        </div>
        <div class="text-right text-xs text-gray-500 bg-white p-3 rounded-xl shadow-sm border border-indigo-100">
          <div class="flex items-center gap-2 mb-2">
            <span class="inline-block w-3 h-3 bg-red-500 rounded-full"></span>
            <span class="font-medium">One-way block</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="inline-block w-3 h-3 bg-red-500 rounded-full ring-2 ring-red-200"></span>
            <span class="font-medium">Mutual block</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="participants.length === 0" class="text-center py-16 bg-gray-50 rounded-2xl border-2 border-dashed border-gray-200">
      <p class="text-gray-400 font-medium">Please add participants first.</p>
    </div>

    <div v-else class="grid grid-cols-1 gap-6">
      <div
        v-for="participant in participants"
        :key="participant.name"
        class="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition-all"
      >
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center text-gray-600 font-bold text-xs">
              {{ participant.name.charAt(0) }}
            </div>
            <h3 class="font-bold text-gray-800 text-lg">{{ participant.name }} cannot buy for:</h3>
          </div>
          <span class="text-xs font-bold px-3 py-1 bg-gray-100 text-gray-600 rounded-full">
            {{ getExclusionCount(participant.name) }} exclusion(s)
          </span>
        </div>

        <div class="flex flex-wrap gap-2">
          <button
            v-for="other in getOtherParticipants(participant.name)"
            :key="other.name"
            @click="toggleExclusion(participant.name, other.name)"
            class="px-4 py-2 rounded-xl text-sm font-bold transition-all relative border"
            :class="getExclusionButtonClass(participant.name, other.name)"
          >
            {{ other.name }}
            <span v-if="isExcluded(participant.name, other.name)" class="ml-1">
              {{ isMutualExclusion(participant.name, other.name) ? '⇄' : '→' }}
            </span>
          </button>
        </div>
      </div>
    </div>

    <div v-if="participants.length > 0" class="mt-8 p-4 bg-amber-50 border border-amber-100 rounded-xl flex items-start gap-3">
      <span class="text-amber-500 text-xl">💡</span>
      <p class="text-sm text-amber-800 font-medium pt-0.5">
        If exclusions make pairing impossible, the algorithm will retry automatically.
        Make sure your exclusions allow for valid pairings.
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ participants: Array })
const exclusions = defineModel('exclusions', { required: true })
const autoMutual = ref(true)

const getOtherParticipants = (name) => props.participants.filter(p => p.name !== name)
const isExcluded = (giver, recipient) => exclusions.value[giver]?.includes(recipient) || false
const isMutualExclusion = (giver, recipient) => isExcluded(giver, recipient) && isExcluded(recipient, giver)
const getExclusionCount = (name) => exclusions.value[name]?.length || 0

const getExclusionButtonClass = (giver, recipient) => {
  if (isMutualExclusion(giver, recipient)) {
    return 'bg-red-500 text-white hover:bg-red-600 ring-2 ring-red-200 border-transparent shadow-sm'
  }
  if (isExcluded(giver, recipient)) {
    return 'bg-red-500 text-white hover:bg-red-600 border-transparent shadow-sm'
  }
  return 'bg-white text-gray-600 border-gray-200 hover:border-modern-primary hover:text-modern-primary hover:shadow-sm'
}

const toggleExclusion = (giver, recipient) => {
  const next = { ...exclusions.value }
  const turnOn = !isExcluded(giver, recipient)
  const set = (a, b) => {
    const rest = (next[a] || []).filter(n => n !== b)
    next[a] = turnOn ? [...rest, b] : rest
  }
  set(giver, recipient)
  if (autoMutual.value) set(recipient, giver)
  exclusions.value = next
}
</script>
