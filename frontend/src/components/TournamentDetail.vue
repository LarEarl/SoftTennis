<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/tournaments" class="hover:underline"
        >Турниры</router-link
      >
      <span> / </span>
      <span class="text-gray-700 font-semibold">{{ tournament?.name }}</span>
    </nav>

    <div
      v-if="tournament"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <img
        v-if="tournament.logo"
        :src="tournament.logo"
        class="w-36 h-36 rounded-full object-cover mb-5 border-4 border-blue-200 shadow"
        alt="Логотип турнира"
      />
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900 break-words">
        {{ tournament.name }}
      </h1>
      <div
        class="text-lg text-blue-700 font-semibold mb-4 text-center break-words"
      >
        {{ tournament.location }}
      </div>
      <div class="text-gray-700 text-base mb-4 text-center max-w-full">
        <div class="mb-2 break-words">
          <b>Сроки:</b> {{ tournament.start_date }} — {{ tournament.end_date }}
        </div>
        <div
          v-if="tournament.description"
          class="whitespace-pre-line break-words overflow-hidden"
        >
          {{ tournament.description }}
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
const tournament = ref(null);

onMounted(async () => {
  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/tournaments/${route.params.id}/`
    );
    if (res.ok) {
      tournament.value = await res.json();
    } else {
      tournament.value = null;
    }
  } catch (e) {
    tournament.value = null;
  }
});
</script>
