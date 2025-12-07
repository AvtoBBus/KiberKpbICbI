import React from "react";
import { View, StyleSheet } from "react-native";
import { mainStyle } from "../style";
import { BarChart } from "react-native-gifted-charts";

export default function StatisticView({ navigation }) {
  const data = [
    { value: 330, label: "03.09", frontColor: "#F4A623" },
    { value: 270, label: "04.09", frontColor: "#A4D96C" },
    { value: 400, label: "05.09", frontColor: "#F4A623" },
    { value: 140, label: "06.09", frontColor: "#A4D96C" },
  ];

  return (
    <View>
      <BarChart
        data={data}
        barWidth={35}
        height={350}
        noOfSections={5}
        maxValue={400}
        dashGap={6}
        dashWidth={4}
        showYAxisIndices
        yAxisColor={"#E0E0E0"}
        xAxisColor={"#E0E0E0"}
        spacing={30}
        isAnimated
        horizontalRulesStyle={{ strokeDasharray: "6 6" }}
        renderReferenceLines={(y) => {
          return (
            y === 350 && (
              <View
                style={{
                  position: "absolute",
                  top: 50,
                  width: "100%",
                  height: 1,
                  borderStyle: "dashed",
                  borderWidth: 1,
                  borderColor: "#999",
                }}
              >
                <Text style={{ position: "absolute", right: 0 }}>
                  Цель (468)
                </Text>
              </View>
            )
          );
        }}
      />
    </View>
  );
}

const styles = StyleSheet.create({});
