<template>
  <div>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- ВЕРХНЯЯ СЕКЦИЯ -->
      <div class="lg:col-span-2 flex flex-col gap-6">
        <NewsCarousel :newsList="carouselNewsList" />
      </div>
      <div class="flex flex-col gap-6">
        <DirectorCard />
      </div>
    </div>

    <!-- ОСНОВНАЯ СЕТКА -->
    <div class="mt-8 grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Левая колонка: Новости -->
      <section class="lg:col-span-2">
        <h2 class="text-2xl font-bold mb-4">Свежие новости</h2>
        <div class="space-y-5">
          <router-link
            v-for="news in newsList"
            :key="news.id"
            :to="`/news/${news.id}`"
            class="block bg-white rounded-xl shadow hover:shadow-lg transition p-6"
          >
            <div class="flex flex-col md:flex-row md:items-center gap-4">
              <div
                v-if="news.image"
                class="w-full md:w-44 aspect-video bg-gray-100 flex-shrink-0 rounded mb-3 md:mb-0 md:mr-4 overflow-hidden"
              >
                <img
                  :src="news.image"
                  class="w-full h-full object-contain object-center bg-white"
                  alt="news image"
                />
              </div>
              <div>
                <h3 class="text-lg font-bold mb-2">{{ news.title }}</h3>
                <span class="text-xs text-gray-400">{{
                  formatDate(news.published_at)
                }}</span>
              </div>
            </div>
          </router-link>
        </div>
      </section>

      <!-- Правая колонка: Рейтинг игроков и Календарь матчей -->
      <aside class="flex flex-col gap-8">
        <!-- Рейтинг игроков -->
        <div class="bg-white rounded-xl shadow p-6">
          <h2 class="text-xl font-bold mb-4 text-center">Рейтинг игроков</h2>
          <div class="divide-y">
            <router-link
              v-for="player in topPlayers"
              :key="player.id"
              :to="`/players/${player.id}`"
              class="flex items-center gap-3 py-3 hover:bg-blue-50 rounded transition"
            >
              <img
                v-if="player.photo"
                :src="player.photo"
                class="w-10 h-10 rounded-full object-cover border-2 border-blue-200"
              />
              <div class="flex-1">
                <span class="font-semibold"
                  >{{ player.first_name }} {{ player.last_name }}</span
                >
                <span class="text-xs text-gray-400 ml-2">{{
                  player.country
                }}</span>
              </div>
              <span class="font-bold text-blue-700">{{ player.rank }}</span>
            </router-link>
          </div>
        </div>

        <!-- Календарь матчей -->
        <div class="bg-white rounded-xl shadow p-6">
          <h2 class="text-xl font-bold mb-4 text-center">Ближайшие матчи</h2>
          <div v-if="limitedMatches.length" class="space-y-3">
            <div
              v-for="match in limitedMatches"
              :key="match.id"
              class="bg-blue-50 rounded-lg px-3 py-2 flex flex-col"
            >
              <div class="flex items-center text-xs text-gray-500 mb-0.5">
                <span>{{ formatDate(match.date) }}</span>
                <span
                  class="ml-auto px-2 py-0.5 rounded"
                  :class="
                    match.score
                      ? 'bg-green-100 text-green-700'
                      : 'bg-gray-200 text-gray-600'
                  "
                >
                  {{ match.score ? "Завершён" : "Скоро" }}
                </span>
              </div>
              <router-link
                :to="`/matches/${match.id}`"
                class="grid grid-cols-3 gap-2 items-center mt-1 hover:underline"
              >
                <span class="text-blue-800 font-medium text-left truncate">
                  {{ match.player1_first_name }}
                  <!-- {{ match.player1_last_name }} -->
                </span>
                <span class="mx-2 text-gray-400 text-center">vs</span>
                <span class="text-blue-800 font-medium text-right truncate">
                  {{ match.player2_first_name }}
                  <!-- {{ match.player2_last_name }} -->
                </span>
              </router-link>
              <div class="text-xs text-gray-500">
                Турнир:
                <template
                  v-if="
                    typeof match.tournament === 'object' && match.tournament
                  "
                >
                  <router-link
                    v-if="match.tournament.id"
                    :to="`/tournaments/${match.tournament.id}`"
                    class="text-blue-700 hover:underline font-medium"
                  >
                    {{ match.tournament.name }}
                  </router-link>
                  <span v-else>{{ match.tournament.name }}</span>
                </template>
                <template v-else>
                  <span>{{ match.tournament }}</span>
                </template>
              </div>
              <div
                v-if="match.score"
                class="text-sm text-green-600 font-semibold"
              >
                Счёт: {{ match.score }}
              </div>
            </div>
          </div>
          <div v-else class="text-gray-400 text-center py-6">
            Нет ближайших матчей.
          </div>
        </div>
      </aside>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import NewsCarousel from "../components/NewsCarousel.vue";
import DirectorCard from "../components/DirectorCard.vue";

// Новости
const newsList = ref([]);
const carouselNewsList = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/news/");
  const data = await res.json();
  newsList.value = data;
  carouselNewsList.value = data.slice(0, 5);
});

// Топ-игроки
const playerList = ref([]);
const topPlayers = computed(() =>
  playerList.value
    .slice()
    .sort((b, a) => a.rank - b.rank)
    .slice(0, 5)
);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/players/");
  const data = await res.json();
  playerList.value = data.map((player) => ({
    ...player,
    first_name: player.first_name ?? "",
    last_name: player.last_name ?? "",
    photo: player.photo ?? "",
    country: player.country ?? "",
    rank: player.rank ?? "",
  }));
});

// Календарь матчей
const matchList = ref([]);
const limit = 3;
const limitedMatches = computed(() =>
  limit ? matchList.value.slice(0, limit) : matchList.value
);

onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/matches/");
  let data = await res.json();
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

function formatDate(dateStr) {
  if (!dateStr) return "";
  const date = new Date(dateStr);
  return date.toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}
</script>
