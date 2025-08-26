<template>
  <div class="max-w-3xl mx-auto">
    <!-- Breadcrumbs -->
    <nav class="text-sm mb-6 text-gray-500">
      <router-link to="/" class="hover:underline">Главная</router-link>
      <span> / </span>
      <router-link to="/federation/team" class="hover:underline"
        >Наша команда</router-link
      >
      <span> / </span>
      <span class="text-gray-700 font-semibold">{{ member?.name }}</span>
    </nav>

    <div
      v-if="member"
      class="bg-white rounded-2xl shadow-xl p-8 flex flex-col items-center"
    >
      <img
        v-if="member.photo"
        :src="member.photo"
        class="w-36 h-36 rounded-full object-cover mb-5 border-4 border-blue-200 shadow"
        alt="Фото члена команды"
      />
      <h1 class="text-3xl font-bold mb-1 text-center text-blue-900">
        {{ member.name }}
      </h1>
      <div class="text-lg text-blue-700 font-semibold mb-4 text-center">
        {{ member.role }}
      </div>
      <div
        v-if="member.bio"
        class="text-gray-700 text-base mb-4 text-center whitespace-pre-line"
      >
        {{ member.bio }}
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
const member = ref(null);
onMounted(async () => {
  const res = await fetch(`http://127.0.0.1:8000/api/team/${route.params.id}/`);
  if (res.ok) member.value = await res.json();
});
</script>
