import React, { useState, useEffect, useContext } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import {
  View,
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  ActivityIndicator,
} from "react-native";
import { NotificationContext } from "../store";
import { API } from "../api/api.js";
import BarChartUI from "../components/ui/BarChartUI";
import PeriodToggle from "../components/ui/PeriodToggleUI.js";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc.js";
import BackImg from "../assets/img/Back.js";
import LineChartUI from "../components/ui/LineChartUI.js";

export default function StatisticView({ route, navigation }) {
  const { showMessage } = useContext(NotificationContext);
  const [userStat, setUserStat] = useState([]);
  const [period, setPeriod] = useState("week"); // ← выбранный период
  const [loading, setLoading] = useState(true);

  const { totalStat } = route.params ?? {};

  // === Генерация диапазона дат по периоду ===
  const getRange = () => {
    const today = new Date();
    const to = today.toISOString().split("T")[0];

    const fromDate = new Date(today);

    if (period === "week") {
      fromDate.setDate(today.getDate() - 6);
    } else if (period === "month") {
      fromDate.setMonth(today.getMonth() - 1);
    } else if (period === "year") {
      fromDate.setMonth(today.getMonth() - 2);
    }

    const from = fromDate.toISOString().split("T")[0];
    return { from, to };
  };

  const formatGraphData = (stats, key) => {
    return stats.map((item) => {
      const date = new Date(item.Date);

      // красивый label для графиков
      const label =
        date.getDate().toString().padStart(2, "0") +
        "." +
        (date.getMonth() + 1).toString().padStart(2, "0");

      // приводим значение к безопасному числу
      const raw = Number(item[key]);
      const value = isFinite(raw) ? raw : 0;

      return {
        value,
        label,
        rawDate: item.Date, // обязательно сохраняем оригинальную дату
        dateObj: date, // удобно для расчетов в LineChart
        frontColor: "#9ED228",
      };
    });
  };

  // === Загрузка статистики ===
  const loadStats = async () => {
    setLoading(true);
    const range = getRange();

    try {
      const stat = await API.getStatistic(range.from, range.to);
      setUserStat(stat);
      // console.log(stat);
    } catch (err) {
      showMessage(
        err.response?.data?.detail?.message || "Ошибка загрузки статистики"
      );
    }
    setLoading(false);
  };

  // подгрузка при смене периода
  useEffect(() => {
    loadStats();
  }, [period]);

  const caloriesData = formatGraphData(userStat, "Calories");
  const proteinData = formatGraphData(userStat, "Protein");
  const fatsData = formatGraphData(userStat, "Fats");
  const carbsData = formatGraphData(userStat, "Carbonates");

  if (loading) {
    return (
      <View style={mainStyle.loaderScreen}>
        <ActivityIndicator size="large" color="#9ED228" />
      </View>
    );
  }

  return (
    <View style={{ height: "100%" }}>
      <ScrollView showsVerticalScrollIndicator={false}>
        <SafeAreaView style={mainStyle.main_bloc}>
          <View style={mainStyle.start_bloc}>
            <TouchableOpacity onPress={() => navigation.goBack()}>
              <BackImg width={30} height={30} />
            </TouchableOpacity>

            <Text style={mainStyle.h1}>Статистика</Text>
          </View>
          <View style={mainStyle.start_bloc}>
            <PeriodToggle period={period} onChange={setPeriod} />
          </View>

          <View style={styles.bloc_stat}>
            <View style={[mainStyle.white_bloc, { alignItems: "flex-start" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Килокалории</Text>
              <BarChartUI
                data={caloriesData}
                goalValue={Math.round(totalStat?.Calories) ?? "0"}
              />
            </View>

            <View style={[mainStyle.white_bloc, { alignItems: "flex-start" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Белки</Text>
              <BarChartUI
                data={proteinData}
                goalValue={Math.round(totalStat?.Protein) ?? "0"}
              />
            </View>

            <View style={[mainStyle.white_bloc, { alignItems: "flex-start" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Углеводы</Text>
              <BarChartUI
                data={carbsData}
                goalValue={Math.round(totalStat?.Carbonatest) ?? "0"}
              />
            </View>

            <View style={[mainStyle.white_bloc, { alignItems: "flex-start" }]}>
              <Text style={[mainStyle.h1, styles.label]}>Жиры</Text>
              <BarChartUI
                data={fatsData}
                goalValue={Math.round(totalStat?.Fats) ?? "0"}
              />
            </View>
          </View>
        </SafeAreaView>
      </ScrollView>

      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({
  bloc_stat: {
    gap: 10,
  },
  label: {
    textAlign: "left",
  },
});
