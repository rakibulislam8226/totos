<template>
  <div>
    <h2 class="text-3xl mt-2 flex justify-center">Projects list</h2>
    <div class="p-5">
      <div class="flex flex-wrap justify-center gap-5">
        <div
          v-for="item in items"
          class="max-w-sm p-6 mt-2 w-[400px] bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-700 dark:border-gray-700"
        >
          <div class="flex justify-between">
            <h5
              class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
            >
              {{ item.name }}
            </h5>
            <font-awesome-icon
              class="text-2xl hover:text-red-600"
              role="button"
              @click="deleteProject(item.uid)"
              :icon="faTrash"
            />
          </div>
          <p
            :class="getStatusColor(item.status)"
            class="mb-3 text-sm text-gray-700 dark:text-gray-400"
          >
            {{ item.status }}
          </p>
          <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
            {{ textLimit(item.description, 80) }}
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
            class="inline-flex items-center px-3 py-2 mb-1 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
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

    <Modal
      v-model="isShowDeleteModal"
      @hide="clearDeleteModal"
      :show-header="false"
    >
      <svg
        class="mx-auto mb-4 text-gray-400 w-12 h-12 dark:text-gray-200"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 20 20"
      >
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M10 11V6m0 8h.01M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
        />
      </svg>
      <h3 class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400">
        Are you sure you want to delete this project?
      </h3>
      <div class="flex justify-center">
        <button
          type="button"
          @click="deleteItem"
          class="text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 font-medium rounded-lg text-sm inline-flex items-center px-5 py-2.5 text-center"
        >
          Yes, I'm sure
        </button>
        <button
          type="button"
          @click="isShowDeleteModal = false"
          class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
        >
          No, cancel
        </button>
      </div>
    </Modal>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";

import iziToast from "@/plugins/iziToast";
import Modal from "@/components/Modal.vue";
import projectStatus from "@/constants/projectStatus";

const items = ref([]);

// getting project list
const fetchItems = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/projects");
    items.value = response.data;
  } catch (error) {
    console.log(error);
  }
};
fetchItems();

// Descriptions text limit
const textLimit = (text, limit = 50) => {
  return text.length > limit ? text.substring(0, limit) + "..." : text;
};

// Delete project
const isShowDeleteModal = ref(false);
const selectedItemId = ref(null);

const deleteProject = (uid) => {
  selectedItemId.value = uid;
  isShowDeleteModal.value = true;
};

const deleteItem = async () => {
  try {
    const response = await axios.delete(
      "http://127.0.0.1:8000/projects/" + selectedItemId.value
    );
    isShowDeleteModal.value = false;
    fetchItems();
    iziToast.success({
      message: "Project deleted successfully",
    });
  } catch (error) {
    console.log(error);
  }
};

const clearDeleteModal = () => {
  selectedItemId.value = null;
  isShowDeleteModal.value = false;
};

const getStatusColor = (status) => {
  const found = projectStatus.find((item) => item.value === status);
  return found ? found.color : "";
};
</script>
