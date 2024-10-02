<template>
  <div>
    <h2 class="text-3xl hover:font-light flex justify-center">Projects list</h2>
    <div class="p-5">
      <div class="flex flex-wrap justify-center gap-5">
        <div
          v-for="item in items"
          class="max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-700 dark:border-gray-700"
        >
          <div class="flex justify-between">
            <h5
              class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
            >
              {{ item.name }}
            </h5>
            <font-awesome-icon class="text-2xl" :icon="faTrash" />
          </div>
          <p class="mb-3 text-sm text-gray-700 dark:text-gray-400">
            {{ item.status }}
          </p>
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            {{ item.description }}
          </p>
          <div class="flex justify-between">
            <p class="mb-3 text-sm text-gray-700 dark:text-gray-400">
              Start: {{ item.start_date }}
            </p>
            <p class="mb-3 text-sm text-gray-700 dark:text-gray-400">
              End: {{ item.end_date }}
            </p>
          </div>
          <RouterLink
            :to="`/projects/${item.uid}`"
            class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Read more
            <svg
              class="rtl:rotate-180 w-3.5 h-3.5 ms-2"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M1 5h12m0 0L9 1m4 4L9 9"
              />
            </svg>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

const items = ref([]);

const fetchItems = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/projects");
    items.value = response.data;
  } catch (error) {
    console.log(error);
  }
};
fetchItems();
</script>
