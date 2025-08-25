<template>
  <div class="grid gap-7 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
    <div
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center"
    >
      <div
        class="w-24 h-24 rounded-full bg-blue-100 flex items-center justify-center mb-4 border-2 border-blue-300 shadow"
      >
        <svg
          class="w-12 h-12 text-blue-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
          />
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
          />
        </svg>
      </div>
      <h3 class="text-lg font-bold mb-2 text-center">Адрес</h3>
      <p class="text-gray-700 text-center">{{ contacts.address }}</p>
    </div>

    <div
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center"
    >
      <div
        class="w-24 h-24 rounded-full bg-green-100 flex items-center justify-center mb-4 border-2 border-blue-300 shadow"
      >
        <svg
          class="w-12 h-12 text-green-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
          />
        </svg>
      </div>
      <h3 class="text-lg font-bold mb-2 text-center">Телефон</h3>
      <a
        :href="`tel:${contacts.phone}`"
        class="text-blue-700 hover:underline text-center"
        >{{ contacts.phone }}</a
      >
    </div>

    <div
      class="bg-white rounded-xl shadow-md hover:shadow-xl transition p-6 flex flex-col items-center"
    >
      <div
        class="w-24 h-24 rounded-full bg-purple-100 flex items-center justify-center mb-4 border-2 border-blue-300 shadow"
      >
        <svg
          class="w-12 h-12 text-purple-600"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
          />
        </svg>
      </div>
      <h3 class="text-lg font-bold mb-2 text-center">Электронная почта</h3>
      <a
        :href="`mailto:${contacts.email}`"
        class="text-blue-700 hover:underline text-center"
        >{{ contacts.email }}</a
      >
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const contacts = ref({});
onMounted(async () => {
  const res = await fetch("http://127.0.0.1:8000/api/contacts/");
  const data = await res.json();
  contacts.value = data[0] || {};
});
</script>
