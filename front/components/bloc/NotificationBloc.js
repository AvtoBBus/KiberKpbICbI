import React, { useContext } from "react";
import { View, Text, StyleSheet, Animated } from "react-native";
import { NotificationContext } from "../../store";

export default function NotificationBloc() {
  const { message } = useContext(NotificationContext);

  if (!message) return null;

  return (
    <View style={styles.banner}>
      <Text style={styles.text}>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  banner: {
    position: "absolute",
    top: 40,
    left: 0,
    right: 0,
    padding: 14,
    backgroundColor: "#FF4043",
    zIndex: 100,
  },
  text: {
    color: "#fff",
    textAlign: "center",
    fontSize: 16,
  },
});
