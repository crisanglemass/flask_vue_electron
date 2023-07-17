import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import ElementPlus from 'element-plus';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'element-plus/theme-chalk/index.css';
import '@element-plus/icons-vue';

import i18next from 'i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import en from '@/assets/locales/en.json';
import zh from '@/assets/locales/zh.json';

//i18n international translation
i18next.use(LanguageDetector).init({
  lng: 'en',
  resources: {
    en: { translation: en },
    zh: { translation: zh },
  },
});

const app = createApp(App);
app.use(ElementPlus);
app.config.globalProperties.$axios = axios;
app.config.globalProperties.$i18n = i18next;

app.use(router);

app.mount('#app');
