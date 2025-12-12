import React from "react";
import { View } from "react-native";
import { LineChart } from "react-native-chart-kit";

// Месяцы — короткие подписи
const MONTH_LABELS = [
  "Янв",
  "Фев",
  "Мар",
  "Апр",
  "Май",
  "Июн",
  "Июл",
  "Авг",
  "Сен",
  "Окт",
  "Ноя",
  "Дек",
];

export default function LineChartUI({ data = [], goalValue = null }) {
  const values = data.map((d) => Number(d.value) || 0);

  // безопасное значение цели
  const safeGoal = Number(goalValue);
  const validGoal = isFinite(safeGoal) ? safeGoal : null;

  // Для нормальной работы нам НУЖНО получить реальные даты
  // Предполагаю что в d есть d.rawDate — если нет, подставь item.Date туда.
  const dates = data.map((d) => new Date(d.rawDate || d.date || d.Date));

  const count = data.length;

  // --- Выбор режима ---
  let mode = "custom";

  if (count === 7) mode = "week";
  else if (count >= 28 && count <= 31) mode = "month";
  else if (count === 365 || count === 366) mode = "year";

  let labels = [];

  // ---- WEEK: показываем все 7 подписей ----
  if (mode === "week") {
    labels = data.map((d) => d.label);
  }

  // ---- MONTH: показываем 5 подписей ----
  else if (mode === "month") {
    const labelCount = 5;
    const step = Math.floor(count / labelCount);

    labels = data.map((d, i) => (i % step === 0 ? d.label : ""));
  }

  // ---- YEAR: показываем имена месяцев ----
  else if (mode === "year") {
    // массив из 12 месяцев
    const monthMap = new Array(12).fill("");

    dates.forEach((date) => {
      const m = date.getMonth();
      monthMap[m] = MONTH_LABELS[m];
    });

    labels = monthMap;
  }

  // ---- CUSTOM fallback ----
  else {
    const labelCount = Math.min(count, 7);
    const step = Math.floor(count / labelCount);

    labels = data.map((d, i) => (i % step === 0 ? d.label : ""));
  }

  return (
    <View style={{ marginTop: 10, width: 300, overflow: "hidden" }}>
      <LineChart
        data={{
          labels,
          datasets: [
            {
              data: values,
              color: () => "#4E9FFF",
              strokeWidth: 2,
            },
            ...(validGoal !== null
              ? [
                  {
                    data: values.map(() => validGoal),
                    color: () => "#9ED228",
                    strokeWidth: 1,
                  },
                ]
              : []),
          ],
        }}
        width={350}
        height={200}
        withDots={false}
        withInnerLines={true}
        withOuterLines={true}
        // =====✨ Анимация ✨=====
        fromZero={true}
        animationDuration={1200}
        chartConfig={{
          backgroundGradientFrom: "#fff",
          backgroundGradientTo: "#fff",
          decimalPlaces: 0,
          labelColor: () => "#333",
          color: () => "#4E9FFF",
          propsForLabels: {
            fontSize: 8,
          },
          propsForBackgroundLines: {
            strokeWidth: 0,
          },
        }}
        bezier
        style={{
          borderRadius: 8,
          marginRight: 0,
          marginLeft: -30,
        }}
      />
    </View>
  );
}
