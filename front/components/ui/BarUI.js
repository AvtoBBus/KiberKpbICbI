import React, { useState } from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { BarChart, Grid } from "react-native-svg-charts";
import * as svg from "react-native-svg";

export default function BarChartBloc({ dataWeek, dataMonth, dataYear, goal }) {
  const [mode, setMode] = useState("week");
  const modes = ["week", "month", "year"];

  const chartData =
    mode === "week" ? dataWeek : mode === "month" ? dataMonth : dataYear;

  const CUT_OFF = goal;

  const HorizontalLine = ({ y }) => (
    <svg.Line
      x1="0"
      x2="100%"
      y1={y(CUT_OFF)}
      y2={y(CUT_OFF)}
      stroke="#BDBDBD"
      strokeWidth="1"
      strokeDasharray={[6, 4]}
    />
  );

  return (
    <View style={styles.wrapper}>
      <Text style={styles.title}>Белки</Text>

      <View style={styles.tabs}>
        {modes.map((m) => (
          <TouchableOpacity
            key={m}
            onPress={() => setMode(m)}
            style={[styles.tab, mode === m && styles.tabActive]}
          >
            <Text style={[styles.tabText, mode === m && styles.tabTextActive]}>
              {m === "week" ? "неделя" : m === "month" ? "месяц" : "год"}
            </Text>
          </TouchableOpacity>
        ))}
      </View>

      <View style={{ height: 250, marginTop: 20 }}>
        <BarChart
          style={{ flex: 1 }}
          data={chartData.map((i) => i.value)}
          svg={{
            fill: (value, index) =>
              chartData[index].highlight ? "#F9A825" : "#9ED228",
          }}
          contentInset={{ top: 20, bottom: 20 }}
          spacingInner={0.3}
          gridMin={0}
        >
          <Grid svg={{ stroke: "#eee" }} />
          <HorizontalLine />
        </BarChart>

        {/* подписи под столбиками */}
        <View style={styles.labelsRow}>
          {chartData.map((item, idx) => (
            <Text key={idx} style={styles.label}>
              {item.label}
            </Text>
          ))}
        </View>

        <Text style={styles.goalText}>Цель ({goal})</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    backgroundColor: "#fff",
    padding: 16,
    borderRadius: 12,
  },
  title: {
    fontSize: 26,
    fontWeight: "500",
    marginBottom: 10,
  },

  tabs: {
    flexDirection: "row",
    borderWidth: 2,
    borderColor: "#9ED228",
    borderRadius: 12,
    overflow: "hidden",
  },
  tab: {
    flex: 1,
    paddingVertical: 8,
    backgroundColor: "#fff",
    alignItems: "center",
  },
  tabActive: {
    backgroundColor: "#9ED228",
  },
  tabText: {
    fontSize: 16,
    color: "#333",
  },
  tabTextActive: {
    color: "#fff",
  },

  labelsRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 6,
  },
  label: {
    fontSize: 12,
    color: "#666",
  },

  goalText: {
    position: "absolute",
    right: 0,
    top: 0,
    fontSize: 12,
    color: "#999",
  },
});
