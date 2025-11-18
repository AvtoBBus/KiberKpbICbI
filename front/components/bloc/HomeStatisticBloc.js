import { StyleSheet, Text, View } from "react-native";
import { mainStyle } from "../../style";
// import { VictoryPie } from "victory-native";
import DonutChartUI from "../ui/DonutChartUI";

export default function HomeStatisticBloc({ userData }) {
  // const { userData } = route.params ?? {};

  return (
    <View style={mainStyle.white_bloc}>
      <View style={[mainStyle.start_bloc, styles.stat_bloc]}>
        <View style={{ maxWidth: 180 }}>
          <Text style={[mainStyle.h1, styles.label]}>Статистика</Text>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>потреблено</Text>
            <Text style={[mainStyle.p, styles.p_table]}>
              {userData?.p ?? "1000"}
            </Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>осталось</Text>
            <Text style={[mainStyle.p, styles.p_table]}>
              {userData?.o ?? "1000"}
            </Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>всего</Text>
            <Text style={[mainStyle.p, styles.p_table]}>
              {userData?.v ?? "1000"}
            </Text>
          </View>
        </View>
        <View>
          <DonutChartUI
            percent={userData?.percent ?? 65}
            size={100}
            strokeWidth={12}
          />
        </View>
      </View>
      <View></View>
    </View>
  );
}

const styles = StyleSheet.create({
  infoRow: {
    flexDirection: "row",
    marginTop: 1,
    width: 200,
  },
  p_table: {
    flex: 1,
    fontSize: 14,
  },
  label: {
    marginBottom: 14,
    fontSize: 20,
    textAlign: "left",
  },
  stat_bloc: {
    // width: 390,
    // width: 334,
    // flexDirection: "row",
    justifyContent: "center",
    // alignItems: "flex-end",
    marginBottom: 0,
    marginTop: 0,
  },
});
