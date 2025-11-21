import React, { useState, useCallback, useEffect } from "react";
import { useFocusEffect } from "@react-navigation/native";
import { View, StyleSheet, ScrollView, TouchableOpacity } from "react-native";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc";
import CalendarUI from "../components/ui/CalendarUI.js";
import { SafeAreaView } from "react-native-safe-area-context";
import UserImg from "../assets/img/User.js";
import StatImg from "../assets/img/Stat.js";
import HomeStatisticBloc from "../components/bloc/HomeStatisticBloc.js";
import HomeLanchBloc from "../components/bloc/HomeLanchBloc.js";
import { API } from "../api/api.js";

export default function HomeView({ navigation }) {
  const getToday = () => {
    const d = new Date();
    const day = String(d.getDate()).padStart(2, "0");
    const month = String(d.getMonth() + 1).padStart(2, "0");
    const year = d.getFullYear();
    return `${year}-${month}-${day}`;
  };

  const [userData, setUserData] = useState(null);
  const [userStat, setUserStat] = useState(null);
  const [date, setDate] = useState(getToday());

  const loadUserData = async () => {
    if (!date) return;

    try {
      console.log("Дата запроса:", date);

      const stat = await API.getDayStat(date);
      setUserStat(stat);
    } catch (err) {
      console.log("Ошибка загрузки1:", err);
    }

    try {
      const res = await API.getStatNorm();
      setUserData(res);
    } catch (err) {
      console.log("Ошибка загрузки2:", err);
    }
  };

  useEffect(() => {
    loadUserData();
  }, [date]);

  useFocusEffect(
    useCallback(() => {
      loadUserData();
    }, [date])
  );

  return (
    <View style={{ height: "100%" }}>
      <ScrollView
        contentContainerStyle={{ paddingBottom: 0 }}
        showsVerticalScrollIndicator={false}
      >
        <SafeAreaView style={mainStyle.main_bloc}>
          <View style={mainStyle.start_bloc}>
            <TouchableOpacity onPress={() => navigation.navigate("User")}>
              <UserImg width={36} height={36} />
            </TouchableOpacity>
            <TouchableOpacity onPress={() => navigation.navigate("")}>
              <StatImg width={36} height={36} />
            </TouchableOpacity>
          </View>
          <CalendarUI onSelect={(date) => setDate(date)} />
          <HomeStatisticBloc userData={userData} userStat={userStat} />
          <View style={{ marginTop: 20, gap: 10 }}>
            <HomeLanchBloc
              image={require("../assets/img/br.png")}
              title="Завтрак"
            />
            <HomeLanchBloc
              image={require("../assets/img/ln.png")}
              title="Обед"
            />
            <HomeLanchBloc
              image={require("../assets/img/dn.png")}
              title="Ужин"
            />
          </View>
        </SafeAreaView>
      </ScrollView>

      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({});
