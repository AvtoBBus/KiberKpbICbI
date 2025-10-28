import { StyleSheet } from "react-native";

export const mainStyle = StyleSheet.create({
  h1: {
    // fontFamily: "regular",
    fontSize: 24,
    // lineHeight: "110%",
    color: "black",
    textAlign: "center",
  },
  p_input: {
    // fontFamily: "regular",
    fontSize: 16,
    // lineHeight: "120%",
    color: "black",
    textAlign: "left",
    textAlignVertical: "center",
  },
  p_light: {
    fontWeight: 300,
    fontSize: 12,
    // lineHeight: "125%",
    textAlign: "left",
    textAlignVertical: "center",
  },
  whiteCard: {
    backgroundColor: "white",
    height: "100%",
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    borderBottomLeftRadius: 0,
    borderBottomRightRadius: 0,
    flexDirection: "column",
    justifyContent: "center",
    paddingLeft: 20,
    paddingRight: 20,
  },
  inputContainer: {
    width: "100%",
    borderWidth: 1,
    borderColor: "#A5D66D",
    borderRadius: 10,
    paddingHorizontal: 20,
    flexDirection: "row",
    alignItems: "center",
  },
  inputContainerFocus: {
    borderColor: "#F7B31F",
  },
});
