<template>
  <section class="max-w-4xl mx-auto">
    <div class="mb-8">
      <h2 class="text-4xl font-bold text-gray-900 mb-2">Blog</h2>
      <p class="text-lg text-gray-600">Thoughts, insights, and experiences from my journey</p>
    </div>
    
    <div v-if="posts.length" class="space-y-8">
      <article 
        v-for="post in posts" 
        :key="post.id" 
        class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-lg transition-all duration-300 group"
      >
        <div class="p-8">
          <div class="flex items-center justify-between mb-4">
            <div class="flex items-center space-x-2">
              <div class="w-2 h-2 bg-black rounded-full"></div>
              <span class="text-sm text-gray-500 uppercase tracking-wide font-medium">Blog Post</span>
            </div>
            <time class="text-sm text-gray-400">{{ formatDate(post.created_at) }}</time>
          </div>
          
          <router-link :to="`/blog/${post.id}`" class="block mb-4">
            <h3 class="text-2xl font-bold text-gray-900 group-hover:text-black transition-colors duration-200 mb-3">
              {{ post.title }}
            </h3>
          </router-link>
          
          <p class="text-gray-600 leading-relaxed mb-6 line-clamp-3">
            {{ post.content.substring(0, 200) }}{{ post.content.length > 200 ? '...' : '' }}
          </p>
          
          <div class="flex items-center justify-between">
            <router-link 
              :to="`/blog/${post.id}`" 
              class="inline-flex items-center text-black hover:text-gray-700 font-medium group/link"
            >
              Read more
              <svg class="w-4 h-4 ml-2 group-hover/link:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
            
            <div class="flex items-center space-x-4 text-sm text-gray-400">
              <span v-if="post.published" class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                Published
              </span>
            </div>
          </div>
        </div>
      </article>
    </div>
    
    <div v-else class="text-center py-16">
      <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
        <svg class="w-12 h-12 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
        </svg>
      </div>
      <h3 class="text-xl font-medium text-gray-900 mb-2">No blog posts yet</h3>
      <p class="text-gray-500">Stay tuned for upcoming articles and insights!</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getPosts } from '../api';

const posts = ref([]);

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
};

onMounted(async () => {
  try {
    const res = await getPosts();
    posts.value = res.data;
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
});
</script>

<style scoped>
/* No purple! */
</style>
