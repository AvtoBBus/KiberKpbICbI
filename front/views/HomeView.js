import React from "react";
import { View, StyleSheet } from "react-native";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc";

export default function HomeView({ navigation }) {
  return (
    <View>
      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({});
