import axios from "axios";
import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => {
    return {
      accessToken: localStorage.getItem("access_token"),
      refreshToken: localStorage.getItem("refresh_token"),
      user: JSON.parse(localStorage.getItem("user")),
    };
  },
  getters: {
    isLoggedIn: (state) => state.accessToken !== null,
  },
  actions: {
    setToken(accessToken, refreshToken) {
      this.accessToken = accessToken;
      this.refreshToken = refreshToken;
      localStorage.setItem("access_token", accessToken);
      localStorage.setItem("refresh_token", refreshToken);
    },
    setUser(user) {
      this.user = JSON.stringify(user);
      localStorage.setItem("user", this.user);
    },
    logout() {
      this.accessToken = null;
      this.refreshToken = null;
      this.user = null;
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("user");
    },
    async checkApiAuth() {
      try {
        const { data } = await axios.get("http://127.0.0.1:8000/auth/me", {
          headers: {
            Authorization: `Bearer ${this.accessToken}`,
          },
        });
        return data.phone !== "";
      } catch (error) {
        return false;
      }
    },
  },
});
