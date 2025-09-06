<template>
  <section class="max-w-6xl mx-auto">
    <!-- Login Form (shown when not authenticated) -->
    <div v-if="!isLoggedIn" class="max-w-md mx-auto bg-white rounded-xl shadow-sm border border-gray-200 p-8">
      <div class="text-center mb-6">
        <h2 class="text-3xl font-bold text-gray-900 mb-2">Admin Access</h2>
        <p class="text-gray-600">Please log in to access the admin console</p>
      </div>
      
      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Username</label>
          <input 
            v-model="loginForm.username" 
            type="text"
            placeholder="Enter username" 
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-black focus:border-black transition-colors" 
            required 
          />
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
          <input 
            v-model="loginForm.password" 
            type="password"
            placeholder="Enter password" 
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-black focus:border-black transition-colors" 
            required 
          />
        </div>
        
        <div v-if="loginError" class="text-red-600 text-sm">
          {{ loginError }}
        </div>
        
        <button 
          type="submit" 
          :disabled="isLoggingIn"
          class="w-full bg-black text-white py-3 px-4 rounded-lg font-medium hover:bg-gray-800 transition-colors disabled:opacity-50"
        >
          {{ isLoggingIn ? 'Logging in...' : 'Log In' }}
        </button>
      </form>
    </div>

    <!-- Admin Console (shown when authenticated) -->
    <div v-else>
      <div class="mb-8 flex justify-between items-center">
        <div>
          <h2 class="text-4xl font-bold text-gray-900 mb-2">Admin Console</h2>
          <p class="text-lg text-gray-600">Manage your blog posts and portfolio items</p>
        </div>
        <button 
          @click="handleLogout"
          class="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg font-medium hover:bg-gray-200 transition-colors"
        >
          Logout
        </button>
      </div>

      <!-- Tabs -->
      <div class="mb-8">
        <div class="border-b border-gray-200">
          <nav class="-mb-px flex space-x-8">
            <button 
              @click="activeTab = 'posts'"
              class="py-4 px-1 border-b-2 font-medium text-sm"
              :class="activeTab === 'posts' 
                ? 'border-black text-black' 
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'"
            >
              Blog Posts
            </button>
            <button 
              @click="activeTab = 'portfolio'"
              class="py-4 px-1 border-b-2 font-medium text-sm"
              :class="activeTab === 'portfolio' 
                ? 'border-black text-black' 
                : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'"
            >
              Portfolio Items
            </button>
          </nav>
        </div>
      </div>

    <!-- Blog Posts Tab -->
    <div v-if="activeTab === 'posts'" class="space-y-8">
      <!-- Add Blog Post Form -->
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-6">Add New Blog Post</h3>
        <form @submit.prevent="addBlogPost" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Title</label>
            <input 
              v-model="post.title" 
              type="text"
              placeholder="Enter blog post title" 
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
              required 
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Content</label>
            <textarea 
              v-model="post.content" 
              placeholder="Write your blog post content here..." 
              rows="8"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors resize-none" 
              required
            ></textarea>
          </div>
          
          <div class="flex items-center space-x-4">
            <label class="flex items-center">
              <input 
                v-model="post.published" 
                type="checkbox" 
                class="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
              />
              <span class="ml-2 text-sm font-medium text-gray-700">Published</span>
            </label>
          </div>
          
          <button 
            type="submit" 
            :disabled="isLoading"
            class="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ isLoading ? 'Adding...' : 'Add Blog Post' }}
          </button>
        </form>
      </div>

      <!-- Existing Blog Posts -->
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-6">Existing Blog Posts</h3>
        <div v-if="posts.length" class="space-y-4">
          <div 
            v-for="blogPost in posts" 
            :key="blogPost.id"
            class="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:border-gray-300 transition-colors"
          >
            <div class="flex-1">
              <h4 class="font-semibold text-gray-900">{{ blogPost.title }}</h4>
              <p class="text-sm text-gray-500 mt-1">{{ formatDate(blogPost.created_at) }}</p>
              <p class="text-sm text-gray-600 mt-2 line-clamp-2">
                {{ blogPost.content.substring(0, 100) }}{{ blogPost.content.length > 100 ? '...' : '' }}
              </p>
            </div>
            <div class="flex items-center space-x-2 ml-4">
              <span 
                class="px-2 py-1 text-xs font-medium rounded-full"
                :class="blogPost.published 
                  ? 'bg-green-100 text-green-800' 
                  : 'bg-gray-100 text-gray-800'"
              >
                {{ blogPost.published ? 'Published' : 'Draft' }}
              </span>
              <button 
                @click="deleteBlogPost(blogPost.id)"
                class="text-red-600 hover:text-red-700 p-2 rounded-lg hover:bg-red-50 transition-colors"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No blog posts yet
        </div>
      </div>
    </div>

    <!-- Portfolio Items Tab -->
    <div v-if="activeTab === 'portfolio'" class="space-y-8">
      <!-- Add Portfolio Item Form -->
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-6">Add New Portfolio Item</h3>
        <form @submit.prevent="addPortfolioItemHandler" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Project Name</label>
              <input 
                v-model="portfolioItem.name" 
                type="text"
                placeholder="Enter project name" 
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                required 
              />
            </div>
            
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">Live Demo URL</label>
              <input 
                v-model="portfolioItem.link" 
                type="url"
                placeholder="https://example.com" 
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
              />
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Image URL</label>
            <input 
              v-model="portfolioItem.image_url" 
              type="url"
              placeholder="https://example.com/image.jpg" 
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
            <textarea 
              v-model="portfolioItem.description" 
              placeholder="Describe your project..." 
              rows="4"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors resize-none" 
              required
            ></textarea>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Tags (comma-separated)</label>
            <input 
              v-model="tagsInput" 
              type="text"
              placeholder="React, TypeScript, Node.js" 
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
            />
          </div>
          
          <button 
            type="submit" 
            :disabled="isLoading"
            class="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-semibold hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ isLoading ? 'Adding...' : 'Add Portfolio Item' }}
          </button>
        </form>
      </div>

      <!-- Existing Portfolio Items -->
      <div class="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
        <h3 class="text-2xl font-bold text-gray-900 mb-6">Existing Portfolio Items</h3>
        <div v-if="portfolioItems.length" class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div 
            v-for="item in portfolioItems" 
            :key="item.id"
            class="border border-gray-200 rounded-lg overflow-hidden hover:border-gray-300 transition-colors"
          >
            <div class="aspect-video bg-gradient-to-br from-blue-50 to-indigo-100">
              <img 
                v-if="item.image_url" 
                :src="item.image_url" 
                :alt="item.name"
                class="w-full h-full object-cover"
              />
              <div v-else class="w-full h-full flex items-center justify-center">
                <svg class="w-12 h-12 text-blue-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                </svg>
              </div>
            </div>
            <div class="p-4">
              <div class="flex items-start justify-between mb-2">
                <h4 class="font-semibold text-gray-900">{{ item.name }}</h4>
                <button 
                  @click="deletePortfolioItem(item.id)"
                  class="text-red-600 hover:text-red-700 p-1 rounded hover:bg-red-50 transition-colors"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                  </svg>
                </button>
              </div>
              <p class="text-sm text-gray-600 line-clamp-2 mb-3">{{ item.description }}</p>
              <div v-if="item.tags && item.tags.length" class="flex flex-wrap gap-1 mb-3">
                <span 
                  v-for="tag in item.tags.slice(0, 3)" 
                  :key="tag"
                  class="px-2 py-1 bg-blue-50 text-blue-700 text-xs rounded-full"
                >
                  {{ tag }}
                </span>
              </div>
              <p class="text-xs text-gray-500">{{ formatDate(item.created_at) }}</p>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-8 text-gray-500">
          No portfolio items yet
        </div>
      </div>
    </div>
    </div> <!-- End of admin console (v-else) -->
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { 
  addPost, 
  addPortfolioItem, 
  getPosts, 
  getPortfolio, 
  deletePost, 
  deletePortfolioItem as deletePortfolioItemAPI,
  login,
  setAuthToken,
  removeAuthToken,
  isAuthenticated
} from '../api';

