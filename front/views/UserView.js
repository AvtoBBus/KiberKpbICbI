import React from "react";
import { View, StyleSheet, Text } from "react-native";
import { mainStyle } from "../style";
import SettingImg from "../assets/img/setting.svg";
import FooterBloc from "../components/bloc/FooterBloc";
import { SafeAreaView } from "react-native-safe-area-context";

export default function UserView({ navigation }) {
  return (
    <View style={{ height: "100%" }}>
      <SafeAreaView style={styles.main_bloc}>
        <View style={styles.start_bloc}>
          <Text style={mainStyle.h1}>Профиль</Text>
          <SettingImg width={37} height={37} />
        </View>
        <View style={styles.senter_bloc}></View>
      </SafeAreaView>
      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({
  main_bloc: {
    flex: 1,
    flexDirection: "column",
    justifyContent: "start",
    alignItems: "center",
  },
  start_bloc: {
    width: 334,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 20,
    marginTop: 20,
  },
  senter_bloc: {
    backgroundColor: "white",
    width: 334,
    height: 263,
    paddingTop: 20,
    paddingBottom: 20,
    paddingRight: 20,
    paddingRight: 20,
    flexDirection: "column",
    justifyContent: "start",
    alignItems: "center",
    borderRadius: 10,
  },
});
