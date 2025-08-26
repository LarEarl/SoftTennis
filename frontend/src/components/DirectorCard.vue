<template>
  <div class="director-card">
    <div
      class="director-card__bg"
      :style="
        director.photo ? { backgroundImage: `url(${director.photo})` } : {}
      "
    >
      <div class="director-card__overlay"></div>
      <div class="director-card__content">
        <div class="director-card__name">{{ director.name }}</div>
        <div class="director-card__position">{{ director.position }}</div>
        <div class="director-card__bio">{{ director.bio }}</div>
        <span v-if="director.email" class="director-card__email">
          <a :href="`mailto:${director.email}`">{{ director.email }}</a>
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const director = ref({});
onMounted(async () => {
  // Получаем первого руководителя (предполагаем, что директор всегда первый)
  const res = await fetch("http://127.0.0.1:8000/api/leadership/");
  const data = await res.json();
  director.value = data?.[0] || {};
});
</script>

<style scoped>
.director-card {
  background: #fff;
  border-radius: 1.5rem;
  box-shadow: 0 6px 32px 0 rgba(30, 64, 175, 0.1),
    0 1.5px 6px 0 rgba(30, 64, 175, 0.08);
  min-height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: stretch;
}
.director-card__bg {
  position: relative;
  width: 100%;
  height: 100%;
  min-height: 24rem;
  background: #e5e7eb;
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: end;
  justify-content: center;
}
.director-card__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    0deg,
    rgba(30, 41, 59, 0.82) 0%,
    rgba(30, 41, 59, 0.18) 100%
  );
  z-index: 1;
}
.director-card__content {
  position: relative;
  z-index: 2;
  width: 100%;
  padding: 2.5rem 1.5rem 0 1.5rem;
  text-align: center;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.director-card__name {
  font-size: 1.6rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.2rem;
  text-shadow: 0 2px 8px rgba(30, 41, 59, 0.18);
}
.director-card__position {
  color: #c7d2fe;
  font-weight: 600;
  margin-bottom: 0.7rem;
  font-size: 1.1rem;
  text-shadow: 0 2px 8px rgba(30, 41, 59, 0.12);
}
.director-card__bio {
  color: #e0e7ef;
  font-size: 1rem;
  margin-bottom: 0.7rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  /* min-height: 3.5em; */
  text-shadow: 0 2px 8px rgba(30, 41, 59, 0.1);
}
.director-card__email {
  font-size: 0.95rem;
  color: #cbd5e1;
  margin-top: 0.5rem;
  display: block;
}
.director-card__email a {
  color: #facc15;
  text-decoration: underline;
  transition: color 0.2s;
}
.director-card__email a:hover {
  color: #fde047;
}
</style>
