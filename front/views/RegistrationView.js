import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { AuthAPI } from "../api/api.js";
import { Keyboard, TouchableWithoutFeedback } from "react-native";
import { mainStyle } from "../style";
import { stylesAuth } from "../style/auto.js";
import EmailUI from "../components/ui/EmailUI";
import PasswordInput from "../components/ui/PasswordUI";
import ButtonUI from "../components/ui/ButtonUI";
import Fingerprint from "../assets/img/Fingerprint.js";
import { useContext } from "react";
import { NotificationContext } from "../store";

export default function RegistrationView({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [secure, setSecure] = useState(true);
  const [focusedField, setFocusedField] = useState(null);
  const { showMessage } = useContext(NotificationContext);

  const handleLogin = async () => {
    if (!email.trim() || !password.trim()) {
      showMessage("Введите email и пароль для регистрации");
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.trim())) {
      showMessage("Введите корректный email");
      return;
    }

    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9]).{12,}$/;

    if (!passwordRegex.test(password)) {
      showMessage(
        "Пароль должен содержать минимум 12 символов, заглавные и строчные буквы и хотя бы один специальный символ"
      );
      return;
    }

    try {
      const res = await AuthAPI.registration(email.trim(), password);
      navigation.reset({
        index: 0,
        routes: [{ name: "EditUser" }],
      });
    } catch (err) {
      const msg = err.response?.data?.detail?.message || "Ошибка регистрации";
      showMessage(msg);
      console.log("Ошибка входа:", err.response?.data);
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
            onPress={() => navigation.goBack()}
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