// Authentication state
const isLoggedIn = ref(false);
const isLoggingIn = ref(false);
const loginError = ref('');
const loginForm = ref({
  username: '',
  password: ''
});

const activeTab = ref('posts');
const isLoading = ref(false);

// Blog post form data
const post = ref({ 
  title: '', 
  content: '', 
  published: true 
});

// Portfolio item form data
const portfolioItem = ref({ 
  name: '', 
  description: '', 
  link: '', 
  image_url: '', 
  tags: []
});

const tagsInput = ref('');

// Data lists
const posts = ref([]);
const portfolioItems = ref([]);

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
};

const addBlogPost = async () => {
  if (isLoading.value) return;
  
  try {
    isLoading.value = true;
    await addPost(post.value);
    post.value = { title: '', content: '', published: true };
    await loadPosts();
    alert('Blog post added successfully!');
  } catch (error) {
    console.error('Error adding blog post:', error);
    alert('Error adding blog post. Please try again.');
  } finally {
    isLoading.value = false;
  }
};

const addPortfolioItemHandler = async () => {
  if (isLoading.value) return;
  
  try {
    isLoading.value = true;
    // Convert tags string to array
    const tags = tagsInput.value.split(',').map(tag => tag.trim()).filter(tag => tag);
    const itemData = { ...portfolioItem.value, tags };
    
    await addPortfolioItem(itemData);
    portfolioItem.value = { name: '', description: '', link: '', image_url: '', tags: [] };
    tagsInput.value = '';
    await loadPortfolioItems();
    alert('Portfolio item added successfully!');
  } catch (error) {
    console.error('Error adding portfolio item:', error);
    alert('Error adding portfolio item. Please try again.');
  } finally {
    isLoading.value = false;
  }
};

