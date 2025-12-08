import React, { useState, useCallback, useEffect } from "react";
import { useFocusEffect } from "@react-navigation/native";
import {
  View,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from "react-native";
import { mainStyle } from "../style";
import FooterBloc from "../components/bloc/FooterBloc";
import CalendarUI from "../components/ui/CalendarUI.js";
import { SafeAreaView } from "react-native-safe-area-context";
import UserImg from "../assets/img/User.js";
import StatImg from "../assets/img/Stat.js";
import HomeStatisticBloc from "../components/bloc/HomeStatisticBloc.js";
import HomeLanchBloc from "../components/bloc/HomeLanchBloc.js";
// import { getToday } from "../utils/functions.js";
import { API } from "../api/api.js";
import { useContext } from "react";
import { NotificationContext } from "../store";
import SkeletonBlock from "../components/bloc/SkeletonBlock.js";
import { DateContext } from "../store";

export default function HomeView({ navigation }) {
  const [loading, setLoading] = useState(true);
  const [userData, setUserData] = useState(null);
  const [userStat, setUserStat] = useState(null);
  const { showMessage } = useContext(NotificationContext);
  const [loadingMain, setLoadingMain] = useState(true);
  const [loadingMeals, setLoadingMeals] = useState([true, true, true]);

  const [mealType, setMealType] = useState([null, null, null]);
  // const [loadingMeals, setLoadingMeals] = useState([false, false, false]);

  const { date, setDate } = useContext(DateContext);

  const loadUserData = async () => {
    setLoadingMain(true);

    try {
      const stat = await API.getDayStat(date);
      const norm = await API.getStatNorm();

      setUserStat(stat);
      setUserData(norm);
    } catch (err) {
      showMessage(err.response?.data?.message || "Ошибка загрузки");
    }

    setLoadingMain(false);
  };

  const loadMealProduct = async (id) => {
    const index = id - 1;

    setLoadingMeals((prev) => {
      const arr = [...prev];
      arr[index] = true;
      return arr;
    });

    try {
      const res = await API.getProductMeal(id, date);

      setMealType((prev) => {
        const updated = [...prev];
        updated[index] = res;
        return updated;
      });
    } catch (err) {
      showMessage(err.response?.data?.message || "Ошибка приема пищи");
    }

    setLoadingMeals((prev) => {
      const arr = [...prev];
      arr[index] = false;
      return arr;
    });
  };

  const loaderPostDelete = async (id) => {
    try {
      const stat = await API.getDayStat(date);

      setUserStat(stat);

      // console.log(1, stat);
      // console.log(2, norm);
    } catch (err) {
      const msg = err.response?.data?.message || "Ошибка загрузки";
      showMessage(msg);
      console.log("Ошибка загрузки:", err);
    }
  };

  const deleteMealTypeProduct = async (productId, mealId, id) => {
    try {
      await API.deleteProductMeal(productId, mealId);

      loaderPostDelete();

      loadMealProduct(id);
      // loadUserData();
    } catch (err) {
      const msg = err.response?.data?.message || "Ошибка удаления";
      showMessage(msg);
      console.log("Ошибка удаления:", err);
    }
  };

  useEffect(() => {
    loadUserData();

    setMealType([null, null, null]);

    loadMealProduct(1);
    loadMealProduct(2);
    loadMealProduct(3);
  }, [date]);

  useFocusEffect(
    useCallback(() => {
      loadUserData();

      loadMealProduct(1);
      loadMealProduct(2);
      loadMealProduct(3);
    }, [date])
  );

  // if (loading) {
  //   return (
  //     <View style={styles.loaderScreen}>
  //       <ActivityIndicator size="large" color="#9ED228" />
  //     </View>
  //   );
  // }

  return (
    <View style={{ height: "100%" }}>
      <ScrollView showsVerticalScrollIndicator={false}>
        <SafeAreaView style={mainStyle.main_bloc}>
          <View style={mainStyle.start_bloc}>
            <TouchableOpacity onPress={() => navigation.navigate("User")}>
              <UserImg width={36} height={36} />
            </TouchableOpacity>
            <TouchableOpacity onPress={() => navigation.navigate("User")}>
              <StatImg width={36} height={36} />
            </TouchableOpacity>
          </View>

          <CalendarUI
            selected={date}
            onSelect={(newDate) => setDate(newDate)}
          />

          <HomeStatisticBloc userData={userData} userStat={userStat} />
          <View style={{ marginTop: 20, gap: 10 }}>
            <HomeLanchBloc
              image={require("../assets/img/br.png")}
              title="Завтрак"
              onAdd={() =>
                navigation.navigate("Loading", { MealType: 1, date })
              }
              // onToggle={() => loadMealProduct(1)}
              onDelete={(id) =>
                deleteMealTypeProduct(id, mealType[0]?.[0]?.MealID, 1)
              }
              dropdownInfo={mealType[0]?.[0]?.Products ?? []}
              date={date}
              // loading={loadingMeals[0]}
            />

            <HomeLanchBloc
              image={require("../assets/img/ln.png")}
              title="Обед"
              onAdd={() =>
                navigation.navigate("Loading", { MealType: 2, date })
              }
              // onToggle={() => loadMealProduct(2)}
              onDelete={(id) =>
                deleteMealTypeProduct(id, mealType[1]?.[0]?.MealID, 2)
              }
              dropdownInfo={mealType[1]?.[0]?.Products ?? []}
              date={date}
              // loading={loadingMeals[1]}
            />

            <HomeLanchBloc
              image={require("../assets/img/dn.png")}
              title="Ужин"
              onAdd={() =>
                navigation.navigate("Loading", { MealType: 3, date })
              }
              // onToggle={() => loadMealProduct(3)}
              onDelete={(id) =>
                deleteMealTypeProduct(id, mealType[2]?.[0]?.MealID, 3)
              }
              dropdownInfo={mealType[2]?.[0]?.Products ?? []}
              date={date}
              // loading={loadingMeals[2]}
            />
          </View>
        </SafeAreaView>
      </ScrollView>

      <FooterBloc style={mainStyle.main_footer} navigation={navigation} />
    </View>
  );
}

const styles = StyleSheet.create({
  loaderScreen: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});
