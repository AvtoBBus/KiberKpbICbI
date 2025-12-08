import { useFonts } from "expo-font";
import React, { useCallback } from "react";
import { Text } from "react-native";
import { FONT_MAP } from "./assets/fonts";
// import * as SplashScreen from "expo-splash-screen";
import Router from "./router";
import { NotificationProvider } from "./store";
import { DateProvider } from "./store";
// import NotificationBloc from "./components/bloc/NotificationBloc.js";
// import NotificationBloc from "./components/bloc/notificationBloc";
import NotificationBloc from "./components/bloc/NotificationBloc.js";

// SplashScreen.preventAutoHideAsync();

export default function App() {
  // const [fontsLoaded] = useFonts(FONT_MAP);

  // const onLayoutRootView = useCallback(async () => {
  //   if (fontsLoaded) {
  //     await SplashScreen.hideAsync();
  //   }
  // }, [fontsLoaded]);

  // if (!fontsLoaded) {
  //   return <Text>Загрузка, которую потом сделаем</Text>;
  // } else
  return (
    <DateProvider>
      <NotificationProvider>
        <NotificationBloc />
        <Router />
      </NotificationProvider>
    </DateProvider>
  );
}
