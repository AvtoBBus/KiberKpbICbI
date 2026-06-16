import React, { useState, useEffect } from "react";
import {
  View,
  Image,
  TouchableOpacity,
  StyleSheet,
  Alert,
  Text,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import * as ImagePicker from "expo-image-picker";
import { mainStyle } from "../style";

export default function LoadingView({ navigation }) {
  const [image, setImage] = useState(null);

  useEffect(() => {
    (async () => {
      const cameraPermission =
        await ImagePicker.requestCameraPermissionsAsync();
      const mediaPermission =
        await ImagePicker.requestMediaLibraryPermissionsAsync();

      if (
        cameraPermission.status !== "granted" ||
        mediaPermission.status !== "granted"
      ) {
        Alert.alert(
          "Ошибка",
          "Разрешите доступ к камере и фото, чтобы продолжить"
        );
        return;
      }

      const result = await ImagePicker.launchCameraAsync({
        allowsEditing: true,
        aspect: [4, 4],
        quality: 1,
      });

      if (!result.canceled) {
        setImage(result.assets[0].uri);
      }
    })();
  }, []);

  const takePhoto = async () => {
    const result = await ImagePicker.launchCameraAsync({
      allowsEditing: true,
      aspect: [4, 4],
      quality: 1,
    });
    if (!result.canceled) {
      setImage(result.assets[0].uri);
    }
  };

  const pickImage = async () => {
    const result = await ImagePicker.launchImageLibraryAsync({
      allowsEditing: true,
      aspect: [4, 4],
      quality: 1,
    });
    if (!result.canceled) {
      setImage(result.assets[0].uri);
    }
  };

  return (
    <View style={styles.container}>
      {/* Фото или пустое место */}
      <View style={styles.preview}>
        {image ? (
          <Image source={{ uri: image }} style={styles.image} />
        ) : (
          <View style={styles.placeholder} />
        )}

        {/* Кнопка закрытия */}
        {image && (
          <TouchableOpacity
            style={styles.closeBtn}
            onPress={() => setImage(null)}
          >
            <Ionicons name="close" size={22} color="#fff" />
          </TouchableOpacity>
        )}
      </View>

      {/* Нижняя панель */}
      <View style={styles.bottomBar}>
        <TouchableOpacity onPress={pickImage}>
          <Ionicons name="images-outline" size={36} color="#fff" />
        </TouchableOpacity>

        <TouchableOpacity onPress={takePhoto}>
          <Ionicons name="radio-button-on-outline" size={64} color="#fff" />
        </TouchableOpacity>

        <TouchableOpacity onPress={() => navigation.navigate("Result")}>
          <Ionicons name="checkmark" size={42} color="#fff" />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#111",
    justifyContent: "center",
    alignItems: "center",
  },
  preview: {
    flex: 1,
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
    position: "relative",
  },
  placeholder: {
    width: "100%",
    height: "100%",
    backgroundColor: "#222",
  },
  image: {
    width: "100%",
    height: "100%",
    resizeMode: "cover",
  },
  closeBtn: {
    position: "absolute",
    top: 50,
    right: 30,
    backgroundColor: "rgba(0,0,0,0.5)",
    borderRadius: 20,
    padding: 6,
  },
  frame: {
    position: "absolute",
    width: 250,
    height: 250,
    borderWidth: 5,
    borderColor: "#fff",
    borderRadius: 20,
  },
  bottomBar: {
    width: "100%",
    height: 120,
    backgroundColor: "rgba(0,0,0,0.3)",
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
  },
});
