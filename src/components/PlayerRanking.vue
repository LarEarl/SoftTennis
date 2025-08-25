<template>
  <ul class="divide-y">
    <li
      v-for="player in players"
      :key="player.id"
      class="flex items-center py-2"
    >
      <span class="w-6 text-right font-bold text-blue-700 mr-2">{{
        player.rank
      }}</span>
      <img
        v-if="player.photo"
        :src="player.photo"
        class="w-8 h-8 rounded-full object-cover mx-2"
      />
      <span class="flex-1">{{ player.first_name }} {{ player.last_name }}</span>
      <span class="ml-auto font-semibold text-gray-700">{{
        player.points
      }}</span>
    </li>
  </ul>
</template>

<script setup>
import { ref, onMounted } from "vue";
const players = ref([]);
onMounted(async () => {
  const res = await fetch(
    "http://127.0.0.1:8000/api/players/?ordering=rank&limit=10"
  );
  players.value = await res.json();
});
</script>