const deleteBlogPost = async (id) => {
  if (!confirm('Are you sure you want to delete this blog post?')) return;
  
  try {
    await deletePost(id);
    await loadPosts();
    alert('Blog post deleted successfully!');
  } catch (error) {
    console.error('Error deleting blog post:', error);
    alert('Error deleting blog post. Please try again.');
  }
};

const deletePortfolioItem = async (id) => {
  if (!confirm('Are you sure you want to delete this portfolio item?')) return;
  
  try {
    await deletePortfolioItemAPI(id);
    await loadPortfolioItems();
    alert('Portfolio item deleted successfully!');
  } catch (error) {
    console.error('Error deleting portfolio item:', error);
    alert('Error deleting portfolio item. Please try again.');
  }
};

const loadPosts = async () => {
  try {
    const res = await getPosts();
    posts.value = res.data;
  } catch (error) {
    console.error('Error loading posts:', error);
  }
};

const loadPortfolioItems = async () => {
  try {
    const res = await getPortfolio();
    portfolioItems.value = res.data;
  } catch (error) {
    console.error('Error loading portfolio items:', error);
  }
};

// Authentication functions
const handleLogin = async () => {
  isLoggingIn.value = true;
  loginError.value = '';
  
  try {
    const response = await login(loginForm.value);
    setAuthToken(response.data.access_token);
    isLoggedIn.value = true;
    await loadPosts();
    await loadPortfolioItems();
  } catch (error) {
    console.error('Login error:', error);
    loginError.value = error.response?.data?.detail || 'Login failed. Please try again.';
  } finally {
    isLoggingIn.value = false;
  }
};

const handleLogout = () => {
  removeAuthToken();
  isLoggedIn.value = false;
  loginForm.value = { username: '', password: '' };
};

onMounted(async () => {
  // Check if user is already authenticated
  isLoggedIn.value = isAuthenticated();
  
  if (isLoggedIn.value) {
    await loadPosts();
    await loadPortfolioItems();
  }
});
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
