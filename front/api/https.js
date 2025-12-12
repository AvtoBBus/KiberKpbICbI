import axios from "axios";
import * as SecureStore from "expo-secure-store";
import { router } from "../router/routerRef";

const API_URL = "http://62.84.122.18:8000/api";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 20_000,
});

api.interceptors.request.use(async (config) => {
  const token = await SecureStore.getItemAsync("accessToken");
  if (token) {
    // config.headers.Authorization = `Bearer ${token}`;
    config.headers.token = token;
  }
  return config;
});

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.config?.skipAuthRefresh) {
      return Promise.reject(error);
    }

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const refreshToken = await SecureStore.getItemAsync("refreshToken");

      if (refreshToken) {
        try {
          const { data } = await api.post(`${API_URL}/user/data/refresh`, {
            refresh_token: refreshToken,
          });

          await SecureStore.setItemAsync("accessToken", data.access_token);
          await SecureStore.setItemAsync("refreshToken", data.refresh_token);

          // originalRequest.headers.Authorization = `Bearer ${data.access_token}`;
          originalRequest.headers.token = data.access_token;

          return api(originalRequest);
        } catch (refreshError) {
          console.warn("Срок действия токена истек");
          console.warn("REFRESH ERROR:", refreshError?.response?.data);
        }
      }

      await SecureStore.deleteItemAsync("accessToken");
      await SecureStore.deleteItemAsync("refreshToken");
      if (router.isReady()) {
        router.navigate("Authorization");
      }
    }

    return Promise.reject(error);
  }
);

export default api;
