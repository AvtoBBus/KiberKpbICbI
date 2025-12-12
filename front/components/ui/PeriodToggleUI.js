import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function PeriodToggleUI({ period, onChange }) {
  const options = ["week", "month", "year"];

  const labels = {
    week: "неделя",
    month: "месяц",
    year: "2 месяца",
  };

  return (
    <View style={styles.wrapper}>
      {options.map((opt) => {
        const isActive = opt === period;

        return (
          <TouchableOpacity
            key={opt}
            onPress={() => onChange(opt)}
            style={[styles.btn, isActive && styles.active]}
          >
            <Text style={[styles.text, isActive && styles.activeText]}>
              {labels[opt]}
            </Text>
          </TouchableOpacity>
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    flexDirection: "row",
    borderWidth: 2,
    borderColor: "#9ED228",
    borderRadius: 10,
    padding: 4,
    justifyContent: "space-between",
    backgroundColor: "#F6F6F6",
  },

  btn: {
    flex: 1,
    paddingVertical: 8,
    borderRadius: 5,
    alignItems: "center",
  },

  active: {
    backgroundColor: "#9ED228",
  },

  text: {
    fontSize: 16,
    color: "#000",
  },

  activeText: {
    color: "#fff",
    fontWeight: "500",
  },
});
