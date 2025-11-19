import React from "react";
import { View, StyleSheet, ScrollView } from "react-native";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc";
import CalendarUI from "../components/ui/CalendarUI.js";
import { SafeAreaView } from "react-native-safe-area-context";
import UserImg from "../assets/img/User.js";
import StatImg from "../assets/img/Stat.js";
import HomeStatisticBloc from "../components/bloc/HomeStatisticBloc.js";
import HomeLanchBloc from "../components/bloc/HomeLanchBloc.js";

export default function HomeView({ navigation }) {
  return (
    <View style={{ height: "100%" }}>
      <ScrollView
        contentContainerStyle={{ paddingBottom: 0 }}
        showsVerticalScrollIndicator={false}
      >
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
