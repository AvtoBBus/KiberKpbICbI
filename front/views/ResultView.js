import React from "react";
import {
  View,
  StyleSheet,
  Text,
  TouchableWithoutFeedback,
  Keyboard,
  ImageBackground,
} from "react-native";
import { mainStyle } from "../style";
import SettingImg from "../assets/img/SettingGreen.js";
import { stylesAuth } from "../style/auto.js";
import ButtonUI from "../components/ui/ButtonUI.js";
import BackImg from "../assets/img/Back.js";
import MultiDonutChartUI from "../components/ui/MultiDonutChartUI.js";

// import DonutChartUI from "../components/ui/DonutChartUI";

export default function ResultView({ navigation }) {
  const handleLogin = () => {
    console.log(678);
  };
  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <ImageBackground
        style={styles.container}
        source={require("../assets/img/br.png")} // твоя картинка
        // style={styles.container}
        resizeMode="cover" // или "stretch"
      >
        <View style={[mainStyle.whiteCard, styles.res_card]}>
          <BackImg style={styles.back} onPress={() => navigation.goBack()} />
          <View style={styles.circle}>
            <MultiDonutChartUI protein={30} fats={0} carbs={30} />
          </View>

          <View style={[styles.res_w]}>
            <Text style={[mainStyle.h1, styles.label]}>Название блюда</Text>
            <SettingImg />
          </View>
          <View style={[styles.res_w, styles.res_p]}>
            <View style={[styles.res_kbjy]}>
              <Text style={[mainStyle.h1, styles.label]}>Белок</Text>
              <Text style={[mainStyle.h2, styles.text_m]}>9999</Text>
              <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                грамм
              </Text>
            </View>
            <View style={[styles.res_kbjy, { borderColor: "#F9E5B8" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Жиры</Text>
              <Text style={[mainStyle.h2, styles.text_m]}>9999</Text>
              <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                грамм
              </Text>
            </View>
            <View style={[styles.res_kbjy, { borderColor: "#B6E8FF" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Углеводы</Text>
              <Text style={[mainStyle.h2, styles.text_m]}>9999</Text>
              <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                грамм
              </Text>
            </View>
          </View>
          <View style={[mainStyle.start_bloc, styles.res_f]}>
            <View style={styles.res_w2}>
              <Text style={[mainStyle.h2]}>9999</Text>
              <Text
                style={[
                  mainStyle.p_light,
                  { textAlign: "center", marginTop: 12 },
                ]}
              >
                грамм
              </Text>
            </View>
            <View style={styles.res_w2}>
              <Text style={[mainStyle.h2]}>999</Text>
              <Text
                style={[
                  mainStyle.p_light,
                  { textAlign: "center", marginTop: 12 },
                ]}
              >
                кДж
              </Text>
            </View>
          </View>
          <ButtonUI title={"Добавить"} green={true} onPress={handleLogin} />
        </View>
      </ImageBackground>
    </TouchableWithoutFeedback>
  );
}

const styles = StyleSheet.create({
  circle: {
    // flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  container: {
    flex: 1,
    // backgroundColor: "#D6F3A1",
    paddingTop: 300,
  },
  back: {
    position: "absolute",
    top: 20,
    left: 20,
  },
  res_card: {
    backgroundColor: "#F6F6F6",
    gap: 10,
    position: "relative",
  },
  label: {
    fontSize: 15,
    maxWidth: 300,
  },
  res_w: {
    // flex: 1,
    // width:
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderRadius: 10,
    paddingTop: 6,
    paddingBottom: 6,
    paddingLeft: 9,
    paddingRight: 9,
    // maxWidth: 316,
  },
  res_w2: {
    width: 154,
    height: 66,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderRadius: 10,
    gap: 4,
  },
  res_p: {
    paddingTop: 9,
    paddingBottom: 9,
    gap: 10,
  },
  res_kbjy: {
    height: 110,
    // width: 97,
    flex: 1,
    flexDirection: "column",
    justifyContent: "center",
    alignContent: "space-between",
    padding: 10,
    borderWidth: 1,
    borderColor: "#A5D66D",
    borderRadius: 10,
  },
  res_f: {
    marginBottom: 10,
    marginTop: 0,
    width: "100%",
  },
  text_m: {
    marginTop: 10,
    // marginEnd: 3,
  },
});
