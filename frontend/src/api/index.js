import axios from 'axios';

const API_BASE = 'http://localhost:8000'; // Adjust if backend runs elsewhere

// Create axios instance with interceptor for auth
const api = axios.create({
  baseURL: API_BASE
});

// Add auth token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Public endpoints
export const getPosts = () => api.get('/posts');
export const getPost = (id) => api.get(`/posts/${id}`);
export const getPortfolio = () => api.get('/portfolio');
export const getPortfolioItem = (id) => api.get(`/portfolio/${id}`);

// Auth endpoints
export const login = (credentials) => api.post('/admin/login', credentials);

// Admin endpoints (require authentication)
export const addPost = (data) => api.post('/admin/posts', data);
export const updatePost = (id, data) => api.patch(`/admin/posts/${id}`, data);
export const deletePost = (id) => api.delete(`/admin/posts/${id}`);

export const addPortfolioItem = (data) => api.post('/admin/portfolio', data);
export const updatePortfolioItem = (id, data) => api.patch(`/admin/portfolio/${id}`, data);
export const deletePortfolioItem = (id) => api.delete(`/admin/portfolio/${id}`);

export const uploadImage = (formData) => api.post('/admin/upload-image/', formData);

// Auth utilities
export const setAuthToken = (token) => {
  localStorage.setItem('authToken', token);
};

export const removeAuthToken = () => {
  localStorage.removeItem('authToken');
};

export const getAuthToken = () => {
  return localStorage.getItem('authToken');
};

export const isAuthenticated = () => {
  return !!getAuthToken();
};
