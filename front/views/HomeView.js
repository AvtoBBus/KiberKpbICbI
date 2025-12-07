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
import { getToday } from "../utils/functions.js";
import { API } from "../api/api.js";

export default function HomeView({ navigation }) {
  const [loading, setLoading] = useState(true);
  const [userData, setUserData] = useState(null);
  const [userStat, setUserStat] = useState(null);

  const [mealType, setMealType] = useState([null, null, null]);
  // const [loadingMeals, setLoadingMeals] = useState([false, false, false]);

  const [date, setDate] = useState(getToday());

  const loadUserData = async () => {
    setLoading(true);

    try {
      const stat = await API.getDayStat(date);
      const norm = await API.getStatNorm();

      setUserStat(stat);
      setUserData(norm);

      console.log(1, stat);
      console.log(2, norm);
    } catch (err) {
      console.log("Ошибка загрузки:", err);
    }

    setLoading(false);
  };

  const loadMealProduct = async (id) => {
    const index = id - 1;

    // if (mealType[index] !== null) return;

    // setLoadingMeals((prev) => {
    //   const updated = [...prev];
    //   updated[index] = true;
    //   return updated;
    // });

    try {
      console.log("приемы пищи");
      const res = await API.getProductMeal(id, date);

      setMealType((prev) => {
        const updated = [...prev];
        updated[index] = res;
        return updated;
      });

      // console.log("приемы пищи", res);
      // console.log("завтрак", mealType[0]);
      // console.log("обед", mealType[1]);
      // console.log("ужин", mealType[2]);
      // // console.log("завтрак п", mealType[0].Products);
      // // console.log("обед п", mealType[1].Products);
      // console.log("ужин п", mealType[2]).Products;
    } catch (err) {
      console.log("Ошибка загрузки приемы пищи:", err);
    }

    // setLoadingMeals((prev) => {
    //   const updated = [...prev];
    //   updated[index] = false;
    //   return updated;
    // });
  };

  const deleteMealTypeProduct = async (productId, mealId) => {
    const index = mealId - 1;

    // setLoadingMeals((prev) => {
    //   const updated = [...prev];
    //   updated[index] = true;
    //   return updated;
    // });

    try {
      await API.deleteProductMeal(productId, mealId);

      const res = await API.getProductMeal(mealId, date);

      setMealType((prev) => {
        const updated = [...prev];
        updated[index] = res;
        return updated;
      });
    } catch (err) {
      console.log("Ошибка удаления:", err);
    }

    // setLoadingMeals((prev) => {
    //   const updated = [...prev];
    //   updated[index] = false;
    //   return updated;
    // });
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

  if (loading) {
    return (
      <View style={styles.loaderScreen}>
        <ActivityIndicator size="large" color="#9ED228" />
      </View>
    );
  }

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
              onDelete={(id) => deleteMealTypeProduct(id, 1)}
              dropdownInfo={mealType[0]?.[0]?.Products ?? []}
              // loading={loadingMeals[0]}
            />

            <HomeLanchBloc
              image={require("../assets/img/ln.png")}
              title="Обед"
              onAdd={() =>
                navigation.navigate("Loading", { MealType: 2, date })
              }
              // onToggle={() => loadMealProduct(2)}
              onDelete={(id) => deleteMealTypeProduct(id, 2)}
              dropdownInfo={mealType[1]?.[0]?.Products ?? []}
              // loading={loadingMeals[1]}
            />

            <HomeLanchBloc
              image={require("../assets/img/dn.png")}
              title="Ужин"
              onAdd={() =>
                navigation.navigate("Loading", { MealType: 3, date })
              }
              // onToggle={() => loadMealProduct(3)}
              onDelete={(id) => deleteMealTypeProduct(id, 3)}
              dropdownInfo={mealType[2]?.[0]?.Products ?? []}
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
