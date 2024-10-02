<template>
  <div>
    <h2 class="text-3xl hover:font-light flex justify-center">
      Projects Details
    </h2>
    <RouterLink
      to="/projects"
      class="text-sm hover:font-light flex justify-center"
    >
      Projects List
    </RouterLink>

    <div class="p-5">
      <form @submit.prevent="updateProject" class="max-w-md mx-auto">
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700"
            >Name</label
          >
          <input
            type="text"
            id="name"
            v-model="item.name"
            class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
            required
          />
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
            required
          ></textarea>
          <div class="mb-4">
            <label for="status" class="block text-sm font-medium text-gray-700"
              >Status</label
            >
            <select
              id="status"
              v-model="item.status"
              class="mt-1 block w-full p-2 border border-gray-300 rounded-md"
              required
            >
              <option value="PENDING">Pending</option>
              <option value="ACTIVE">Active</option>
              <option value="DEACTIVATED">Deactivated</option>
              <option value="COMPLETED">Completed</option>
              <option value="CANCELLED">Cancelled</option>
              <option value="REMOVED">Removed</option>
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
              required
            />
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
              required
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
const item = ref([]);

const route = useRoute();
const router = useRouter();

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

// Update project
const updateProject = async () => {
  try {
    const uid = route.params.uid;
    await axios.patch("http://localhost:8000/projects/" + uid, item.value);
    iziToast.success({
      title: "Success",
      message: "Project updated successfully",
    });
    router.push("/projects");
  } catch (error) {
    console.log(error);
  }
};
</script>
