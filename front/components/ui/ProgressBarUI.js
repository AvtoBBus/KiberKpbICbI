import React, { useEffect, useRef } from "react";
import { View, Text, StyleSheet, Animated } from "react-native";

export default function ProgressBarUI({
  title = "белки",
  current = 20,
  total = 100,
  color = "#9ED228",
  bgColor = "#DFF3A8",
  style,
  duration = 800,
}) {
  const percent = Math.min(current / total, 1);

  const animatedWidth = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(animatedWidth, {
      toValue: percent,
      duration: duration,
      useNativeDriver: false,
    }).start();
  }, [percent]);

  const widthInterpolated = animatedWidth.interpolate({
    inputRange: [0, 1],
    outputRange: ["0%", "100%"],
  });

  return (
    <View style={[styles.container, style]}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.values}>
        {current}/{total}
      </Text>

      <View style={[styles.barBackground, { backgroundColor: bgColor }]}>
        <Animated.View
          style={[
            styles.barFill,
            {
              backgroundColor: color,
              width: widthInterpolated,
            },
          ]}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    width: "100%",
    marginTop: 5,
  },

  title: {
    fontSize: 16,
    fontWeight: "400",
    marginBottom: 4,
  },

  values: {
    fontSize: 12,
    color: "#000",
    fontWeight: "300",
    marginBottom: 6,
  },

  barBackground: {
    width: "100%",
    height: 7,
    borderRadius: 10,
    overflow: "hidden",
  },

  barFill: {
    height: "100%",
    borderRadius: 10,
  },
});
