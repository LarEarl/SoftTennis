<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/matches" class="hover:underline">Матчи</router-link>
      <span> / </span>
      <span class="text-gray-700 font-semibold"
        >{{ match?.player1_first_name }} {{ match?.player1_last_name }} vs
        {{ match?.player2_first_name }} {{ match?.player2_last_name }}</span
      >
    </nav>

    <div
      v-if="match"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <div
        class="w-36 h-36 rounded-full bg-green-100 flex items-center justify-center mb-5 border-4 border-blue-200 shadow"
      >
        <svg
          class="w-16 h-16 text-green-600"
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
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900 break-words">
        {{ match.player1_first_name }} {{ match.player1_last_name }} vs
        {{ match.player2_first_name }} {{ match.player2_last_name }}
      </h1>
      <div
        class="text-lg text-blue-700 font-semibold mb-4 text-center break-words"
      >
        {{ match.tournament_name }}
      </div>
      <div class="text-gray-700 text-base mb-4 text-center max-w-full">
        <div class="mb-2 break-words">
          <b>Дата:</b> {{ formatDate(match.date) }}
        </div>
        <div class="mb-2 break-words"><b>Счёт:</b> {{ match.score }}</div>
        <div
          v-if="match.winner_first_name"
          class="text-green-700 font-semibold break-words"
        >
          Победитель: {{ match.winner_first_name }} {{ match.winner_last_name }}
        </div>
      </div>
    </div>
    <div v-else class="text-center py-10 text-gray-400">
      Информация не найдена...
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const match = ref(null);

function formatDate(dateStr) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleString();
}

onMounted(async () => {
  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/matches/${route.params.id}/`
    );
    if (res.ok) {
      const data = await res.json();
      console.log("Fetched match:", data);

      // Обрабатываем данные матча так же, как в MatchCalendar
      match.value = {
        ...data,
        tournament_name: data.tournament?.name ?? "",
        player1_first_name: data.player1?.first_name ?? "",
        player1_last_name: data.player1?.last_name ?? "",
        player2_first_name: data.player2?.first_name ?? "",
        player2_last_name: data.player2?.last_name ?? "",
        winner_first_name: data.winner?.first_name ?? "",
        winner_last_name: data.winner?.last_name ?? "",
      };
    } else {
      match.value = null;
    }
  } catch (e) {
    console.error("Error fetching match:", e);
    match.value = null;
  }
});
</script>
