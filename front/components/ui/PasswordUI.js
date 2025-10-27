import React from "react";
import { View, TextInput, TouchableOpacity, StyleSheet } from "react-native";
import { Feather } from "@expo/vector-icons";
import { mainStyle } from "../../style";

export default function PasswordInput({
  value,
  onChangeText,
  secure,
  onToggleSecure,
  onFocus,
  onBlur,
  isFocused,
  style,
  styleInput,
}) {
  return (
    <View
      style={[
        mainStyle.inputContainer,
        isFocused && mainStyle.inputContainerFocus,
        style,
      ]}
    >
      <TextInput
        placeholder="Пароль"
        placeholderTextColor="#999"
        secureTextEntry={secure}
        autoCapitalize="none"
        value={value}
        onChangeText={onChangeText}
        onFocus={onFocus}
        onBlur={onBlur}
        style={[styles.input, mainStyle.p_input, styleInput]}
      />
      <TouchableOpacity style={styles.eyeIcon} onPress={onToggleSecure}>
        <Feather name={secure ? "eye-off" : "eye"} size={18} color="black" />
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    flex: 1,
    height: 60,
    width: "100%",
  },
  eyeIcon: {
    paddingHorizontal: 5,
  },
});
