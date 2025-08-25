<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/federation/leadership" class="hover:underline"
        >Руководство</router-link
      >
      <span> / </span>
      <span class="text-gray-700 font-semibold">{{ leader?.name }}</span>
    </nav>

    <div
      v-if="leader"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <img
        v-if="leader.photo"
        :src="leader.photo"
        class="w-36 h-36 rounded-full object-cover mb-5 border-4 border-blue-200 shadow"
        alt="Фото руководителя"
      />
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900">
        {{ leader.name }}
      </h1>
      <div class="text-lg text-blue-700 font-semibold mb-4 text-center">
        {{ leader.position }}
      </div>
      <div
        v-if="leader.bio"
        class="text-gray-700 text-base mb-4 text-center whitespace-pre-line"
      >
        {{ leader.bio }}
      </div>
      <!-- Пример социальных сетей (если добавишь на бэкенде) -->
      <!--
      <div class="flex gap-3 mt-3">
        <a v-if="leader.vk" :href="leader.vk" target="_blank" class="text-blue-700 hover:underline">VK</a>
        <a v-if="leader.telegram" :href="leader.telegram" target="_blank" class="text-blue-700 hover:underline">Telegram</a>
      </div>
      -->
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
const leader = ref(null);
onMounted(async () => {
  const res = await fetch(
    `http://127.0.0.1:8000/api/leadership/${route.params.id}/`
  );
  if (res.ok) leader.value = await res.json();
});
</script>
