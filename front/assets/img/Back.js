import * as React from "react";
import Svg, { Path } from "react-native-svg";

const SvgIcon = (props) => (
  <Svg
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="24"
    fill="none"
    viewBox="0 0 24 24"
  >
    <Path
      fill="#000"
      d="M3 19h1V5H3zM21 11.5H8.921l5.793-5.792L14 5l-7 7 7 7 .713-.708L8.922 12.5H21z"
    ></Path>
  </Svg>
);

export default SvgIcon;
