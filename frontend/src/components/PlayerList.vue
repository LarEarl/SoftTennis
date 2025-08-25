<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="player in limitedPlayers"
      :key="player.id"
      :to="`/players/${player.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <img
        v-if="player.photo"
        :src="player.photo"
        alt="player photo"
        class="w-24 h-24 rounded-full object-cover mb-4 border-2 border-blue-300 shadow"
      />
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ player.first_name }} {{ player.last_name }}
      </h3>
      <p
        class="text-gray-500 text-sm text-center mb-2 break-words"
        v-if="player.rank"
      >
        Рейтинг: {{ player.rank }}
      </p>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="player.country"
      >
        {{ player.country }}
      </p>
      <span class="text-xs text-gray-400 mt-auto" v-if="player.birth_date">{{
        new Date(player.birth_date).toLocaleDateString()
      }}</span>
    </router-link>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
const props = defineProps({ top: { type: Number, default: null } });

const playerList = ref([]);

const limitedPlayers = computed(() =>
  props.top
    ? [...playerList.value].sort((a, b) => a.rank - b.rank).slice(0, props.top)
    : playerList.value
);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/players/");
  playerList.value = await res.json();
});
</script>
