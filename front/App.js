import { useFonts } from "expo-font";
import React, { useCallback } from "react";
import { StyleSheet, Text, SafeAreaView } from "react-native";
import { mainStyle } from "./style";
import { FONT_MAP } from "./assets/fonts";
import * as SplashScreen from "expo-splash-screen";

SplashScreen.preventAutoHideAsync();

export default function App() {
  const [fontsLoaded] = useFonts(FONT_MAP);

  const onLayoutRootView = useCallback(async () => {
    if (fontsLoaded) {
      await SplashScreen.hideAsync();
    }
  }, [fontsLoaded]);

  if (!fontsLoaded) {
    return (
      <SafeAreaView>
        <Text>Загрузка</Text>
      </SafeAreaView>
    );
  } else
    return (
      <SafeAreaView onLayout={onLayoutRootView}>
        <Text style={mainStyle.title}>Приложение</Text>
      </SafeAreaView>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
});
