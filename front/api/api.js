import api from "./https";
import * as SecureStore from "expo-secure-store";
import { ACTIVITY } from "../utils/constants";

export const AuthAPI = {
  login: async (email, password) => {
    const { data } = await api.post("/user/data/login", {
      Email: email,
      Password: password,
    });

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

  // норма кбжу
  putStatNorm: async (config) => {
    const { data } = await api.put("/user/data/normcpfc", config);
    return data;
  },
  postStatNorm: async (config) => {
    const { data } = await api.post("/user/data/normcpfc", config);
    return data;
  },
  getStatNorm: async () => {
    const { data } = await api.get("/user/data/normcpfc");
    return data;
  },

  // запрос на день
  getDayStat: async (isoDate) => {
    const start = `${isoDate}T00:00:00`;
    const end = `${isoDate}T23:59:59`;

    console.log("Запрос на сервер:", start, end);

    const { data } = await api.get("/user/statistic/userstatistic/fromTo", {
      params: {
        start_date: start,
        end_date: end,
      },
    });

    return data;
  },
};
