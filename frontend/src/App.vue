<script setup>
import { ref } from 'vue';

const isMobileMenuOpen = ref(false);

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};
</script>

<template>
  <div id="app" class="min-h-screen bg-white">
    <!-- Navigation -->
    <header class="bg-white shadow-sm border-b border-gray-200 sticky top-0 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <!-- Logo -->
          <router-link to="/" class="flex items-center space-x-2">
            <div class="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
              </svg>
            </div>
            <span class="text-xl font-bold text-black">Jaswant Kondur</span>
          </router-link>
          
          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-8">
            <router-link 
              to="/" 
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path === '/' }"
            >
              Home
            </router-link>
            <router-link 
              to="/blog" 
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path.startsWith('/blog') }"
            >
              Blog
            </router-link>
            <router-link 
              to="/portfolio" 
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path.startsWith('/portfolio') }"
            >
              Portfolio
            </router-link>
            <router-link 
              to="/admin" 
              class="bg-black text-white px-4 py-2 rounded-lg font-medium hover:bg-gray-800 transition-all duration-200 shadow-lg hover:shadow-xl"
            >
              Admin
            </router-link>
          </div>
          
          <!-- Mobile menu button -->
          <button 
            @click="toggleMobileMenu"
            class="md:hidden inline-flex items-center justify-center p-2 rounded-lg text-gray-700 hover:text-black hover:bg-gray-100 transition-colors duration-200"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path v-if="!isMobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        
        <!-- Mobile Navigation -->
        <div v-if="isMobileMenuOpen" class="md:hidden border-t border-gray-200 py-4">
          <div class="flex flex-col space-y-2">
            <router-link 
              to="/" 
              @click="isMobileMenuOpen = false"
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path === '/' }"
            >
              Home
            </router-link>
            <router-link 
              to="/blog" 
              @click="isMobileMenuOpen = false"
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path.startsWith('/blog') }"
            >
              Blog
            </router-link>
            <router-link 
              to="/portfolio" 
              @click="isMobileMenuOpen = false"
              class="text-gray-700 hover:text-black px-3 py-2 rounded-lg font-medium transition-colors duration-200"
              :class="{ 'text-black bg-gray-100': $route.path.startsWith('/portfolio') }"
            >
              Portfolio
            </router-link>
            <router-link 
              to="/admin" 
              @click="isMobileMenuOpen = false"
              class="bg-black text-white px-4 py-2 rounded-lg font-medium hover:bg-gray-800 transition-all duration-200 shadow-lg hover:shadow-xl text-center"
            >
              Admin
            </router-link>
          </div>
        </div>
      </nav>
    </header>
    
    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <router-view />
    </main>
    
    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div class="text-center">
          <p class="text-gray-600">
            © {{ new Date().getFullYear() }} Jaswant Kondur. Built with Vue.js and FastAPI.
          </p>
        </div>
      </div>
    </footer>
  </div>
</template>

<style>
/* Global styles */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
}

/* Remove any purple/blue colors and use black/white/gray aesthetic */
.router-link-active {
  color: #000 !important;
}

/* Ensure consistent black and white design */
a:not(.bg-black):not(.text-white) {
  color: #000;
  text-decoration: none;
}

a:not(.bg-black):not(.text-white):hover {
  color: #374151;
}

/* Preserve white text on black backgrounds */
.bg-black,
.bg-black a,
.bg-black *,
a.bg-black,
button.bg-black {
  color: #fff !important;
}

.bg-black:hover,
.bg-black a:hover,
a.bg-black:hover,
button.bg-black:hover {
  color: #fff !important;
}

/* Override any remaining color classes */
.text-blue-600,
.text-blue-700,
.text-indigo-600 {
  color: #000 !important;
}

.bg-blue-600,
.bg-blue-700,
.bg-indigo-600 {
  background-color: #000 !important;
}

.bg-blue-50,
.bg-indigo-100 {
  background-color: #f9fafb !important;
}

.border-blue-600,
.border-blue-700,
.border-indigo-600 {
  border-color: #000 !important;
}

.hover\:bg-blue-700:hover,
.hover\:bg-indigo-700:hover {
  background-color: #374151 !important;
}

.hover\:text-blue-600:hover,
.hover\:text-blue-700:hover {
  color: #000 !important;
}
</style>
