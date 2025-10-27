import React, { useState } from "react";
import { TouchableOpacity, Text, StyleSheet } from "react-native";

export default function ButtonUI({ title, onPress, green, gray, style }) {
  const [isPressed, setIsPressed] = useState(false);

  const buttonStyle = [
    styles.button,
    green && (isPressed ? styles.greenPress : styles.green),
    gray && (isPressed ? styles.grayPress : styles.gray),
    style,
  ];

  const textStyle = [
    styles.text,
    green && (isPressed ? styles.textGreenPress : styles.textGreen),
    gray && (isPressed ? styles.textGrayPress : styles.textGray),
  ];

  return (
    <TouchableOpacity
      style={buttonStyle}
      onPress={onPress}
      activeOpacity={1}
      onPressIn={() => setIsPressed(true)}
      onPressOut={() => setIsPressed(false)}
    >
      <Text style={textStyle}>{title}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    borderRadius: 10,
    height: 50,
    alignItems: "center",
    justifyContent: "center",
  },

  green: {
    backgroundColor: "#A5D66D",
  },
  greenPress: {
    backgroundColor: "#D6F3A1",
  },

  textGreen: {
    color: "white",
    fontWeight: "600",
    fontSize: 16,
  },
  textGreenPress: {
    color: "#A5D66D",
    fontWeight: "600",
    fontSize: 16,
  },

  gray: {
    backgroundColor: "#F6F6F6",
  },
  grayPress: {
    backgroundColor: "#E6E6E6",
  },

  textGray: {
    color: "#A5D66D",
    fontWeight: "600",
    fontSize: 16,
  },
  textGrayPress: {
    color: "white",
    fontWeight: "600",
    fontSize: 16,
  },

  text: {
    fontWeight: 300,
    textAlign: "center",
    fontSize: 18,
    lineHeight: 125,
    textAlign: "center",
    textAlignVertical: "center",
  },
});
