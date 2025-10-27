import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
} from "react-native";

import { mainStyle } from "../style";
import { Feather } from "@expo/vector-icons";
import EmailUI from "../components/ui/EmailUI";
import PasswordInput from "../components/ui/PasswordUI";
import ButtonUI from "../components/ui/ButtonUI";

export default function AuthorizationView({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [secure, setSecure] = useState(true);
  const [focusedField, setFocusedField] = useState(null);

  return (
    <View style={styles.container}>
      <View style={mainStyle.whiteCard}>
        {/* <Feather name="fingerprint" size={60} color="#A5D66D" /> */}
        <Text style={mainStyle.h1}>Вход в систему</Text>

        <EmailUI
          value={email}
          onChangeText={setEmail}
          onFocus={() => setFocusedField("email")}
          onBlur={() => setFocusedField(null)}
          isFocused={focusedField === "email"}
          style={styles.email}
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
        <Text style={[styles.text, mainStyle.p_light]}>Забыли пароль?</Text>
        <ButtonUI style={styles.button} title={"Войти"} green={true} />
        <ButtonUI title={"Создать аккаунт"} gray={true} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#D6F3A1",
    paddingTop: 215,
  },
  input: {
    flex: 1,
    height: 60,
    width: "100%",
  },
  email: {
    marginBottom: 20,
    marginTop: 30,
  },
  button: {
    marginTop: 20,
    marginBottom: 20,
  },
  text: {
    color: "#9ED228",
    marginTop: 33,
  },
  // eyeIcon: {
  //   paddingHorizontal: 5,
  // },
});
