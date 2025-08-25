<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <router-link
      v-for="doc in docs"
      :key="doc.id"
      :to="`/federation/docs/${doc.id}`"
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center cursor-pointer"
    >
      <div
        class="w-24 h-24 rounded-full bg-red-100 flex items-center justify-center mb-4 border-2 border-blue-300 shadow"
      >
        <svg
          class="w-12 h-12 text-red-600"
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
      <h3 class="text-lg font-bold mb-2 text-center break-words">
        {{ doc.title }}
      </h3>
      <p
        class="text-gray-700 line-clamp-3 text-center break-words overflow-hidden"
        v-if="doc.description"
      >
        {{ doc.description }}
      </p>
      <a
        :href="doc.file"
        download
        class="mt-auto px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition text-sm"
        @click.stop
        >Скачать</a
      >
    </router-link>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const docs = ref([]);
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/documents/");
  docs.value = await res.json();
});
</script>
