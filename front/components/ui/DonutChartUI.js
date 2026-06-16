import React, { useEffect, useRef } from "react";
import { View, Text, StyleSheet, Animated } from "react-native";
import Svg, { Circle } from "react-native-svg";

export default function DonutChartUI({
  percent = 0,
  size = 64,
  strokeWidth = 10,
  color = "#9ED228",
  bgColor = "#E3F5B5",
  duration = 800,
}) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;

  const animatedPercent = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(animatedPercent, {
      toValue: percent / 100,
      duration: duration,
      useNativeDriver: false,
    }).start();
  }, [percent]);

  const strokeDashoffset = animatedPercent.interpolate({
    inputRange: [0, 1],
    outputRange: [circumference, 0],
  });

  return (
    <View
      style={{
        width: size,
        height: size,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <Svg width={size} height={size}>
        <Circle
          stroke={bgColor}
          fill="none"
          cx={size / 2}
          cy={size / 2}
          r={radius}
          strokeWidth={strokeWidth}
        />

        <AnimatedCircle
          stroke={color}
          fill="none"
          cx={size / 2}
          cy={size / 2}
          r={radius}
          strokeWidth={strokeWidth}
          strokeDasharray={`${circumference} ${circumference}`}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          rotation="-90"
          origin={`${size / 2}, ${size / 2}`}
        />
      </Svg>

      <View style={styles.center}>
        <Text style={styles.percent}>{percent}%</Text>
      </View>
    </View>
  );
}

const AnimatedCircle = Animated.createAnimatedComponent(Circle);

const styles = StyleSheet.create({
  center: {
    position: "absolute",
    justifyContent: "center",
    alignItems: "center",
  },
  percent: {
    fontSize: 18,
    fontWeight: "600",
    color: "#000",
  },
});
