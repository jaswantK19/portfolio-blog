<template>
  <section>
    <h2 class="text-2xl font-bold mb-4">Post</h2>
    <div v-if="post" class="space-y-2">
      <h3 class="text-xl font-semibold">{{ post.title }}</h3>
      <p class="text-xs text-gray-500">{{ post.created_at }}</p>
      <div class="prose max-w-none text-gray-800" v-html="post.content"></div>
    </div>
    <div v-else class="text-gray-400">Loading...</div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getPost } from '../api';

const route = useRoute();
const post = ref(null);

onMounted(async () => {
  const res = await getPost(route.params.id);
  post.value = res.data;
});
</script>

<style scoped>
/* No purple! */
</style>
