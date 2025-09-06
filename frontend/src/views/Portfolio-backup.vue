<template>
          <!-- Image placeholde              <router-link 
                :to="`/portfolio/${item.id}`"
                class="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors border border-gray-200"
              >
                View Details
              </router-link>
              <a 
                v-if="item.link" 
<template>
  <section class="max-w-6xl mx-auto">
    <div class="mb-12 text-center">
      <h2 class="text-4xl font-bold text-gray-900 mb-4">Portfolio</h2>
      <p class="text-lg text-gray-600 max-w-2xl mx-auto">A collection of projects that showcase my skills, creativity, and passion for development</p>
    </div>
    
    <div v-if="items.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <div 
        v-for="item in items" 
        :key="item.id" 
        class="group bg-white rounded-2xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-xl hover:scale-[1.02] transition-all duration-300"
      >
        <!-- Image placeholder or actual image -->
        <div class="aspect-video bg-gradient-to-br from-gray-50 to-gray-100 relative overflow-hidden">
          <img 
            v-if="item.image_url" 
            :src="item.image_url" 
            :alt="item.name"
            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
          />
          <div v-else class="w-full h-full flex items-center justify-center">
            <svg class="w-16 h-16 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
            </svg>
          </div>
          
          <!-- Overlay with quick actions -->
          <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-300 flex items-center justify-center">
            <div class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex space-x-3">
              <router-link 
                :to="`/portfolio/${item.id}`"
                class="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors border border-gray-200"
              >
                View Details
              </router-link>
              <a 
                v-if="item.link" 
                :href="item.link" 
                target="_blank"
                class="bg-black text-white px-4 py-2 rounded-lg font-medium hover:bg-gray-800 transition-colors"
              >
                Live Demo
              </a>
            </div>
          </div>
        </div>
        
        <div class="p-6">
          <div class="mb-4">
            <router-link :to="`/portfolio/${item.id}`">
              <h3 class="text-xl font-bold text-gray-900 group-hover:text-black transition-colors duration-200 mb-2">
                {{ item.name }}
              </h3>
            </router-link>
            <p class="text-gray-600 leading-relaxed line-clamp-3">
              {{ item.description || 'No description available' }}
            </p>
          </div>
          
          <!-- Tags -->
          <div v-if="item.tags && item.tags.length" class="flex flex-wrap gap-2 mb-4">
            <span 
              v-for="tag in item.tags.slice(0, 3)" 
              :key="tag"
              class="inline-block px-3 py-1 bg-gray-100 text-gray-700 text-sm font-medium rounded-full"
            >
              {{ tag }}
            </span>
            <span 
              v-if="item.tags.length > 3"
              class="inline-block px-3 py-1 bg-gray-200 text-gray-600 text-sm font-medium rounded-full"
            >
              +{{ item.tags.length - 3 }} more
            </span>
          </div>
          
          <div class="flex items-center justify-between">
            <router-link 
              :to="`/portfolio/${item.id}`" 
              class="inline-flex items-center text-black hover:text-gray-700 font-medium group/link"
            >
              Learn more
              <svg class="w-4 h-4 ml-2 group-hover/link:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
            
            <time class="text-sm text-gray-400">{{ formatDate(item.created_at) }}</time>
          </div>
        </div>
      </div>
    </div>
    
    <div v-else class="text-center py-20">
      <div class="w-32 h-32 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
        </svg>
      </div>
      <h3 class="text-2xl font-bold text-gray-900 mb-4">No portfolio items yet</h3>
      <p class="text-gray-500 text-lg">Projects and work samples will be showcased here soon!</p>
    </div>
  </section>
</template>
          </div>
          
          <!-- Overlay with quick actions -->
          <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-300 flex items-center justify-center">
            <div class="opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex space-x-3">
              <router-link 
                :to="`/portfolio/${item.id}`"
                class="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors"
              >
                View Details
              </router-link>
              <a 
                v-if="item.link" 
                :href="item.link" 
                target="_blank"
                class="bg-black text-white px-4 py-2 rounded-lg font-medium hover:bg-gray-800 transition-colors"
              >
                Live Demo
              </a>
            </div>
          </div>
        </div>
        
        <div class="p-6">
          <div class="mb-4">
            <router-link :to="`/portfolio/${item.id}`">
              <h3 class="text-xl font-bold text-gray-900 group-hover:text-black transition-colors duration-200 mb-2">
                {{ item.name }}
              </h3>
            </router-link>
            <p class="text-gray-600 leading-relaxed line-clamp-3">
              {{ item.description || 'No description available' }}
            </p>
          </div>
          
          <!-- Tags -->
          <div v-if="item.tags && item.tags.length" class="flex flex-wrap gap-2 mb-4">
            <span 
              v-for="tag in item.tags.slice(0, 3)" 
              :key="tag"
              class="inline-block px-3 py-1 bg-gray-100 text-gray-800 text-sm font-medium rounded-full"
            >
              {{ tag }}
            </span>
            <span 
              v-if="item.tags.length > 3"
              class="inline-block px-3 py-1 bg-gray-200 text-gray-600 text-sm font-medium rounded-full"
            >
              +{{ item.tags.length - 3 }} more
            </span>
          </div>
          
          <div class="flex items-center justify-between">
            <router-link 
              :to="`/portfolio/${item.id}`" 
              class="inline-flex items-center text-black hover:text-gray-700 font-medium group/link"
            >
              Learn more
              <svg class="w-4 h-4 ml-2 group-hover/link:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
            
            <time class="text-sm text-gray-400">{{ formatDate(item.created_at) }}</time>
          </div>
        </div>
      </div>
    </div>
    
    <div v-else class="text-center py-20">
      <div class="w-32 h-32 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6">
        <svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
        </svg>
      </div>
      <h3 class="text-2xl font-bold text-gray-900 mb-4">No portfolio items yet</h3>
      <p class="text-gray-500 text-lg">Projects and work samples will be showcased here soon!</p>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getPortfolio } from '../api';

const items = ref([]);

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'short'
  });
};

onMounted(async () => {
  try {
    const res = await getPortfolio();
    items.value = res.data;
  } catch (error) {
    console.error('Error fetching portfolio items:', error);
  }
});
</script>

<style scoped>
/* No purple! */
</style>
