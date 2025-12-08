import React, { useContext, useEffect, useRef } from "react";
import { View, Text, StyleSheet, Animated } from "react-native";
import { NotificationContext } from "../../store";

export default function NotificationBloc() {
  const { messages, removeMessage } = useContext(NotificationContext);

  return (
    <View style={styles.container}>
      {messages.map((msg) => (
        <FadeMessage
          key={msg.id}
          id={msg.id}
          text={msg.text}
          onRemove={removeMessage}
        />
      ))}
    </View>
  );
}

function FadeMessage({ id, text, onRemove }) {
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(opacity, {
      toValue: 1,
      duration: 200,
      useNativeDriver: true,
    }).start();

    const timer = setTimeout(() => {
      Animated.timing(opacity, {
        toValue: 0,
        duration: 200,
        useNativeDriver: true,
      }).start(() => onRemove(id));
    }, 3000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <Animated.View style={[styles.banner, { opacity }]}>
      <Text style={styles.text}>{text}</Text>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: "absolute",
    top: 60,
    right: 10,
    width: 290,
    zIndex: 100,
    gap: 10,
  },
  banner: {
    padding: 16,
    backgroundColor: "#FF4043",
    borderRadius: 10,
  },
  text: {
    color: "#fff",
    fontSize: 15,
    textAlign: "center",
  },
});
