<template>
  <div class="max-w-md mx-auto mt-10 p-6 bg-white rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-center mb-4">Get in Touch</h2>
    <p class="text-gray-600 text-center mb-6">
      We would love to hear from you! Please fill out the form below.
    </p>
    <form @submit.prevent="createContact">
      <div class="relative z-0 w-full mb-5 group">
        <input
          type="text"
          id="subject"
          v-model="contact.subject"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="subject"
          class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Subject</label
        >
        <!-- letter counter -->
        <div class="text-right text-xs text-gray-500 dark:text-gray-400">
          {{ contact.subject.length }} / 100
        </div>
        <!-- error message -->
        <div class="text-red-500 text-sm" v-if="errors.subject">
          {{ errors.subject }}
        </div>
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <input
          type="email"
          id="email"
          v-model="contact.email"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        />
        <label
          for="email"
          class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Email address</label
        >
        <!-- error message -->
        <div class="text-red-500 text-sm" v-if="errors.email">
          {{ errors.email }}
        </div>
      </div>

      <div class="relative z-0 w-full mb-5 group">
        <textarea
          id="message"
          v-model="contact.message"
          rows="4"
          class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
          placeholder=" "
        ></textarea>
        <label
          for="message"
          class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
          >Message</label
        >
        <!-- error message -->
        <div class="text-red-500 text-sm" v-if="errors.message">
          {{ errors.message }}
        </div>
      </div>

      <button
        type="submit"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

import iziToast from "@/plugins/iziToast";

const router = useRouter();

const contact = ref({
  subject: "",
  email: "",
  message: "",
});

const errors = ref({
  subject: "",
  email: "",
  message: "",
});

const createContact = async () => {
  try {
    // initialize errors to empty
    errors.value = {
      subject: "",
      email: "",
      message: "",
    };

    await axios.post("http://localhost:8000/contact", contact.value);
    iziToast.success({
      message: "Form submitted successfully",
    });

    // clear form fields
    contact.value = {
      subject: "",
      email: "",
      message: "",
    };

    // set errors if any
  } catch (error) {
    Object.keys(errors.value).forEach((key) => {
      if (error.response.data[key]) {
        errors.value[key] = error.response.data[key][0];
      }
    });
  }

  // alternatively, following code can be used to set errors
  // } catch (error) {
  //   errors.value = {
  //     subject: error.response.data?.subject?.at(0),
  //     email: error.response.data?.email?.at(0),
  //     message: error.response.data?.message?.at(0),
  //   };
  // }
};

// disbale subject input if it has more than 100 characters
watchEffect(() => {
  if (contact.value.subject.length > 100) {
    contact.value.subject = contact.value.subject.slice(0, 100);
  }
});
</script>
