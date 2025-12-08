import React, { useState, useRef, useEffect } from "react";
import {
  View,
  Text,
  Image,
  StyleSheet,
  TouchableOpacity,
  Animated,
} from "react-native";
import Addimg from "../../assets/img/Add.js";
import TableUI from "../ui/TableUI.js";

export default function HomeLanchBloc({
  title = "Завтрак",
  calories = "--",
  image,
  onAdd = () => {},
  onToggle = () => {},
  onDelete = () => {},
  dropdownInfo = [],
  date,
}) {
  const [open, setOpen] = useState(false);
  //   const [hasLoaded, setHasLoaded] = useState(false);

  const animatedHeight = useRef(new Animated.Value(0)).current;
  const contentHeight = useRef(0);

  useEffect(() => {
    setOpen(false);
    animatedHeight.setValue(0);
  }, [date]);

  const getCalories = (products) => {
    if (!Array.isArray(products)) return 0;

    return products.reduce((sum, item) => sum + (item.Calories || 0), 0);
  };

  const toggle = () => {
    const nextOpen = !open;
    setOpen(nextOpen);

    // if (nextOpen && !hasLoaded) {
    //   onToggle();
    //   setHasLoaded(true);
    // }

    const toValue = nextOpen ? contentHeight.current : 0;

    Animated.timing(animatedHeight, {
      toValue,
      duration: 300,
      useNativeDriver: false,
    }).start();
  };

  // useEffect(() => {
  //   if (open) {
  //     Animated.timing(animatedHeight, {
  //       toValue: contentHeight.current,
  //       duration: 200,
  //       useNativeDriver: false,
  //     }).start();
  //   }
  // }, [dropdownInfo]);

  return (
    <View style={styles.card}>
      <TouchableOpacity style={styles.row} onPress={toggle} activeOpacity={0.8}>
        <Image source={image} style={styles.avatar} />

        <View style={styles.textBlock}>
          <Text style={styles.title}>{title}</Text>
          <Text style={styles.calories}>
            <Text style={styles.green}>{getCalories(dropdownInfo)}</Text> ккал
          </Text>
        </View>

        <TouchableOpacity style={styles.addBtn} onPress={onAdd}>
          <Addimg width={40} height={40} />
        </TouchableOpacity>
      </TouchableOpacity>

      <Animated.View style={[styles.dropdown, { height: animatedHeight }]}>
        <View
          style={{ position: "absolute", top: 0, left: 0, right: 0 }}
          onLayout={(e) => {
            contentHeight.current = e.nativeEvent.layout.height;

            if (open) {
              animatedHeight.setValue(contentHeight.current);
            }
          }}
        >
          <TableUI data={dropdownInfo} onDelete={(id) => onDelete(id)} />
        </View>
      </Animated.View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: "#fff",
    borderRadius: 10,
    paddingLeft: 23,
    paddingRight: 23,
    paddingTop: 10,
    width: 334,
  },

  row: {
    flexDirection: "row",
    alignItems: "center",
  },

  avatar: {
    width: 60,
    height: 60,
    borderRadius: 60 / 2,
    marginRight: 10,
  },

  textBlock: {
    flex: 1,
  },

  title: {
    fontSize: 20,
    fontWeight: "400",
  },

  calories: {
    fontSize: 14,
    fontWeight: "300",
    marginTop: 4,
  },

  green: {
    color: "#9ED228",
  },

  addBtn: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: "#9ED228",
    justifyContent: "center",
    alignItems: "center",
  },

  addText: {
    color: "#fff",
    fontSize: 26,
    lineHeight: 26,
    fontWeight: "300",
  },

  dropdown: {
    overflow: "hidden",
    marginTop: 10,
    borderRadius: 10,
    paddingHorizontal: 10,
  },
});
