<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="leader in leadership"
      :key="leader.id"
      :to="`/federation/leadership/${leader.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <img
        v-if="leader.photo"
        :src="leader.photo"
        class="w-24 h-24 rounded-full object-cover mb-4 border-2 border-blue-300 shadow"
      />
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ leader.name }}
      </h3>
      <p class="text-gray-500 text-sm text-center mb-2 break-words">
        {{ leader.position }}
      </p>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="leader.description"
      >
        {{ leader.description }}
      </p>
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const leadership = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/leadership/");
  leadership.value = await res.json();
});
</script>
