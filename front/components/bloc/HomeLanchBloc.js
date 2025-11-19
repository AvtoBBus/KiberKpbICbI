import React, { useState } from "react";
import {
  View,
  Text,
  Image,
  StyleSheet,
  TouchableOpacity,
  Animated,
} from "react-native";
import Addimg from "../../assets/img/Add.js";

export default function HomeLanchBloc({
  title = "Завтрак",
  calories = "--",
  image,
  onAdd = () => {},
  dropdownText = "Дописать когда будет готов запрос",
}) {
  const [open, setOpen] = useState(false);
  const animatedHeight = useState(new Animated.Value(0))[0];

  const toggle = () => {
    const toValue = open ? 0 : 1;
    setOpen(!open);

    Animated.timing(animatedHeight, {
      toValue,
      duration: 300,
      useNativeDriver: false,
    }).start();
  };

  const dropdownHeight = animatedHeight.interpolate({
    inputRange: [0, 1],
    outputRange: [0, 70],
  });

  return (
    <View style={styles.card}>
      <TouchableOpacity style={styles.row} onPress={toggle} activeOpacity={0.8}>
        {/* Картинка */}
        <Image source={image} style={styles.avatar} />

        {/* Текст */}
        <View style={styles.textBlock}>
          <Text style={styles.title}>{title}</Text>
          <Text style={styles.calories}>
            <Text style={styles.green}>{calories}</Text> ккал
          </Text>
        </View>

        {/* Кнопка + */}
        <TouchableOpacity style={styles.addBtn} onPress={onAdd}>
          <Addimg width={40} height={40} />
        </TouchableOpacity>
      </TouchableOpacity>

      {/* Dropdown */}
      <Animated.View style={[styles.dropdown, { height: dropdownHeight }]}>
        <Text style={styles.dropdownText}>{dropdownText}</Text>
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
    backgroundColor: "#F8F8F8",
    marginTop: 10,
    borderRadius: 10,
    paddingHorizontal: 10,
  },

  dropdownText: {
    fontSize: 14,
    paddingTop: 10,
    color: "#444",
  },
});
