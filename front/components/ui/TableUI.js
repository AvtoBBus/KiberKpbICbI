import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { Table, Row } from "react-native-table-component";
import CrossImg from "../../assets/img/Cross.js";

export default function TableUI({ data, onDelete }) {
  const tableHead = ["Имя", "Б", "Ж", "У", "Ккал", ""];

  const tableRows = data.map((item) => [
    item.ProductName,
    item.Protein,
    item.Fats,
    item.Carbonates,
    item.Calories,
    <TouchableOpacity
      onPress={() => onDelete(item.ProductID)}
      style={styles.headText}
    >
      <CrossImg width={20} height={20} color="#FFB6B7" />
    </TouchableOpacity>,
  ]);

  return (
    <View style={styles.container}>
      <Table borderStyle={{ borderWidth: 0, borderColor: "transparent" }}>
        <Row
          data={tableHead}
          style={styles.head}
          textStyle={styles.headText}
          widthArr={[70, 40, 40, 40, 60, 40]}
        />

        {tableRows.map((rowData, index) => (
          <Row
            key={index}
            data={rowData}
            style={[
              styles.row,
              index === tableRows.length - 1 && styles.lastRow,
            ]}
            textStyle={[styles.headText, { fontWeight: "300" }]}
            widthArr={[70, 40, 40, 40, 60, 40]}
          />
        ))}
      </Table>
    </View>
  );
}
const styles = StyleSheet.create({
  container: {
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 10,
  },
  head: {
    height: 50,
    borderBottomColor: "#9ED228",
    borderBottomWidth: 1,
  },

  row: {
    height: 40,
    borderBottomColor: "#D6F3A1",
    borderBottomWidth: 1,
  },

  headText: {
    textAlign: "center",
    alignItems: "center",
    fontWeight: "400",
    fontSize: 14,
  },
  lastRow: {
    borderBottomWidth: 0,
  },
});
