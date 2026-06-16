import * as React from "react";
import Svg, { Path, Circle } from "react-native-svg";

const SvgIcon = (props) => (
  <Svg
    xmlns="http://www.w3.org/2000/svg"
    width="36"
    height="36"
    fill="none"
    viewBox="0 0 36 36"
  >
    <Circle cx="18.5" cy="17.5" r="16.5" fill="#fff"></Circle>
    <Path
      fill="#000"
      d="M18.36 18.6A9.36 9.36 0 0 0 9 27.96a.72.72 0 0 0 1.44 0 7.92 7.92 0 1 1 15.84 0 .72.72 0 0 0 1.44 0 9.36 9.36 0 0 0-9.36-9.36M18.36 17.375a5.04 5.04 0 0 0 4.903-5.184A5.04 5.04 0 0 0 18.36 7a5.04 5.04 0 0 0-4.904 5.191 5.04 5.04 0 0 0 4.904 5.184m0-8.935a3.6 3.6 0 0 1 3.463 3.751 3.6 3.6 0 0 1-3.463 3.744 3.6 3.6 0 0 1-3.464-3.744A3.6 3.6 0 0 1 18.36 8.44"
    ></Path>
  </Svg>
);

export default SvgIcon;
