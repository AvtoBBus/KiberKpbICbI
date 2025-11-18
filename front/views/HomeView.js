import React from "react";
import { View, StyleSheet } from "react-native";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc";
import CalendarUI from "../components/ui/CalendarUI.js";
import { SafeAreaView } from "react-native-safe-area-context";
import UserImg from "../assets/img/User.js";
import StatImg from "../assets/img/Stat.js";
import HomeStatisticBloc from "../components/bloc/HomeStatisticBloc.js";

export default function HomeView({ navigation }) {
  return (
    <View style={{ height: "100%" }}>
      <SafeAreaView style={mainStyle.main_bloc}>
        <View style={mainStyle.start_bloc}>
          <UserImg
            width={36}
            height={36}
            onPress={() => navigation.navigate("User")}
          />
          <StatImg
            width={36}
            height={36}
            onPress={() => navigation.navigate("")}
          />
        </View>
        <CalendarUI onSelect={(date) => console.log("Выбрали:", date)} />
        <HomeStatisticBloc />
      </SafeAreaView>

      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({});
