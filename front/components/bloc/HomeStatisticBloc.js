import { StyleSheet, Text, View } from "react-native";
import { mainStyle } from "../../style";
import DonutChartUI from "../ui/DonutChartUI";
import ProgressBarUI from "../ui/ProgressBarUI";

export default function HomeStatisticBloc({ userData, userStat }) {
  // const { userData } = route.params ?? {};
  const procent = userData?.Calories
    ? ((userStat?.Calories ?? 0) * 100) / userData.Calories
    : 0;

  const mod =
    userData?.Calories && userStat?.Calories
      ? userData.Calories - userStat.Calories
      : "--";

  return (
    <View style={mainStyle.white_bloc}>
      <View style={[mainStyle.start_bloc, styles.stat_bloc]}>
        <View style={{ maxWidth: 180 }}>
          <Text style={[mainStyle.h1, styles.label]}>Статистика</Text>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>потреблено</Text>
            <Text style={[mainStyle.p, styles.p_table]}>
              {userStat?.Calories ?? "--"}
            </Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>осталось</Text>
            <Text style={[mainStyle.p, styles.p_table]}>{mod}</Text>
          </View>
          <View style={styles.infoRow}>
            <Text style={[mainStyle.p, styles.p_table]}>всего</Text>
            <Text style={[mainStyle.p, styles.p_table]}>
              {userData?.Calories ?? "--"}
            </Text>
          </View>
        </View>
        <View>
          <DonutChartUI percent={procent} size={100} strokeWidth={12} />
        </View>
      </View>
      <View style={styles.bar_flex}>
        <ProgressBarUI
          style={styles.bar_width}
          title="белки"
          current={userStat?.Protein ?? 0}
          total={userData?.Protein ?? 0}
          color="#9ED228"
          bgColor="#E6F5C4"
        />
        <ProgressBarUI
          style={styles.bar_width}
          title="жиры"
          current={userStat?.Fats ?? 0}
          total={userData?.Fats ?? 0}
          color="#F7B31F"
          bgColor="#F9E5B8"
        />
        <ProgressBarUI
          style={styles.bar_width}
          title="углеводы"
          current={userStat?.Carbonatest ?? 0}
          total={userData?.Carbonatest ?? 0}
          color="#40C2FF"
          bgColor="#B6E8FF"
        />
      </View>
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
    justifyContent: "center",
    marginBottom: 0,
    marginTop: 0,
  },
  bar_flex: {
    flexDirection: "row",
    gap: 30,
  },
  bar_width: {
    width: 74,
  },
});
