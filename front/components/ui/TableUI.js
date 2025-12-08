import React from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  FlatList,
} from "react-native";
import CrossImg from "../../assets/img/Cross.js";

export default function TableUI({ data, onDelete }) {
  const tableHead = ["Имя", "Б", "Ж", "У", "Ккал", ""];

  const renderHeader = () => (
    <View style={styles.row}>
      {tableHead.map((col, i) => (
        <View
          key={`head-${i}`}
          style={[styles.cell, styles.headCell, styles.widths[i]]}
        >
          <Text style={styles.headText}>{col}</Text>
        </View>
      ))}
    </View>
  );

  const renderItem = ({ item, index }) => {
    const isLast = index === data.length - 1;

    return (
      <View style={[styles.row, !isLast && styles.rowBorder]}>
        <View style={[styles.cell, styles.widths[0]]}>
          <Text style={styles.cellText}>{item.ProductName}</Text>
        </View>

        <View style={[styles.cell, styles.widths[1]]}>
          <Text style={styles.cellText}>{item.Protein}</Text>
        </View>

        <View style={[styles.cell, styles.widths[2]]}>
          <Text style={styles.cellText}>{item.Fats}</Text>
        </View>

        <View style={[styles.cell, styles.widths[3]]}>
          <Text style={styles.cellText}>{item.Carbonates}</Text>
        </View>

        <View style={[styles.cell, styles.widths[4]]}>
          <Text style={styles.cellText}>{item.Calories}</Text>
        </View>

        <TouchableOpacity
          style={[styles.cell, styles.widths[5]]}
          onPress={() => onDelete(item.ProductID)}
        >
          <CrossImg width={20} height={20} color="#FFB6B7" />
        </TouchableOpacity>
      </View>
    );
  };

  return (
    <View style={styles.container}>
      {renderHeader()}

      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={(item) => item.ProductID.toString()}
        scrollEnabled={false}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 10,
  },

  row: {
    flexDirection: "row",
    alignItems: "center",
    height: 40,
  },

  rowBorder: {
    borderBottomColor: "#D6F3A1",
    borderBottomWidth: 1,
  },

  headCell: {
    borderBottomColor: "#9ED228",
    borderBottomWidth: 1,
    height: 50,
    justifyContent: "center",
  },

  cell: {
    justifyContent: "center",
    alignItems: "center",
  },

  headText: {
    textAlign: "center",
    fontWeight: "400",
    fontSize: 14,
  },

  cellText: {
    textAlign: "center",
    fontWeight: "300",
    fontSize: 14,
  },

  widths: [
    { width: 70 },
    { width: 40 },
    { width: 40 },
    { width: 40 },
    { width: 60 },
    { width: 40 },
  ],
});
