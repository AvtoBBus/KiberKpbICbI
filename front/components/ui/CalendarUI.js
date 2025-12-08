import React, { useState, useEffect } from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

const WEEK_DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"];

export default function CalendarUI({ selected, onSelect }) {
  const selectedDate = new Date(selected);
  const [currentDate, setCurrentDate] = useState(selectedDate);

  useEffect(() => {
    setCurrentDate(new Date(selected));
  }, [selected]);

  const getStartOfWeek = (date) => {
    const day = date.getDay();
    const diff = day === 0 ? -6 : 1 - day;
    const start = new Date(date);
    start.setDate(date.getDate() + diff);
    return start;
  };

  const startOfWeek = getStartOfWeek(currentDate);

  const days = [...Array(7)].map((_, i) => {
    const d = new Date(startOfWeek);
    d.setDate(startOfWeek.getDate() + i);
    return d;
  });

  const monthName = currentDate.toLocaleString("ru-RU", { month: "long" });

  const changeWeek = (direction) => {
    const newDate = new Date(currentDate);
    newDate.setDate(currentDate.getDate() + direction * 7);
    setCurrentDate(newDate);
  };

  return (
    <View style={[styles.wrapper, { maxWidth: 334 }]}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => changeWeek(-1)}>
          <Text style={styles.arrow}>{"<"}</Text>
        </TouchableOpacity>

        <Text style={styles.month}>
          {monthName.charAt(0).toUpperCase() + monthName.slice(1)}{" "}
          {currentDate.getFullYear()}
        </Text>

        <TouchableOpacity onPress={() => changeWeek(1)}>
          <Text style={styles.arrow}>{">"}</Text>
        </TouchableOpacity>
      </View>

      <View style={styles.weekRow}>
        {WEEK_DAYS.map((d) => (
          <Text key={d} style={styles.weekDay}>
            {d}
          </Text>
        ))}
      </View>

      <View style={styles.daysRow}>
        {days.map((day, idx) => {
          const iso = day.toISOString().split("T")[0];
          const isSelected = selected === iso;

          return (
            <TouchableOpacity
              key={idx}
              style={[styles.dayContainer, isSelected && styles.daySelected]}
              onPress={() => onSelect(iso)}
            >
              <Text style={styles.dayText}>{day.getDate()}</Text>
            </TouchableOpacity>
          );
        })}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    backgroundColor: "#fff",
    borderRadius: 12,
    padding: 15,
    marginBottom: 20,
  },

  header: {
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    marginBottom: 10,
  },

  arrow: {
    fontSize: 30,
    color: "#9ED228",
  },

  month: {
    fontSize: 20,
    fontWeight: "400",
  },

  weekRow: {
    flexDirection: "row",
    justifyContent: "center",
    marginBottom: 5,
  },

  weekDay: {
    width: 45,
    textAlign: "center",
    color: "#000",
    fontWeight: "400",
  },

  daysRow: {
    flexDirection: "row",
    justifyContent: "center",
  },

  dayContainer: {
    width: 45,
    height: 25,
    borderRadius: 8,
    justifyContent: "center",
    alignItems: "center",
  },

  daySelected: {
    backgroundColor: "#D9F7A0",
  },

  dayText: {
    fontSize: 16,
    color: "#000",
  },
});
