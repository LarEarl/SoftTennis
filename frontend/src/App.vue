<template>
  <div
    class="min-h-screen bg-gradient-to-b from-blue-50 to-white flex flex-col"
  >
    <!-- Навигация -->
    <nav class="bg-white/95 shadow sticky top-0 z-30 backdrop-blur">
      <div
        class="max-w-7xl mx-auto flex justify-between items-center px-4 py-2"
      >
        <router-link
          to="/"
          class="text-blue-800 font-bold text-2xl tracking-wide"
          >Федерация падел тенниса</router-link
        >
        <div class="flex gap-2 md:gap-6 items-center">
          <!-- Бургер и выпадающее меню -->
          <div class="relative">
            <button
              class="flex items-center gap-1 text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium focus:outline-none"
              @click="showFederationMenu = !showFederationMenu"
              @blur="onBlurFederationMenu"
            >
              <span class="hidden md:inline">Федерация</span>
              <span class="md:hidden">
                <span :class="['burger', { open: showFederationMenu }]">
                  <span></span><span></span><span></span>
                </span>
              </span>
              <svg
                class="w-4 h-4 ml-1 transition-transform duration-300"
                :class="{ 'rotate-180': showFederationMenu }"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  d="M19 9l-7 7-7-7"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                />
              </svg>
            </button>
            <transition name="fade-slide">
              <div
                v-if="showFederationMenu"
                class="absolute left-0 mt-2 w-48 bg-white rounded shadow-lg animate-fade-in z-20 py-2"
                @mousedown.prevent
              >
                <router-link
                  to="/federation/leadership"
                  class="block px-4 py-2 text-gray-700 hover:bg-blue-50 transition"
                  @click="showFederationMenu = false"
                  >Руководство</router-link
                >
                <router-link
                  to="/federation/team"
                  class="block px-4 py-2 text-gray-700 hover:bg-blue-50 transition"
                  @click="showFederationMenu = false"
                  >Наша команда</router-link
                >
                <router-link
                  to="/federation/docs"
                  class="block px-4 py-2 text-gray-700 hover:bg-blue-50 transition"
                  @click="showFederationMenu = false"
                  >Документы</router-link
                >
                <router-link
                  to="/federation/contacts"
                  class="block px-4 py-2 text-gray-700 hover:bg-blue-50 transition"
                  @click="showFederationMenu = false"
                  >Контакты</router-link
                >
              </div>
            </transition>
          </div>
          <router-link
            to="/news"
            class="text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium"
            >Новости</router-link
          >
          <router-link
            to="/tournaments"
            class="text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium"
            >Турниры</router-link
          >
          <router-link
            to="/players"
            class="text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium"
            >Игроки</router-link
          >
          <router-link
            to="/matches"
            class="text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium"
            >Матчи</router-link
          >
        </div>
      </div>
    </nav>
    <main class="flex-1 max-w-7xl mx-auto px-4 py-8 w-full">
      <router-view />
    </main>
    <footer class="bg-blue-900 text-white py-6">
      <div class="max-w-7xl mx-auto text-center text-sm">
        © 2025 Федерация падел тенниса. Все права защищены.
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from "vue";
const showFederationMenu = ref(false);
function onBlurFederationMenu(e) {
  setTimeout(() => (showFederationMenu.value = false), 120);
}
</script>

<style scoped>
.burger {
  display: inline-block;
  width: 24px;
  height: 20px;
  position: relative;
  transition: all 0.3s cubic-bezier(0.4, 2, 0.3, 1);
}
.burger span {
  display: block;
  position: absolute;
  height: 3px;
  width: 100%;
  background: #2563eb;
  border-radius: 2px;
  opacity: 1;
  left: 0;
  transition: all 0.3s cubic-bezier(0.4, 2, 0.3, 1);
}
.burger span:nth-child(1) {
  top: 0;
}
.burger span:nth-child(2) {
  top: 8px;
}
.burger span:nth-child(3) {
  top: 16px;
}
.burger.open span:nth-child(1) {
  transform: rotate(45deg);
  top: 8px;
}
.burger.open span:nth-child(2) {
  opacity: 0;
}
.burger.open span:nth-child(3) {
  transform: rotate(-45deg);
  top: 8px;
}
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: opacity 0.25s, transform 0.25s;
}
.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
.fade-slide-enter-to,
.fade-slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}
</style>
