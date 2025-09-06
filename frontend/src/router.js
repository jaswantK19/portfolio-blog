import { createRouter, createWebHistory } from 'vue-router';

import Home from './views/Home.vue';
import Blog from './views/Blog.vue';
import Portfolio from './views/Portfolio.vue';
import Admin from './views/Admin.vue';
import Post from './views/Post.vue';
import PortfolioItem from './views/PortfolioItem.vue';


const routes = [
  { path: '/', component: Home },
  { path: '/blog', component: Blog },
  { path: '/blog/:id', component: Post },
  { path: '/portfolio', component: Portfolio },
  { path: '/portfolio/:id', component: PortfolioItem },
  { path: '/admin', component: Admin },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
