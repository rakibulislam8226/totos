<template>
  <div>
    <p class="text-3xl mt-2 flex justify-center">Projects create</p>
    <div class="p-5">
      <form @submit.prevent="createProject" class="max-w-md mx-auto">
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
            Create Project
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import iziToast from "@/plugins/iziToast";

const router = useRouter();

const item = ref({
  name: "",
  description: "",
  status: "PENDING",
  start_date: "",
  end_date: null,
});

const errors = ref({
  name: "",
  start_date: "",
});

const createProject = async () => {
  // error handling
  errors.value = {};
  if (item.value.name.length < 3) {
    errors.value.name = "Name must be at least 3 characters.";
    return;
  } else if (!item.value.start_date) {
    errors.value.start_date = "Start date is required.";
    return;
  }

  // create project
  try {
    await axios.post("http://localhost:8000/projects", item.value);
    iziToast.success({
      message: "Project created successfully",
    });
    router.push("/projects");
  } catch (error) {
    console.log(error);
  }
};
</script>
