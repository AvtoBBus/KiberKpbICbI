import React from "react";
import { View, TextInput, StyleSheet } from "react-native";
import { mainStyle } from "../../style";

export default function EmailUI({
  value,
  onChangeText,
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
        placeholder="Почта"
        placeholderTextColor="#999"
        keyboardType="email-address"
        autoCapitalize="none"
        value={value}
        onChangeText={onChangeText}
        onFocus={onFocus}
        onBlur={onBlur}
        style={[styles.input, mainStyle.p_input, styleInput]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    flex: 1,
    height: 60,
    width: "100%",
  },
});
