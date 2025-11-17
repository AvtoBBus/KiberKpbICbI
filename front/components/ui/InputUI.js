import React from "react";
import { View, TextInput, StyleSheet, Text } from "react-native";
import { mainStyle } from "../../style";

export default function InputUI({
  value,
  placeholder,
  type = "text",
  required = false,
  onChangeText,
  onFocus,
  onBlur,
  isFocused,
  style,
  styleInput,
}) {
  const isEmpty = required && !value?.trim();
  return (
    <View style={styles.main_bloc}>
      <Text style={mainStyle.p}>{placeholder}</Text>
      <View
        style={[
          mainStyle.inputContainer,
          isFocused && mainStyle.inputContainerFocus,
          isEmpty && { borderColor: "red" },
          style,
        ]}
      >
        <TextInput
          placeholder={placeholder + (required ? " *" : "")}
          placeholderTextColor="#999"
          keyboardType={type}
          autoCapitalize="none"
          value={value}
          onChangeText={onChangeText}
          onFocus={onFocus}
          onBlur={onBlur}
          style={[styles.input, mainStyle.p_input, styleInput]}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  input: {
    flex: 1,
    height: 40,
    width: "100%",
  },
  main_bloc: {
    gap: 5,
  },
});
