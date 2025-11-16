import api from "./https";
import * as SecureStore from "expo-secure-store";
import { ACTIVITY } from "../utils/constants";

export const AuthAPI = {
  login: async (email, password) => {
    const { data } = await api.post("/user/data/login", {
      Email: email,
      Password: password,
    });
    console.log("TOKEN1:", data.access_token);
    console.log("TOKEN2:", data.refresh_token);

    await SecureStore.setItemAsync("accessToken", data.access_token);
    await SecureStore.setItemAsync("refreshToken", data.refresh_token);

    return data;
  },
  registration: async (email, password) => {
    const { data } = await api.post("/user/data/auth", {
      Email: email,
      Password: password,
    });

    await SecureStore.setItemAsync("accessToken", data.access_token);
    await SecureStore.setItemAsync("refreshToken", data.refresh_token);

    return data;
  },
};

export const API = {
  // Данные пользователя (лк)
  getUserData: async () => {
    const { data } = await api.get("/user/data/userdata");
    return data;
  },
  postUserData: async (config) => {
    const { data } = await api.post("/user/data/userdata", config);
    return data;
  },
  putUserData: async (config) => {
    const { data } = await api.put("/user/data/userdata", config);
    return data;
  },
};
