<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="news in newsList"
      :key="news.id"
      :to="`/news/${news.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <img
        v-if="news.image"
        :src="news.image"
        alt="news image"
        class="w-full h-auto object-cover mb-4 border-2 border-blue-300 shadow"
      />
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ news.title }}
      </h3>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="news.content"
      >
        {{ news.content }}
      </p>
      <span class="text-xs text-gray-400 mt-auto" v-if="news.published_at">{{
        new Date(news.published_at).toLocaleDateString()
      }}</span>
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const newsList = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/news/");
  newsList.value = await res.json();
});
</script>
