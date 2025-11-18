import * as React from "react";
import Svg, { Path } from "react-native-svg";

const SvgIcon = (props) => (
  <Svg
    xmlns="http://www.w3.org/2000/svg"
    width="42"
    height="42"
    fill="none"
    viewBox="0 0 42 42"
  >
    <Path
      stroke="#fff"
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth="2"
      d="M3.5 15.75v-4.375A7.864 7.864 0 0 1 11.375 3.5h4.375M26.25 3.5h4.375a7.864 7.864 0 0 1 7.875 7.875v4.375M38.5 28v2.625a7.864 7.864 0 0 1-7.875 7.875H28M15.75 38.5h-4.375A7.864 7.864 0 0 1 3.5 30.625V26.25M29.75 16.625v8.75q0 5.25-5.25 5.25h-7q-5.25 0-5.25-5.25v-8.75q0-5.25 5.25-5.25h7q5.25 0 5.25 5.25M33.25 21H8.75"
    ></Path>
  </Svg>
);

export default SvgIcon;
