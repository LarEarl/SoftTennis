<template>
  <div class="news-carousel">
    <transition name="fade-slide-carousel" mode="out-in">
      <div class="news-carousel__image-block" :key="currentNews.id">
        <img
          v-if="currentNews.image"
          :src="currentNews.image"
          class="news-carousel__image"
          alt="news image"
        />
        <div v-else class="news-carousel__noimage"></div>
        <div class="news-carousel__overlay"></div>
      </div>
    </transition>
    <button
      class="news-carousel__arrow news-carousel__arrow--left"
      @click="prev"
      aria-label="Previous"
    >
      <svg
        width="22"
        height="22"
        viewBox="0 0 320 512"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M216 464c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L109.3 256l129.4 129.4c12.5 12.5 12.5 32.75 0 45.25C232.4 460.9 224.2 464 216 464z"
          fill="currentColor"
        />
      </svg>
    </button>
    <button
      class="news-carousel__arrow news-carousel__arrow--right"
      @click="next"
      aria-label="Next"
    >
      <svg
        width="22"
        height="22"
        viewBox="0 0 320 512"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M104 48c8.188 0 16.38 3.125 22.62 9.375l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160c-12.5 12.5-32.75 12.5-45.25 0s-12.5-32.75 0-45.25L210.7 256 81.31 126.6c-12.5-12.5-12.5-32.75 0-45.25C87.62 51.13 95.81 48 104 48z"
          fill="currentColor"
        />
      </svg>
    </button>
    <router-link
      v-if="newsList.length"
      :to="`/news/${currentNews.id}`"
      class="news-carousel__content"
    >
      <h3 class="news-carousel__title">{{ currentNews.title }}</h3>
      <!-- <p class="news-carousel__desc">{{ currentNews.content }}</p> -->
      <span class="news-carousel__date">{{
        formatDate(currentNews.published_at)
      }}</span>
    </router-link>
    <div class="news-carousel__indicators">
      <button
        v-for="(n, i) in newsList"
        :key="n.id"
        @click="index = i"
        :class="['news-carousel__indicator', { active: i === index }]"
      ></button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
const props = defineProps({ newsList: Array });
const index = ref(0);
const currentNews = computed(() => props.newsList?.[index.value] || {});

function next() {
  index.value = (index.value + 1) % (props.newsList?.length || 1);
}
function prev() {
  index.value =
    (index.value - 1 + (props.newsList?.length || 1)) %
    (props.newsList?.length || 1);
}
watch(
  () => props.newsList,
  () => {
    index.value = 0;
  }
);
function formatDate(dateStr) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}
</script>

<style scoped>
.news-carousel {
  position: relative;
  width: 100%;
  height: 26rem;
  max-width: 100%;
  border-radius: 1.5rem;
  overflow: hidden;
  box-shadow: 0 4px 32px 0 rgba(0, 0, 0, 0.12);
  background: #222;
}
.news-carousel__image-block {
  width: 100%;
  height: 100%;
  position: relative;
}
.news-carousel__image {
  width: 100%;
  height: 100%;
  object-fit: fill;
  display: block;
  background: #222;
}
.news-carousel__noimage {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
}
.news-carousel__overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.35);
}
.news-carousel__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  /* background: rgba(255, 255, 255, 0.18); */
  color: #fff;
  border: none;
  font-size: 2rem;
  padding: 0.5rem 1rem;
  border-radius: 50%;
  cursor: pointer;
  transition: background 0.2s;
}
.news-carousel__arrow--left {
  left: 1rem;
}
.news-carousel__arrow--right {
  right: 1rem;
}
.news-carousel__arrow:hover {
  background: rgba(255, 255, 255, 0.32);
}
.news-carousel__content {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 3;
  color: #fff;
  padding: 2rem 2rem 1.5rem 2rem;
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.55) 60%,
    rgba(0, 0, 0, 0.05) 100%
  );
  text-decoration: none;
  border-bottom-left-radius: 1.5rem;
  border-bottom-right-radius: 1.5rem;
}
.news-carousel__title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  line-height: 1.1;
}
.news-carousel__desc {
  font-size: 1rem;
  color: #e5e7eb;
  margin-bottom: 0.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 4.5em;
}
.news-carousel__date {
  font-size: 0.85rem;
  color: #cbd5e1;
}
.news-carousel__indicators {
  position: absolute;
  left: 50%;
  bottom: 1rem;
  transform: translateX(-50%);
  display: flex;
  gap: 0.5rem;
  z-index: 4;
}
.news-carousel__indicator {
  width: 2.5rem;
  height: 0.3rem;
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.4);
  border: none;
  transition: background 0.2s;
  cursor: pointer;
}
.news-carousel__indicator.active {
  background: #fff;
}
</style>
<style scoped>
.fade-slide-carousel-enter-active,
.fade-slide-carousel-leave-active {
  transition: opacity 0.4s, transform 0.4s;
}
.fade-slide-carousel-enter-from {
  opacity: 0;
  transform: translateX(40px);
}
.fade-slide-carousel-leave-to {
  opacity: 0;
  transform: translateX(-40px);
}
.fade-slide-carousel-enter-to,
.fade-slide-carousel-leave-from {
  opacity: 1;
  transform: translateX(0);
}
</style>
