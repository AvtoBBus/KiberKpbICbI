import * as React from "react";
import Svg, { Path, Circle } from "react-native-svg";

const SvgIcon = (props) => (
  <Svg
    xmlns="http://www.w3.org/2000/svg"
    width="40"
    height="40"
    fill="none"
    viewBox="0 0 40 40"
  >
    <Circle cx="20" cy="20" r="20" fill="#9ED228"></Circle>
    <Path
      stroke="#F6F6F6"
      strokeLinecap="round"
      strokeWidth="3"
      d="M20 12.8v14.4M27.2 20H12.8"
    ></Path>
  </Svg>
);

export default SvgIcon;
