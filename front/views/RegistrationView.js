import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { AuthAPI } from "../api/api.js";
import { Keyboard, TouchableWithoutFeedback } from "react-native";
import { mainStyle } from "../style";
import { stylesAuth } from "../style/auto.js";
import EmailUI from "../components/ui/EmailUI";
import PasswordInput from "../components/ui/PasswordUI";
import ButtonUI from "../components/ui/ButtonUI";
import Fingerprint from "../assets/img/a-1.svg";

export default function RegistrationView({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [secure, setSecure] = useState(true);
  const [focusedField, setFocusedField] = useState(null);

  const handleLogin = async () => {
    try {
      const res = await AuthAPI.registration(email.trim(), password);
      navigation.reset({
        index: 0,
        routes: [{ name: "EditUser" }],
      });
    } catch (err) {
      console.log("Ошибка входа:", err.response?.data || err.message);
    }
  };

  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <View style={stylesAuth.container}>
        <View style={mainStyle.whiteCard}>
          <View style={stylesAuth.imageWrapper}>
            <Fingerprint width={60} height={60} />
          </View>

          <Text style={mainStyle.h1}>Регистрация</Text>

          <EmailUI
            value={email}
            onChangeText={setEmail}
            onFocus={() => setFocusedField("email")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "email"}
            style={stylesAuth.email}
          />
          <PasswordInput
            value={password}
            onChangeText={setPassword}
            secure={secure}
            onToggleSecure={() => setSecure(!secure)}
            onFocus={() => setFocusedField("password")}
            onBlur={() => setFocusedField(null)}
            isFocused={focusedField === "password"}
          />
          <Text style={[styles.text, mainStyle.p_light, styles.margin]}>
            – Минимум 12 символов
          </Text>
          <Text style={[styles.text, mainStyle.p_light]}>
            – Буквы верхнего и нижнего регистра
          </Text>
          <Text style={[styles.text, mainStyle.p_light]}>– 1 цифра</Text>
          <Text style={[styles.text, mainStyle.p_light]}>
            – 1 специальный символ
          </Text>

          <ButtonUI
            style={stylesAuth.button}
            title={"Регистрация"}
            green={true}
            onPress={handleLogin}
          />
          <ButtonUI
            title={"Уже есть аккаунт?"}
            gray={true}
            onPress={() => navigation.navigate("Authorization")}
          />
        </View>
      </View>
    </TouchableWithoutFeedback>
  );
}

const styles = StyleSheet.create({
  margin: {
    marginTop: 33,
  },
  text: {
    color: "black",
  },
});
