import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function LoadingView({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Экран загрузки</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Authorization")}
      >
        <Text style={styles.buttonText}>Перейти на авторизацию</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Home")}
      >
        <Text style={styles.buttonText}>Перейти на главную</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={styles.button}
        onPress={() => navigation.navigate("Result")}
      >
        <Text style={styles.buttonText}>Перейти на результат</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111",
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    color: "white",
    fontSize: 30,
    marginBottom: 40,
  },
  button: {
    backgroundColor: "#2ecc71",
    padding: 15,
    borderRadius: 10,
    marginVertical: 10,
    width: "80%",
    alignItems: "center",
  },
  buttonText: {
    color: "white",
    fontSize: 20,
  },
});