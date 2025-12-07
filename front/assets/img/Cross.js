import * as React from "react";
import Svg, { Path } from "react-native-svg";

const CrossIcon = ({ width = 20, height = 20, color = "#000", ...props }) => (
  <Svg width={width} height={height} viewBox="0 0 24 24" {...props}>
    <Path
      fill="none"
      stroke={color}
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M19 19 5 5"
    />
    <Path
      fill="none"
      stroke={color}
      strokeLinecap="round"
      strokeLinejoin="round"
      strokeWidth={2}
      d="M19 5 5 19"
    />
  </Svg>
);

export default CrossIcon;
