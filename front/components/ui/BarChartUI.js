import React, { useState } from "react";
import { View, Text, StyleSheet } from "react-native";
import { BarChart } from "react-native-gifted-charts";

export default function BarChartUI({
  data = [],
  goalValue = null,
  height = 200,
}) {
  const [chartWidth, setChartWidth] = useState(0);

  // 1) Определяем количество точек
  const N = data.length;

  // 2) Авто-режим ширины столбика
  const barWidth =
    N <= 10
      ? 15 // неделя
      : N <= 31
      ? 5 // месяц
      : 2; // год или большие данные

  // 3) Авто-spacing, чтобы график идеально заполнил ширину
  // const spacing = chartWidth
  //   ? Math.max((chartWidth - N * barWidth) / (N + 1), 1)
  //   : 2;

  const spacing =
    N <= 10
      ? 17 // неделя
      : N <= 31
      ? 3 // месяц
      : 2; // год или большие данные

  // 4) Авто-maxValue (учёт цели)
  const maxValue = (() => {
    const maxDataValue = data.length
      ? Math.max(...data.map((d) => d.value))
      : 0;
    const base = goalValue ? Math.max(maxDataValue, goalValue) : maxDataValue;
    return base + base * 0.1 + 10; // добавляем запас
  })();

  const chartData = data.map((item) => ({
    ...item,
    // кастомный компонент подписи под столбиком
    labelComponent: () => <Text style={styles.min}>{item.label}</Text>,
  }));

  return (
    <View
      style={styles.wrapper}
      onLayout={(e) => setChartWidth(e.nativeEvent.layout.width)}
    >
      {
        <>
          <BarChart
            data={chartData}
            // initialSpacing={0}
            barWidth={barWidth}
            spacing={spacing}
            height={height}
            maxValue={maxValue}
            noOfSections={5}
            isAnimated
            disableScroll={true}
            // adjustToWidth={true}
            // xAxisLabelTextStyle={{ fontSize: 6 }}
            yAxisTextStyle={{ fontSize: 8 }}
            xAxisColor="#DDD"
            yAxisColor="#DDD"
            // horizontalRulesStyle={{
            //   strokeDasharray: "4 4",
            //   strokeWidth: 1,
            // }}
          />

          {goalValue != null && (
            <View
              style={[
                styles.goalLine,
                {
                  top: (1 - goalValue / maxValue) * height,
                  width: 290,
                },
              ]}
            >
              <Text style={styles.goalText}>Цель: {goalValue}</Text>
            </View>
          )}
        </>
      }
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    maxWidth: "100%",
    // minHeight: 200,
    marginVertical: 15,
    // overflow: "hidden",
  },
  goalLine: {
    position: "absolute",
    height: 1,
    borderStyle: "dashed",
    borderWidth: 1,
    borderColor: "#9ED228",
  },
  goalText: {
    position: "absolute",
    right: 0,
    top: -15,
    fontSize: 10,
    color: "#333",
  },
  xLabel: {
    fontSize: 6,
    transform: [{ rotate: "-90deg" }], // или "90deg" — как больше нравится
    marginTop: 8,
    width: 24, // важно, чтобы текст не обрезался
    textAlign: "center",
  },
  min: {
    opacity: 0,
  },
});
