<template>
  <div class="flex items-center flex-1">
    <div class="flex flex-col items-center relative z-10">
      <div
        class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm transition-all duration-300 shadow-lg"
        :class="completed ? 'bg-gradient-to-br from-green-400 to-green-600 text-white scale-110' : active ? 'bg-gradient-to-br from-modern-secondary to-modern-primary text-white ring-4 ring-modern-primary/20 scale-125' : 'bg-gray-100 text-gray-400'"
      >
        <span v-if="completed">✓</span>
        <span v-else>{{ number }}</span>
      </div>
      <span
        class="mt-3 text-xs font-bold uppercase tracking-wider transition-colors duration-300"
        :class="active ? 'text-modern-primary' : completed ? 'text-green-600' : 'text-gray-400'"
      >
        {{ title }}
      </span>
    </div>
    <div
      v-if="!isLast"
      class="flex-1 h-1 mx-4 rounded-full transition-colors duration-500"
      :class="completed ? 'bg-green-200' : 'bg-gray-100'"
    ></div>
  </div>
</template>

<script setup>
defineProps({
  number: Number,
  title: String,
  active: Boolean,
  completed: Boolean,
  isLast: Boolean
})
</script>
