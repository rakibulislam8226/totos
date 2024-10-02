<template>
  <Teleport to="body">
    <!-- Main modal -->
    <div
      ref="modal"
      tabindex="-1"
      aria-hidden="true"
      class="hidden overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
    >
      <div :class="`max-w-${size}`" class="relative p-4 w-full max-h-full">
        <!-- Modal content -->
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <!-- Modal header -->
          <div
            v-if="showHeader"
            class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600"
          >
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
              {{ title }}
            </h3>
            <button
              type="button"
              @click="() => modal.hide()"
              class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            >
              <i class="fa fa-times text-xl" aria-hidden="true"></i>
              <span class="sr-only">Close Modal</span>
            </button>
          </div>
          <!-- Modal body -->
          <form class="p-4 md:p-5">
            <slot :modal="modal"></slot>
          </form>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script>
import { Modal } from "flowbite";

export default {
  props: {
    modelValue: undefined,
    options: { type: Object, default: {} },
    title: { type: String, default: "Add New" },
    size: { type: String, default: "md" },
    showHeader: { type: Boolean, default: true },
  },

  emits: ["update:modelValue", "hide"],

  data() {
    return {
      modal: null,
    };
  },

  mounted() {
    if (this.$refs.modal instanceof HTMLElement) {
      this.modal = new Modal(this.$refs.modal, {
        onHide: () => {
          this.$emit("update:modelValue", false);
          this.$emit("hide", this.modal);
        },
        ...this.options,
      });
    }
  },

  watch: {
    modelValue: function (newVal) {
      if (newVal === true) {
        this.modal.show();
      } else if (newVal === false) {
        this.modal.hide();
      }
    },
  },
};
</script>
