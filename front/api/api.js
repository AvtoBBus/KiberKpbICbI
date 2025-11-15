import api from "./https";
import * as SecureStore from "expo-secure-store";

// все запросы интуитивные, правильные уточнить у Вовы

export const AuthAPI = {
  login: async (email, password) => {
    const { data } = await api.post("/user/data/login", {
      Email: email,
      Password: password,
    });
    // console.log("LOGIN RESPONSE:", data);

    await SecureStore.setItemAsync("accessToken", data.access_token);
    await SecureStore.setItemAsync("refreshToken", data.refresh_token);

    return data;
  },
  registration: async (email, password) => {
    const { data } = await api.post("/user/data/auth", {
      Email: email,
      Password: password,
    });
    // console.log("LOGIN RESPONSE:", data);

    await SecureStore.setItemAsync("accessToken", data.access_token);
    await SecureStore.setItemAsync("refreshToken", data.refresh_token);

    return data;
  },
};
