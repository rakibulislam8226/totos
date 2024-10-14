<template>
  <router-view v-if="isAuthenticated" />
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();
const isAuthenticated = ref(false);

authStore
  .checkApiAuth()
  .then((res) => {
    if (res === true) {
      isAuthenticated.value = true;
    } else {
      authStore.logout();
      router.push("/auth/login");
    }
  })
  .catch(console.error);
</script>
