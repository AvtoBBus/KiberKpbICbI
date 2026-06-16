import React from "react";
import { StyleSheet, View, Text } from "react-native";
import { Dropdown } from "react-native-element-dropdown";
import { mainStyle } from "../../style";

export default function DropdownUI({
  options = [], // [{ label: "Подвижный", value: 2 }, ...]
  value,
  onSelect,
  label = "Выберите значение",
  placeholder = "Выберите значение",
  required = false,
  style,
}) {
  const isEmpty =
    required && (value === null || value === undefined || value === "");
  return (
    <View style={[styles.container, style]}>
      <Text style={mainStyle.p}>{label}</Text>
      <Dropdown
        data={options}
        labelField="label"
        valueField="value"
        placeholder={placeholder + (required ? " *" : "")}
        placeholderStyle={[styles.placeholderStyle]}
        selectedTextStyle={styles.selectedTextStyle}
        itemTextStyle={styles.itemTextStyle}
        value={value}
        onChange={(item) => onSelect(item.value)}
        style={[
          mainStyle.inputContainer,
          styles.dropdown,
          isEmpty && { borderColor: "red" },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: "100%",
    gap: 5,
  },
  dropdown: {
    height: 50,
    borderRadius: 8,
    paddingHorizontal: 8,
  },
  placeholderStyle: {
    color: "#999",
  },
  selectedTextStyle: {
    color: "#000",
  },
  itemTextStyle: {
    color: "#000",
  },
});
