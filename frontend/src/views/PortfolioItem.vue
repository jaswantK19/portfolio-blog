<template>
  <section>
    <h2 class="text-2xl font-bold mb-4">Portfolio Item</h2>
    <div v-if="item" class="space-y-2">
      <h3 class="text-xl font-semibold">{{ item.title }}</h3>
      <p class="text-xs text-gray-500">{{ item.created_at }}</p>
      <div class="prose max-w-none text-gray-800" v-html="item.content"></div>
    </div>
    <div v-else class="text-gray-400">Loading...</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getPortfolioItem } from '../api';

const route = useRoute();
const item = ref(null);

onMounted(async () => {
  const res = await getPortfolioItem(route.params.id);
  item.value = res.data;
});
</script>

<style scoped>
/* No purple! */
</style>
