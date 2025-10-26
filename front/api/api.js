import api from "./https";

// все запросы интуитивные, правильные уточнить у Вовы

export const AuthAPI = {
  login: async (email, password) => {
    const { data } = await apiClient.post("/auth/login", { email, password });
    await SecureStore.setItemAsync("accessToken", data.accessToken);
    await SecureStore.setItemAsync("refreshToken", data.refreshToken);
    return data;
  },
};
