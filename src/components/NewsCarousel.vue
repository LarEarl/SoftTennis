<template>
  <div
    class="relative w-full h-64 md:h-80 rounded-2xl shadow-xl overflow-hidden group"
  >
    <!-- Фоновое изображение -->
    <div
      v-if="currentNews.image"
      class="absolute inset-0 bg-cover bg-center bg-no-repeat transition-all duration-500"
      :style="{
        backgroundImage: `url(${currentNews.image})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center center',
      }"
    >
      <!-- Темный оверлей -->
      <div class="absolute inset-0 bg-black/40"></div>
    </div>

    <!-- Градиентный фон если нет изображения -->
    <div
      v-else
      class="absolute inset-0 bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800"
    ></div>

    <!-- Стрелка влево -->
    <button
      @click="prev"
      class="absolute left-4 top-1/2 -translate-y-1/2 z-20 bg-white/20 hover:bg-white/30 backdrop-blur-sm text-white p-3 transition-all duration-200 opacity-0 group-hover:opacity-100"
      aria-label="Previous"
    >
      <svg
        class="w-5 h-5"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          d="M15 19l-7-7 7-7"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>

    <!-- Контент -->
    <router-link
      v-if="newsList.length"
      :to="`/news/${currentNews.id}`"
      class="absolute inset-0 flex flex-col justify-end p-6 text-white cursor-pointer z-10"
    >
      <div class="space-y-3">
        <h3 class="text-2xl md:text-3xl font-bold leading-tight">
          {{ currentNews.title }}
        </h3>
        <p
          class="hidden md:block text-gray-200 line-clamp-2 text-sm leading-relaxed"
        >
          {{ currentNews.content }}
        </p>
        <span class="text-xs text-gray-300">
          {{ formatDate(currentNews.published_at) }}
        </span>
      </div>
    </router-link>

    <!-- Стрелка вправо -->
    <button
      @click="next"
      class="absolute right-4 top-1/2 -translate-y-1/2 z-20 bg-white/20 hover:bg-white/30 backdrop-blur-sm text-white p-3 transition-all duration-200 opacity-0 group-hover:opacity-100"
      aria-label="Next"
    >
      <svg
        class="w-5 h-5"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          d="M9 5l7 7-7 7"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        />
      </svg>
    </button>

    <!-- Индикаторы -->
    <div class="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2 z-20">
      <button
        v-for="(n, i) in newsList"
        :key="n.id"
        @click="index = i"
        class="w-8 h-1 rounded-full transition-all duration-300"
        :class="i === index ? 'bg-white' : 'bg-white/40 hover:bg-white/60'"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
const props = defineProps({ newsList: Array });
const index = ref(0);
const currentNews = computed(() => props.newsList?.[index.value] || {});

// Автопрокрутка (опционально)
let timer = null;
onMounted(() => {
  timer = setInterval(() => {
    next();
  }, 7000);
});
watch(
  () => props.newsList,
  () => {
    index.value = 0;
  }
);
function next() {
  index.value = (index.value + 1) % (props.newsList?.length || 1);
}
function prev() {
  index.value =
    (index.value - 1 + (props.newsList?.length || 1)) %
    (props.newsList?.length || 1);
}
function formatDate(dateStr) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}
</script>
