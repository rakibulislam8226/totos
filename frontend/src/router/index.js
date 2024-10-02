import {createRouter, createWebHistory} from 'vue-router';
import ProjectsRoutes from './projects/routes';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/projects',
      children: ProjectsRoutes
    }
  ]
})

export default router