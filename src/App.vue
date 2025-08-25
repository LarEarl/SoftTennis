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
          >Теннисная Федерация</router-link
        >
        <div class="flex gap-2 md:gap-6 items-center">
          <!-- Пример выпадающего пункта -->
          <div class="relative group">
            <button
              class="flex items-center gap-1 text-blue-700 hover:bg-blue-100 rounded px-3 py-2 transition font-medium"
            >
              Федерация
              <svg
                class="w-4 h-4"
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
            <div
              class="absolute left-0 mt-2 w-44 bg-white rounded shadow-lg opacity-0 group-hover:opacity-100 pointer-events-none group-hover:pointer-events-auto transition-opacity z-20"
            >
              <router-link
                to="/federation/leadership"
                class="block px-4 py-2 text-gray-700 hover:bg-blue-50"
                >Руководство</router-link
              >
              <router-link
                to="/federation/team"
                class="block px-4 py-2 text-gray-700 hover:bg-blue-50"
                >Наша команда</router-link
              >
              <router-link
                to="/federation/docs"
                class="block px-4 py-2 text-gray-700 hover:bg-blue-50"
                >Документы</router-link
              >
              <router-link
                to="/federation/contacts"
                class="block px-4 py-2 text-gray-700 hover:bg-blue-50"
                >Контакты</router-link
              >
            </div>
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
        © 2025 Теннисная Федерация. Все права защищены.
      </div>
    </footer>
  </div>
</template>
