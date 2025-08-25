<template>
  <div
    class="bg-white rounded-2xl shadow-xl p-6 flex flex-col items-center text-center"
  >
    <img
      v-if="director.photo"
      :src="director.photo"
      class="w-28 h-28 rounded-full object-cover mb-3 border-4 border-blue-200 shadow"
    />
    <div class="text-xl font-bold text-blue-900">{{ director.name }}</div>
    <div class="text-blue-700 font-semibold mb-2">{{ director.position }}</div>
    <div class="text-gray-700 line-clamp-3 mb-2">{{ director.bio }}</div>
    <span v-if="director.email" class="text-xs text-gray-400 mt-2">
      <a :href="`mailto:${director.email}`" class="hover:underline">{{
        director.email
      }}</a>
    </span>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const director = ref({});
onMounted(async () => {
  // Получаем первого руководителя (предполагаем, что директор всегда первый)
  const res = await fetch("http://127.0.0.1:8000/api/leadership/");
  const data = await res.json();
  director.value = data?.[0] || {};
});
</script>
