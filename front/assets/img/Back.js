import * as React from "react";
import { View, TouchableOpacity } from "react-native";
import Svg, { Path } from "react-native-svg";

export default function BackImg({ style, onPress }) {
  const Wrapper = onPress ? TouchableOpacity : View;

  return (
    <Wrapper style={style} onPress={onPress} activeOpacity={0.7}>
      <Svg
        xmlns="http://www.w3.org/2000/svg"
        width={15}
        height={19}
        fill="none"
        viewBox="0 0 15 19"
      >
        <Path
          fill="#9ED228"
          d="M10.599 18.685c.518-.435.537-1.157.043-1.612L2.71 9.763a.348.348 0 0 1 0-.525l7.93-7.31c.495-.456.476-1.178-.042-1.613-.518-.434-1.338-.418-1.832.038l-7.93 7.31C-.28 8.691-.28 10.31.836 11.337l7.93 7.31c.494.456 1.314.472 1.832.038"
        />
      </Svg>
    </Wrapper>
  );
}
