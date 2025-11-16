import React, { useState } from "react";
import { View, StyleSheet, Text } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { mainStyle } from "../style";
import { API } from "../api/api.js";
import InputUI from "../components/ui/InputUI";
import ButtonUI from "../components/ui/ButtonUI";
import BackImg from "../assets/img/back.svg";

export default function EditUserView({ route, navigation }) {
  const { Userdata } = route.params ?? {};
  const flag = Userdata && Object.keys(Userdata).length > 0;

  const [focusedField, setFocusedField] = useState(null);

  const [formData, setFormData] = useState({
    UserName: Userdata?.UserName ?? "",
    Age: String(Userdata?.Age ?? ""),
    Height: String(Userdata?.Height ?? ""),
    Weight: String(Userdata?.Weight ?? ""),
    DesiredWeight: String(Userdata?.DesiredWeight ?? ""),
    DesiredHeight: String(Userdata?.DesiredHeight ?? ""),
    Activity: String(Userdata?.Activity ?? ""),
    UserDataID: Userdata?.UserDataID ?? 0,
  });

  const handleChange = (field, value) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleUser = async () => {
    try {
      const payload = {
        ...formData,
        // UserDataID: formData.UserDataID,
        Age: Number(formData.Age),
        Height: Number(formData.Height),
        Weight: Number(formData.Weight),
        DesiredWeight: Number(formData.DesiredWeight),
        DesiredHeight: Number(formData.DesiredHeight),
        Activity: Number(formData.Activity),
        UserName: formData.UserName,
      };
      // console.log("Сохранено:", formData);
      // console.log("Сохранено:", payload);
      if (flag) {
        const res = await API.putUserData(payload); // { ...payload, UserDataID: 0 }
        navigation.goBack();
      } else {
        const res = await API.postUserData(payload);
        navigation.navigate("Home");
      }
    } catch (err) {
      console.log("Ошибка сохранения:", err.response?.data || err.message);
    }
  };

  return (
    <View style={{ height: "100%" }}>
      <SafeAreaView style={mainStyle.main_bloc}>
        <View style={mainStyle.start_bloc}>
          {flag && (
            <BackImg
              width={30}
              height={30}
              onPress={() => navigation.goBack()}
            />
          )}
          <Text style={mainStyle.h1}>Настройки профиля</Text>
        </View>
        <View style={[mainStyle.white_bloc, styles.inputPadding]}>
          <InputUI
            value={formData.UserName}
            placeholder="Имя"
            required
            type="text"
            onChangeText={(v) => handleChange("UserName", v)}
            onFocus={() => setFocusedField("UserName")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "UserName"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.Age}
            placeholder="Возраст"
            required
            type="numeric"
            onChangeText={(v) => handleChange("Age", v)}
            onFocus={() => setFocusedField("Age")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "Age"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.Height}
            placeholder="Рост"
            required
            type="numeric"
            onChangeText={(v) => handleChange("Height", v)}
            onFocus={() => setFocusedField("Height")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "Height"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.Weight}
            placeholder="Вес"
            required
            type="numeric"
            onChangeText={(v) => handleChange("Weight", v)}
            onFocus={() => setFocusedField("Weight")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "Weight"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.DesiredWeight}
            placeholder="Желаемый вес"
            required
            type="numeric"
            onChangeText={(v) => handleChange("DesiredWeight", v)}
            onFocus={() => setFocusedField("DesiredWeight")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "DesiredWeight"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.DesiredHeight}
            placeholder="Желаемый рост"
            required
            type="numeric"
            onChangeText={(v) => handleChange("DesiredHeight", v)}
            onFocus={() => setFocusedField("DesiredHeight")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "DesiredHeight"}
            style={styles.inputWight}
          />
          <InputUI
            value={formData.Activity}
            placeholder="Активность"
            required
            type="numeric"
            onChangeText={(v) => handleChange("Activity", v)}
            onFocus={() => setFocusedField("Activity")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "Activity"}
          />

          <ButtonUI
            title={"Сохранить"}
            green={true}
            onPress={handleUser}
            style={styles.inputWight}
          />
        </View>
      </SafeAreaView>
    </View>
  );
}

const styles = StyleSheet.create({
  //   main_bloc: {
  //     flex: 1,
  //     flexDirection: "column",
  //     justifyContent: "start",
  //     alignItems: "center",
  //   },
  //   start_bloc: {
  //     width: 334,
  //     flexDirection: "column",
  //     justifyContent: "space-between",
  //     alignItems: "center",
  //     marginBottom: 20,
  //     marginTop: 20,
  //     gap: 20,
  //     backgroundColor: "white",
  //     borderRadius: 10,
  //     paddingTop: 20,
  //     paddingBottom: 10,
  //   },
  inputWight: {
    // marginLeft: 10,
    // marginRight: 10,
    width: "90%",
  },
  inputPadding: {
    paddingLeft: 0,
    paddingRight: 0,
  },
});
