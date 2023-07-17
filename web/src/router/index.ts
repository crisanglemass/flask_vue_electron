import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
    {path: '/', redirect: '/index'},
    {
        path: '/index',
        name: 'index',
        component: () => import('@/views/index.vue'),
        meta: {
            title: 'index',
        },
    },];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;