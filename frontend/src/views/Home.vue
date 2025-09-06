<template>
  <section class="space-y-16">
    <!-- Hero Section -->
    <div class="text-center py-16 bg-gradient-to-br from-gray-50 via-white to-gray-100 -mx-4 px-4 rounded-3xl">
      <div class="max-w-4xl mx-auto">
        <h1 class="text-5xl md:text-6xl font-bold text-gray-900 mb-6 leading-tight">
          Hi, I'm 
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-gray-900 to-black">
            Jaswant Kondur
          </span>
        </h1>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto leading-relaxed">
          Software developer passionate about creating elegant solutions and meaningful digital experiences. Explore my portfolio and thoughts.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link 
            to="/portfolio" 
            class="inline-flex items-center px-8 py-4 bg-black text-white font-semibold rounded-xl hover:bg-gray-800 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            View My Work
            <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
            </svg>
          </router-link>
          <router-link 
            to="/blog" 
            class="inline-flex items-center px-8 py-4 bg-white text-gray-700 font-semibold rounded-xl border-2 border-gray-200 hover:border-gray-400 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            Read My Blog
            <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
            </svg>
          </router-link>
        </div>
      </div>
    </div>

    <!-- Latest Content -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Latest Blog Post -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="p-8">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-2xl font-bold text-gray-900">Latest Blog Post</h3>
            <router-link 
              to="/blog" 
              class="text-black hover:text-gray-700 font-medium flex items-center group"
            >
              View all
              <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
          </div>
          
          <div v-if="latestPost" class="space-y-4">
            <div class="flex items-center space-x-2 text-sm text-gray-500">
              <div class="w-2 h-2 bg-blue-500 rounded-full"></div>
              <span>{{ formatDate(latestPost.created_at) }}</span>
            </div>
            
            <router-link :to="`/blog/${latestPost.id}`" class="block group">
              <h4 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors duration-200 mb-3">
                {{ latestPost.title }}
              </h4>
              <p class="text-gray-600 leading-relaxed line-clamp-3">
                {{ latestPost.content.substring(0, 150) }}{{ latestPost.content.length > 150 ? '...' : '' }}
              </p>
            </router-link>
            
            <router-link 
              :to="`/blog/${latestPost.id}`" 
              class="inline-flex items-center text-blue-600 hover:text-blue-700 font-medium group"
            >
              Read more
              <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
          </div>
          
          <div v-else class="text-center py-8">
            <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
              </svg>
            </div>
            <p class="text-gray-500">No blog posts yet</p>
          </div>
        </div>
      </div>

      <!-- Latest Portfolio Item -->
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="p-8">
          <div class="flex items-center justify-between mb-6">
            <h3 class="text-2xl font-bold text-gray-900">Latest Project</h3>
            <router-link 
              to="/portfolio" 
              class="text-blue-600 hover:text-blue-700 font-medium flex items-center group"
            >
              View all
              <svg class="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
          </div>
          
          <div v-if="latestPortfolio" class="space-y-4">
            <div class="aspect-video bg-gradient-to-br from-blue-50 to-indigo-100 rounded-xl flex items-center justify-center">
              <img 
                v-if="latestPortfolio.image_url" 
                :src="latestPortfolio.image_url" 
                :alt="latestPortfolio.name"
                class="w-full h-full object-cover rounded-xl"
              />
              <div v-else>
                <svg class="w-12 h-12 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                </svg>
              </div>
            </div>
            
            <div class="flex items-center space-x-2 text-sm text-gray-500">
              <div class="w-2 h-2 bg-green-500 rounded-full"></div>
              <span>{{ formatDate(latestPortfolio.created_at) }}</span>
            </div>
            
            <router-link :to="`/portfolio/${latestPortfolio.id}`" class="block group">
              <h4 class="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors duration-200 mb-3">
                {{ latestPortfolio.name }}
              </h4>
              <p class="text-gray-600 leading-relaxed line-clamp-2">
                {{ latestPortfolio.description || 'No description available' }}
              </p>
            </router-link>
            
            <div class="flex items-center justify-between">
              <router-link 
                :to="`/portfolio/${latestPortfolio.id}`" 
                class="inline-flex items-center text-blue-600 hover:text-blue-700 font-medium group"
              >
                View project
                <svg class="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                </svg>
              </router-link>
              
              <a 
                v-if="latestPortfolio.link" 
                :href="latestPortfolio.link" 
                target="_blank"
                class="inline-flex items-center text-gray-600 hover:text-gray-700 font-medium"
              >
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
                </svg>
                Live demo
              </a>
            </div>
          </div>
          
          <div v-else class="text-center py-8">
            <div class="w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
              </svg>
            </div>
            <p class="text-gray-500">No portfolio items yet</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getPosts, getPortfolio } from '../api';

const latestPost = ref(null);
const latestPortfolio = ref(null);

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
    const postsRes = await getPosts();
    latestPost.value = postsRes.data.length ? postsRes.data[0] : null;
    
    const portfolioRes = await getPortfolio();
    latestPortfolio.value = portfolioRes.data.length ? portfolioRes.data[0] : null;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
</script>

<style scoped>
/* No purple! */
</style>
