<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/federation/docs" class="hover:underline"
        >Документы</router-link
      >
      <span> / </span>
      <span class="text-gray-700 font-semibold">{{ doc?.title }}</span>
    </nav>

    <div
      v-if="doc"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <div
        class="w-36 h-36 rounded-full bg-red-100 flex items-center justify-center mb-5 border-4 border-blue-200 shadow"
      >
        <svg
          class="w-16 h-16 text-red-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
          />
        </svg>
      </div>
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900">
        {{ doc.title }}
      </h1>
      <div class="text-lg text-blue-700 font-semibold mb-4 text-center">
        Документ
      </div>
      <div
        class="text-gray-700 text-base mb-4 text-center"
        v-if="doc.description"
      >
        {{ doc.description }}
      </div>
      <a
        v-if="doc.file"
        :href="doc.file"
        download
        class="px-6 py-3 bg-blue-600 text-white text-lg rounded-lg shadow hover:bg-blue-700 transition"
      >
        Скачать документ
      </a>
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
const doc = ref(null);
onMounted(async () => {
  const res = await fetch(
    `http://127.0.0.1:8000/api/documents/${route.params.id}/`
  );
  if (res.ok) doc.value = await res.json();
});
</script>
