import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import axios from 'axios'

axios.defaults.baseURL = import.meta.env.VITE_BACKEND_HOST

createApp(App).mount('#app')
