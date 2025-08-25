<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/news" class="hover:underline">Новости</router-link>
      <span> / </span>
      <span class="text-gray-700 font-semibold">{{ news?.title }}</span>
    </nav>

    <div
      v-if="news"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <img
        v-if="news.image"
        :src="news.image"
        class="w-full h-auto object-cover mb-5 border-4 border-blue-200 shadow"
        alt="Изображение новости"
      />
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900 break-words">
        {{ news.title }}
      </h1>
      <div
        class="text-lg text-blue-700 font-semibold mb-4 text-center break-words"
      >
        {{ formatDate(news.published_at) }}
      </div>
      <div
        class="text-gray-700 text-base mb-4 text-center whitespace-pre-line break-words overflow-hidden max-w-full"
      >
        {{ news.content }}
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
const news = ref(null);

function formatDate(dateStr) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleString();
}

onMounted(async () => {
  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/news/${route.params.id}/`
    );
    if (res.ok) {
      news.value = await res.json();
    } else {
      news.value = null;
    }
  } catch (e) {
    news.value = null;
  }
});
</script>
