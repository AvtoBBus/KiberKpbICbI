import React, { useState, useContext } from "react";
import { NotificationContext } from "../store";
import {
  View,
  StyleSheet,
  Text,
  TouchableWithoutFeedback,
  Keyboard,
  ImageBackground,
  ScrollView,
  ActivityIndicator,
} from "react-native";
import { mainStyle } from "../style";
import SettingImg from "../assets/img/SettingGreen.js";
import { stylesAuth } from "../style/auto.js";
import ButtonUI from "../components/ui/ButtonUI.js";
import BackImg from "../assets/img/Back.js";
import MultiDonutChartUI from "../components/ui/MultiDonutChartUI.js";
import InputUI from "../components/ui/InputUI.js";
import DropdownUI from "../components/ui/DropdownUI.js";
import { MEAL_TYPE } from "../utils/constants.js";
import { mapToOptions } from "../utils/functions.js";
import { getToday } from "../utils/functions.js";
import { API } from "../api/api.js";

// import DonutChartUI from "../components/ui/DonutChartUI";

export default function ResultView({ route, navigation }) {
  const { showMessage } = useContext(NotificationContext);

  const { imgdata } = route.params ?? {};
  const { image } = route.params ?? {};
  const [focusedField, setFocusedField] = useState(null);
  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    MealID: 0,
    Date: route.params?.date ?? getToday(),
    MealType: route.params?.MealType ?? null,
    Product: {
      ProductID: 0,
      ProductName: "",
      Calories: imgdata?.calories_max,
      Protein: imgdata?.proteins,
      Fats: imgdata?.fats,
      Carbonates: imgdata?.carbs,
    },
  });

  const handleChange = (path, value) => {
    setFormData((prev) => {
      const keys = path.split(".");
      const updated = { ...prev };

      let current = updated;

      for (let i = 0; i < keys.length - 1; i++) {
        const key = keys[i];

        current[key] = { ...current[key] };
        current = current[key];
      }

      current[keys[keys.length - 1]] = value;

      return updated;
    });
  };

  const handleSend = async () => {
    if (!formData.Product.ProductName.trim()) {
      showMessage("Введите название блюда");
      return;
    }

    if (!formData.MealType) {
      showMessage("Выберите прием пищи");
      return;
    }
    setLoading(true);

    try {
      // console.log(formData);

      const res = await API.postProductMeal(formData);
      // console.log(res);
      setLoading(false);
      navigation.navigate("Home");
    } catch (err) {
      setLoading(false);
      const msg = err.response?.data?.detail?.message || "Ошибка добавения";
      showMessage(msg);
      console.log("Ошибка добавления:", err.response?.data);
    }
  };
  if (loading) {
    return (
      <View style={mainStyle.loaderScreen}>
        <ActivityIndicator size="large" color="#9ED228" />
      </View>
    );
  }
  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <ImageBackground
        style={styles.container}
        source={{ uri: image }}
        resizeMode="cover"
      >
        <View style={[mainStyle.whiteCard, styles.res_card]}>
          <BackImg
            style={styles.back}
            onPress={() => navigation.navigate("Home")}
          />
          <ScrollView
            contentContainerStyle={{ paddingBottom: 0 }}
            showsVerticalScrollIndicator={false}
          >
            <View style={[styles.res_card_scroll]}>
              <View style={styles.circle}>
                <MultiDonutChartUI
                  centerText={imgdata?.calories_max ?? 0}
                  protein={imgdata?.proteins ?? 0}
                  fats={imgdata?.fats ?? 0}
                  carbs={imgdata?.carbs ?? 0}
                />
              </View>
              {imgdata?.origin_text ? (
                <View style={[styles.res_w]}>
                  <InputUI
                    value={formData.Product.ProductName}
                    placeholder="Название блюда"
                    required
                    type="text"
                    onChangeText={(v) => handleChange("Product.ProductName", v)}
                    onFocus={() => setFocusedField("Product.ProductName")}
                    onBlur={() => setFocusedField(null)}
                    isFocused={focusedField === "Product.ProductName"}
                  />
                  {/* <Text style={[mainStyle.h1, styles.label]}>Название блюда</Text>
                <SettingImg /> */}
                  <DropdownUI
                    options={mapToOptions(MEAL_TYPE)}
                    required
                    value={formData.MealType ?? null}
                    onSelect={(v) => handleChange("MealType", v)}
                  />
                </View>
              ) : (
                <View></View>
              )}

              <View style={[styles.res_w, styles.res_p]}>
                <View style={[styles.res_kbjy]}>
                  <Text style={[mainStyle.h1, styles.label]}>Белок</Text>
                  <Text style={[mainStyle.h2, styles.text_m]}>
                    {imgdata?.proteins ?? "-"}
                  </Text>
                  <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                    грамм
                  </Text>
                </View>
                <View style={[styles.res_kbjy, { borderColor: "#F9E5B8" }]}>
                  <Text style={[mainStyle.h1, styles.label]}>Жиры</Text>
                  <Text style={[mainStyle.h2, styles.text_m]}>
                    {imgdata?.fats ?? "-"}
                  </Text>
                  <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                    грамм
                  </Text>
                </View>
                <View style={[styles.res_kbjy, { borderColor: "#B6E8FF" }]}>
                  <Text style={[mainStyle.h1, styles.label]}>Углеводы</Text>
                  <Text style={[mainStyle.h2, styles.text_m]}>
                    {imgdata?.carbs ?? "-"}
                  </Text>
                  <Text style={[mainStyle.p_light, { textAlign: "center" }]}>
                    грамм
                  </Text>
                </View>
              </View>
              {/* <View style={[mainStyle.start_bloc, styles.res_f]}>
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
            </View> */}
              <View style={[styles.res_w]}>
                <Text style={mainStyle.p}>
                  {imgdata?.origin_text ?? "Не удалось распознать"}
                </Text>
              </View>
              {imgdata?.origin_text ? (
                <ButtonUI
                  title={"Добавить"}
                  green={true}
                  onPress={handleSend}
                />
              ) : (
                <ButtonUI
                  title={"Назад"}
                  green={true}
                  onPress={() => navigation.navigate("Home")}
                />
              )}
            </View>
          </ScrollView>
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
    zIndex: 20,
  },
  res_card: {
    // flex: 1,
    backgroundColor: "#F6F6F6",
    // gap: 10,
    position: "relative",
    // paddingTop: 20,
    // paddingBottom: 20,
  },
  res_card_scroll: {
    flex: 1,
    // backgroundColor: "#F6F6F6",
    gap: 10,
    // position: "relative",
    paddingTop: 20,
    paddingBottom: 20,
  },
  label: {
    fontSize: 15,
    maxWidth: 300,
  },
  res_w: {
    // flex: 1,
    // width:
    // flexDirection: "row",
    flexDirection: "column",

    justifyContent: "space-between",
    gap: 10,
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
    // flex: 1,
    flexDirection: "row",
    paddingTop: 9,
    paddingBottom: 9,
    gap: 0,
  },
  res_kbjy: {
    height: 110,
    width: 105,
    // flex: 1,
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
