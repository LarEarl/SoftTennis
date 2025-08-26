<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/players" class="hover:underline">Игроки</router-link>
      <span> / </span>
      <span class="text-gray-700 font-semibold"
        >{{ player?.first_name }} {{ player?.last_name }}</span
      >
    </nav>

    <div
      v-if="player"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <img
        v-if="player.photo"
        :src="player.photo"
        class="w-36 h-36 rounded-full object-cover mb-5 border-4 border-blue-200 shadow"
        alt="Фото игрока"
      />
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900 break-words">
        {{ player.first_name }} {{ player.last_name }}
      </h1>
      <div
        class="text-lg text-blue-700 font-semibold mb-4 text-center break-words"
      >
        Рейтинг: {{ player.rank }}
      </div>
      <div class="text-gray-700 text-base mb-4 text-center max-w-full">
        <div class="mb-2 break-words"><b>Страна:</b> {{ player.country }}</div>
        <div class="mb-2 break-words">
          <b>Дата рождения:</b> {{ player.birth_date }}
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
const player = ref(null);

onMounted(async () => {
  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/players/${route.params.id}/`
    );
    if (res.ok) {
      player.value = await res.json();
    } else {
      player.value = null;
    }
  } catch (e) {
    player.value = null;
  }
});
</script>
