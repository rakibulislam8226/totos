<template>
  <div>
    <h2 class="text-3xl hover:font-light flex justify-center">
      Projects Details
    </h2>

    <div class="p-5 flex justify-center">
      <form
        @submit.prevent="updateProject"
        class="w-[600px] shadow-md p-5 hover:shadow-lg bg-gray-50 rounded-lg"
      >
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700"
            >Name</label
          >
          <input
            type="text"
            id="name"
            v-model="item.name"
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
          />
          <!-- error message -->
          <div class="text-red-500 text-sm" v-if="errors.name">
            {{ errors.name }}
          </div>
        </div>
        <div class="mb-4">
          <label
            for="description"
            class="block text-sm font-medium text-gray-700"
            >Descriptions</label
          >
          <textarea
            type="text"
            id="description"
            v-model="item.description"
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
            rows="5"
          ></textarea>
          <div class="mb-4">
            <label for="status" class="block text-sm font-medium text-gray-700"
              >Status</label
            >
            <select
              id="status"
              v-model="item.status"
              class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
            >
              <option
                v-for="{ value, label } in projectStatus"
                :disabled="value === item.status"
                :value="value"
              >
                {{ label }}
              </option>
            </select>
          </div>
          <div class="mb-4">
            <label
              for="start_date"
              class="block text-sm font-medium text-gray-700"
              >Start Date</label
            >
            <input
              type="date"
              id="start_date"
              v-model="item.start_date"
              class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
            />
            <!-- error message -->
            <div class="text-red-500 text-sm" v-if="errors.start_date">
              {{ errors.start_date }}
            </div>
          </div>

          <div class="mb-4">
            <label
              for="end_date"
              class="block text-sm font-medium text-gray-700"
              >End Date</label
            >
            <input
              type="date"
              id="end_date"
              v-model="item.end_date"
              class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
            />
          </div>
        </div>
        <div class="flex justify-center">
          <button
            type="submit"
            class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
          >
            Update Project
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import iziToast from "@/plugins/iziToast";

import projectStatus from "@/constants/projectStatus";

const route = useRoute();
const router = useRouter();

const item = ref([]);

const errors = ref({
  name: "",
  start_date: "",
});

// Update project
const updateProject = async () => {
  // error handling
  errors.value = {};
  if (item.value.name.length < 3) {
    errors.value.name = "Name must be at least 3 characters.";
    return;
  } else if (!item.value.start_date) {
    errors.value.start_date = "Start date is required.";
    return;
  }

  // update project
  try {
    const uid = route.params.uid;
    await axios.patch("http://localhost:8000/projects/" + uid, item.value);
    iziToast.success({
      message: "Project updated successfully",
    });
    router.push("/projects");
  } catch (error) {
    console.log(error);
  }
};

// Get project details
const fetchItems = async () => {
  try {
    const uid = route.params.uid;
    const response = await axios.get("http://localhost:8000/projects/" + uid);
    item.value = response.data;
  } catch (error) {
    console.log(error);
  }
};
fetchItems();
</script>
