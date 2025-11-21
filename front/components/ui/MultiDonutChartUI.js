import React from "react";
import { View, StyleSheet, Text } from "react-native";
import Svg, { Path, Circle } from "react-native-svg";
import { mainStyle } from "../../style";

function polarToCartesian(cx, cy, r, angleDeg) {
  const angleRad = ((angleDeg - 90) * Math.PI) / 180;
  return {
    x: cx + r * Math.cos(angleRad),
    y: cy + r * Math.sin(angleRad),
  };
}

function arcPath(cx, cy, r, startAngle, endAngle) {
  const start = polarToCartesian(cx, cy, r, startAngle);
  const end = polarToCartesian(cx, cy, r, endAngle);

  const largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";
  const sweepFlag = 1;

  return `M ${start.x} ${start.y} A ${r} ${r} 0 ${largeArcFlag} ${sweepFlag} ${end.x} ${end.y}`;
}

export default function MultiDonutChartUI({
  protein = 0,
  fats = 0,
  carbs = 0,
  size = 150,
  strokeWidth = 16,
  bgColor = "#E3F5B5",
  centerText = "--",
}) {
  const radius = (size - strokeWidth) / 2;
  const cx = size / 2;
  const cy = size / 2;

  const total = protein + fats + carbs || 1;

  const segments = [
    { value: protein, color: "#D6F3A1" },
    { value: fats, color: "#F9E5B8" },
    { value: carbs, color: "#B6E8FF" },
  ].filter((s) => s.value > 0);

  let currentAngle = 0;

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
          cx={cx}
          cy={cy}
          r={radius}
          stroke={bgColor}
          strokeWidth={strokeWidth}
          fill="none"
        />

        {segments.map((seg, index) => {
          const segmentAngle = (seg.value / total) * 360;
          const startAngle = currentAngle;
          const endAngle = currentAngle + segmentAngle;

          const d = arcPath(cx, cy, radius, startAngle, endAngle);

          currentAngle = endAngle;

          return (
            <Path
              key={index}
              d={d}
              stroke={seg.color}
              strokeWidth={strokeWidth}
              strokeLinecap="butt"
              fill="none"
            />
          );
        })}
      </Svg>

      <View style={styles.centerText}>
        <Text style={[mainStyle.h2, styles.text]}>{centerText}</Text>
        <Text style={[mainStyle.p_light]}>Килокалорий</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  centerText: {
    position: "absolute",
    justifyContent: "center",
    alignItems: "center",
  },
  text: {
    fontSize: 27,
    fontWeight: "600",
    color: "#9ED228",
    marginTop: 0,
  },
});
