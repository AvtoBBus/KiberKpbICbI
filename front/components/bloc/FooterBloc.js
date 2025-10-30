import { StyleSheet, TouchableOpacity, View } from "react-native";
import PhotoImg from "../../assets/img/photo.svg";
import { SafeAreaView } from "react-native-safe-area-context";

export default function FooterBloc({ navigation }) {
  return (
    <View style={styles.footer}>
      <TouchableOpacity onPress={() => navigation.navigate("Loading")}>
        <View style={styles.footerButton}>
          <PhotoImg width={42} height={42} />
        </View>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  footer: {
    backgroundColor: "white",
    height: 70,
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    width: "100%",
    position: "relative",
  },

  footerButton: {
    justifyContent: "center",
    alignItems: "center",
    width: 61,
    height: 61,
    borderRadius: 61 / 2,
    backgroundColor: "#9ED228",
    position: "absolute",
    top: -50,
    alignSelf: "center",
  },
});
