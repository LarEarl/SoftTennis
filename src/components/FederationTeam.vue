<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="member in team"
      :key="member.id"
      :to="`/federation/team/${member.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <img
        v-if="member.photo"
        :src="member.photo"
        class="w-24 h-24 rounded-full object-cover mb-4 border-2 border-blue-300 shadow"
      />
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ member.name }}
      </h3>
      <p class="text-gray-500 text-sm text-center mb-2 break-words">
        {{ member.role }}
      </p>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="member.description"
      >
        {{ member.description }}
      </p>
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const team = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/team/");
  team.value = await res.json();
});
</script>
