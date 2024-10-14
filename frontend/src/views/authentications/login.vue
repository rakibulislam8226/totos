<template>
  <div
    class="max-w-screen-sm mx-auto mt-10 p-6 bg-gray-100 rounded-lg shadow-lg"
  >
    <h2 class="text-2xl font-bold text-center mb-6">Login your account</h2>
    <form @submit.prevent="loginForm">
      <div class="max-w-sm mx-auto">
        <div class="mb-5">
          <label
            for="phone"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >Phone Number</label
          >
          <input
            type="tel"
            id="phone"
            v-model="login.phone"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          />
          <!-- error message -->
          <div class="text-red-500 text-sm" v-if="errors.phone">
            {{ errors.phone }}
          </div>
        </div>
        <div class="mb-5">
          <label
            for="password"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >Password</label
          >
          <input
            type="password"
            id="password"
            v-model="login.password"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          />
          <!-- error message -->
          <div class="text-red-500 text-sm" v-if="errors.password">
            {{ errors.password }}
          </div>
        </div>
        <div class="flex items-start mb-5">
          <div class="flex items-center h-5">
            <input
              id="remember"
              type="checkbox"
              value=""
              class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800"
            />
          </div>
          <label
            for="remember"
            class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
            >Remember me</label
          >
        </div>
        <button
          type="submit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import iziToast from "@/plugins/iziToast";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();

const login = ref({
  phone: "",
  password: "",
});

const errors = ref({
  phone: "",
  password: "",
});

const loginForm = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/token/",
      login.value
    );

    iziToast.success({
      message: "Login successful",
    });

    // save the token in local storage
    const { access, refresh } = response.data;
    authStore.setToken(access, refresh);

    const { data: user } = await axios.get("http://127.0.0.1:8000/auth/me", {
      headers: {
        Authorization: `Bearer ${access}`,
      },
    });

    authStore.setUser(user);

    router.go(-2);
    // clear the forms
    login.value = {
      phone: "",
      password: "",
    };
  } catch (error) {
    Object.keys(errors.value).forEach((key) => {
      if (error.response?.data[key]) {
        errors.value[key] = error.response.data[key][0];
      }
    });
    iziToast.error({
      message: "Login Failed",
    });
    login.value.password = "";
  }
};
</script>
