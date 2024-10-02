import {createRouter, createWebHistory} from 'vue-router';
import HomeRoutes from './home/routes';
import ProjectsRoutes from './projects/routes';
import AboutRoutes from './about/routes';
import ContactRoutes from './contact/routes';
import ServiceRoutes from './service/routes';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      children: HomeRoutes
    },
    {
      path: '/projects',
      children: ProjectsRoutes
    },
    {
      path: '/about',
      children: AboutRoutes
    },
    {
      path: '/contact',
      children: ContactRoutes
    },
    {
      path: '/service',
      children: ServiceRoutes
    },
  ]
})

export default router