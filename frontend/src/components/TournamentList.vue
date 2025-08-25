<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="tournament in tournamentList"
      :key="tournament.id"
      :to="`/tournaments/${tournament.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <img
        v-if="tournament.logo"
        :src="tournament.logo"
        alt="logo"
        class="w-24 h-24 rounded-full object-cover mb-4 border-2 border-blue-300 shadow"
      />
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ tournament.name }}
      </h3>
      <p
        class="text-gray-500 text-sm text-center mb-2 truncate max-w-full"
        v-if="tournament.location"
      >
        {{ tournament.location }}
      </p>
      <!-- <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="tournament.description"
      >
        {{ tournament.description }}
      </p> -->
      <span class="text-xs text-gray-400 mt-auto" v-if="tournament.start_date"
        >{{ tournament.start_date }} — {{ tournament.end_date }}</span
      >
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const tournamentList = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/tournaments/");
  tournamentList.value = await res.json();
});
</script>
