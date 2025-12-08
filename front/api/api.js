import api from "./https";
import * as SecureStore from "expo-secure-store";
import { ACTIVITY } from "../utils/constants";
import { summarizeDayStats } from "../utils/functions";

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

    // console.log("Запрос на сервер:", start, end);

    const { data } = await api.get("/user/statistic/statisticcpfc/fromTo", {
      params: {
        start_date: start,
        end_date: end,
      },
    });

    // console.log(45, data);

    return data[0];
  },

  // загрузка фото
  getInfoByPhoto: async (img) => {
    const formData = new FormData();

    formData.append("file", {
      uri: img,
      type: "image/jpeg",
      name: "photo.jpg",
    });

    const { data } = await api.post("/general/image", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    // console.log("фото:", data);
    return data;
  },
  // еда по прему пищи в одну дату
  getProductMeal: async (id, isoDate) => {
    const start = `${isoDate}T00:00:00`;
    const end = `${isoDate}T23:59:59`;
    const { data } = await api.get(`user/data/meal/fromTo/${id}`, {
      params: {
        start_date: start,
        end_date: end,
      },
    });

    // console.log(JSON.stringify(data));
    return data;
  },
  postProductMeal: async (config) => {
    const { data } = await api.post("/user/data/meal", config);
    return data;
  },
  deleteProductMeal: async (id, meal) => {
    const { data } = await api.delete(`user/data/meal/${meal}/${id}`);
    return data;
  },
};
