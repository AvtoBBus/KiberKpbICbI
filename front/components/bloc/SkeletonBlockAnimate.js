import React, { useEffect, useRef } from "react";
import { Animated, View, StyleSheet } from "react-native";

export default function SkeletonBlock({ height = 120, width = 335, style }) {
  const shimmer = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.loop(
      Animated.timing(shimmer, {
        toValue: 1,
        duration: 1300,
        useNativeDriver: true,
      })
    ).start();
  }, []);

  const translateX = shimmer.interpolate({
    inputRange: [0, 1],
    outputRange: [-width, width], // двигаем строго по диагонали
  });

  return (
    <View style={[styles.container, { height, width }, style]}>
      <Animated.View
        style={[
          styles.shimmer,
          {
            transform: [
              { translateX },
              { rotate: "-20deg" }, // угол блика
            ],
          },
        ]}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    overflow: "hidden",
    backgroundColor: "#E6E6E6",
    borderRadius: 12,
    marginVertical: 8,
  },

  shimmer: {
    position: "absolute",
    height: "170%",
    width: "50%",
    top: "-35%",
    backgroundColor: "rgba(255,255,255,0.35)",
    opacity: 0.7,
    borderRadius: 12,
  },
});
