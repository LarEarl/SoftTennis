<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="match in limitedMatches"
      :key="match.id"
      :to="`/matches/${match.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <div
        class="w-24 h-24 rounded-full bg-green-100 flex items-center justify-center mb-4 border-2 border-blue-300 shadow"
      >
        <svg
          class="w-12 h-12 text-green-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
          />
        </svg>
      </div>
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ match.player1_first_name }} {{ match.player1_last_name }} vs
        {{ match.player2_first_name }} {{ match.player2_last_name }}
      </h3>
      <p
        class="text-gray-500 text-sm text-center mb-2 break-words"
        v-if="match.tournament_name"
      >
        {{ match.tournament_name }}
      </p>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="match.score"
      >
        Счёт: {{ match.score }}
      </p>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="match.winner_first_name"
      >
        Победитель: {{ match.winner_first_name }} {{ match.winner_last_name }}
      </p>
      <span class="text-xs text-gray-400 mt-auto" v-if="match.date">{{
        new Date(match.date).toLocaleDateString()
      }}</span>
    </router-link>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
const props = defineProps({ limit: { type: Number, default: null } });

const matchList = ref([]);

const limitedMatches = computed(() =>
  props.limit ? matchList.value.slice(0, props.limit) : matchList.value
);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/matches/");
  let data = await res.json();
  console.log("Fetched matches:", data);

  matchList.value = data.map((match) => ({
    ...match,
    tournament_name: match.tournament?.name ?? "",
    player1_first_name: match.player1?.first_name ?? "",
    player1_last_name: match.player1?.last_name ?? "",
    player2_first_name: match.player2?.first_name ?? "",
    player2_last_name: match.player2?.last_name ?? "",
    winner_first_name: match.winner?.first_name ?? "",
    winner_last_name: match.winner?.last_name ?? "",
  }));
});
</script>
