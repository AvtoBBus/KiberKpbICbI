import React from "react";
import { View, StyleSheet } from "react-native";

export default function SkeletonBlock({ height = 80, width = "100%", style }) {
  return <View style={[styles.skeleton, { height, width }, style]} />;
}

const styles = StyleSheet.create({
  skeleton: {
    backgroundColor: "#E6E6E6",
    borderRadius: 10,
    opacity: 0.5,
    marginVertical: 6,
  },
});
