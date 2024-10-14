import { createRouter, createWebHistory } from "vue-router";
import HomeRoutes from "./home/routes";
import ProjectsRoutes from "./projects/routes";
import AboutRoutes from "./about/routes";
import ContactRoutes from "./contact/routes";
import ServiceRoutes from "./service/routes";
import AuthRoutes from "./authentications/routes";
import { useAuthStore } from "@/stores/auth";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      children: HomeRoutes,
    },
    {
      path: "/projects",
      component: () => import("@/views/projects/layout.vue"),
      children: ProjectsRoutes,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore();
        if (!authStore.isLoggedIn) {
          next({ path: "/auth/login" });
        } else {
          next();
        }
      },
    },
    {
      path: "/about",
      children: AboutRoutes,
    },
    {
      path: "/contact",
      children: ContactRoutes,
    },
    {
      path: "/service",
      children: ServiceRoutes,
    },
    // auth routes
    {
      path: "/auth",
      children: AuthRoutes,
      beforeEnter: (to, from, next) => {
        const authStore = useAuthStore();
        if (authStore.isLoggedIn) {
          next({ path: "/" });
        } else {
          next();
        }
      },
    },
  ],
});

export default router;
