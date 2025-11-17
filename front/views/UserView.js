import React, { useState, useCallback } from "react";
import { View, StyleSheet, Text } from "react-native";
import { mainStyle } from "../style";
import SettingImg from "../assets/img/setting.svg";
import FooterBloc from "../components/bloc/FooterBloc";
import { SafeAreaView } from "react-native-safe-area-context";
import { API } from "../api/api.js";
import { useFocusEffect } from "@react-navigation/native";
import { ACTIVITY } from "../utils/constants";

export default function UserView({ navigation }) {
  const [userData, setUserData] = useState(null);
  const loadUserData = async () => {
    try {
      const res = await API.getUserData();

      // console.log("ghgh:", res);
      setUserData(res[0]);
    } catch (err) {
      console.log("Ошибка загрузки:", err);
    }
  };

  useFocusEffect(
    useCallback(() => {
      loadUserData();
    }, [])
  );

  return (
    <View style={{ height: "100%" }}>
      <SafeAreaView style={mainStyle.main_bloc}>
        <View style={mainStyle.start_bloc}>
          <Text style={mainStyle.h1}>Профиль</Text>
          <SettingImg
            width={37}
            height={37}
            onPress={() =>
              navigation.navigate("EditUser", { Userdata: userData })
            }
          />
        </View>
        <View style={mainStyle.white_bloc}>
          <View style={styles.userHeader}>
            <View style={styles.p_table}>
              <View style={styles.avatar} />
            </View>
            <View style={[styles.userName, styles.p_table]}>
              {/* <Text style={mainStyle.p}>Иван</Text>
              <Text style={mainStyle.p}>Иванович</Text> */}
              <Text style={[mainStyle.p]}>{userData?.UserName ?? "-"}</Text>
            </View>
          </View>

          <View style={styles.infoBlock}>
            <View style={styles.infoRow}>
              <Text style={[mainStyle.p, styles.p_table]}>Возраст:</Text>
              <Text style={[mainStyle.p, styles.p_table]}>
                {userData?.Age ?? "-"}
              </Text>
            </View>
            <View style={styles.infoRow}>
              <Text style={[mainStyle.p, styles.p_table]}>Рост:</Text>
              <Text style={[mainStyle.p, styles.p_table]}>
                {userData?.Height ?? "-"}
              </Text>
            </View>
            <View style={styles.infoRow}>
              <Text style={[mainStyle.p, styles.p_table]}>Текущий вес:</Text>
              <Text style={[mainStyle.p, styles.p_table]}>
                {userData?.Weight ?? "-"}
              </Text>
            </View>
            <View style={styles.infoRow}>
              <Text style={[mainStyle.p, styles.p_table]}>Желаемый вес:</Text>
              <Text style={[mainStyle.p, styles.p_table]}>
                {userData?.DesiredWeight ?? "-"}
              </Text>
            </View>
            <View style={styles.infoRow}>
              <Text style={[mainStyle.p, styles.p_table]}>Активность:</Text>
              <Text style={[mainStyle.p, styles.p_table]}>
                {ACTIVITY[userData?.Activity] ?? "-"}
              </Text>
            </View>
          </View>
        </View>
      </SafeAreaView>
      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({
  // main_bloc: {
  //   flex: 1,
  //   flexDirection: "column",
  //   justifyContent: "start",
  //   alignItems: "center",
  // },
  // start_bloc: {
  //   width: 334,
  //   flexDirection: "row",
  //   justifyContent: "space-between",
  //   alignItems: "center",
  //   marginBottom: 20,
  //   marginTop: 20,
  // },
  // senter_bloc: {
  //   backgroundColor: "white",
  //   width: 334,
  //   // height: 263,
  //   paddingTop: 20,
  //   paddingBottom: 20,
  //   paddingRight: 20,
  //   paddingRight: 20,
  //   flexDirection: "column",
  //   justifyContent: "start",
  //   alignItems: "center",
  //   borderRadius: 10,
  // },
  infoRow: {
    flexDirection: "row",
    // justifyContent: "space-between",
    marginBottom: 12,
    width: 270,
  },
  p_table: {
    flex: 1,
  },
  userName: {
    gap: 10,
    height: 64,
    justifyContent: "center",
  },
  userHeader: {
    height: 64,
    width: 264,
    marginBottom: 32,
    flexDirection: "row",
  },
  avatar: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: "black",
  },
});
