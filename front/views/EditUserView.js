import React, { useState } from "react";
import { View, StyleSheet, Text, TouchableOpacity } from "react-native";
import { Keyboard, TouchableWithoutFeedback } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { mainStyle } from "../style";
import { API } from "../api/api.js";
import InputUI from "../components/ui/InputUI";
import ButtonUI from "../components/ui/ButtonUI";
import DropdownUI from "../components/ui/DropdownUI.js";
import BackImg from "../assets/img/Back.js";
import { ACTIVITY, GENDER } from "../utils/constants";
import { mapToOptions } from "../utils/functions.js";

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
    Activity: Userdata?.Activity ?? null,
    Gender: Userdata?.Gender ?? null,
    // UserDataID: Userdata?.UserDataID ?? 0,
  });

  const handleChange = (field, value) => {
    // console.log(field, value);
    setFormData((prev) => ({ ...prev, [field]: value }));
  };

  const handleUser = async () => {
    try {
      const payload = {
        ...formData,
        Age: Number(formData.Age),
        Height: Number(formData.Height),
        Weight: Number(formData.Weight),
        DesiredWeight: Number(formData.DesiredWeight),
        DesiredHeight: Number(formData.DesiredHeight),
        Activity: Number(formData.Activity),
        Gender: formData.Gender,
        UserName: formData.UserName,
      };
      const norma = {
        Age: Number(formData.Age),
        Height: Number(formData.Height),
        Weight: Number(formData.Weight),
        DesiredWeight: Number(formData.DesiredWeight),
        Activity: Number(formData.Activity),
        Gender: formData.Gender,
      };
      if (flag) {
        const res = await API.putUserData(payload);
        await API.putStatNorm(norma);
        navigation.goBack();
      } else {
        const res = await API.postUserData(payload);
        await API.postStatNorm(norma);
        navigation.navigate("Home");
      }
    } catch (err) {
      console.log("Ошибка сохранения:", err.response?.data || err.message);
    }
  };

  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <View style={{ height: "100%" }}>
        <SafeAreaView style={mainStyle.main_bloc}>
          <View style={mainStyle.start_bloc}>
            {flag && (
              <TouchableOpacity onPress={() => navigation.goBack()}>
                <BackImg width={30} height={30} />
              </TouchableOpacity>
            )}
            <Text style={mainStyle.h1}>Настройки профиля</Text>
          </View>
          <View style={[mainStyle.white_bloc, styles.inputPadding]}>
            <DropdownUI
              options={mapToOptions(GENDER)}
              required
              value={formData.Gender}
              label="Пол"
              onSelect={(v) => handleChange("Gender", v)}
              placeholder="Выберите пол"
              style={styles.inputWight}
            />
            <DropdownUI
              options={mapToOptions(ACTIVITY)}
              required
              value={formData.Activity}
              label="Активность"
              onSelect={(v) => handleChange("Activity", v)}
              placeholder="Выберите активность"
              style={styles.inputWight}
            />
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
            <ButtonUI
              title={"Сохранить"}
              green={true}
              onPress={handleUser}
              style={styles.inputWight}
            />
          </View>
        </SafeAreaView>
      </View>
    </TouchableWithoutFeedback>
  );
}

const styles = StyleSheet.create({
  inputWight: {
    width: "90%",
  },
  inputPadding: {
    paddingLeft: 0,
    paddingRight: 0,
  },
});
