// front/router/index.js
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

// Импорты экранов
import AuthorizationView from "../views/AuthorizationView";
import RegistrationView from "../views/RegistrationView";
import HomeView from "../views/HomeView";
import UserView from "../views/UserView";
import EditUserView from "../views/EditUserView";
import StatisticView from "../views/StatisticView";
import ResultView from "../views/ResultView";
import LoadingView from "../views/LoadingView";

const Stack = createStackNavigator();

export default function Router() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Authorization"
        screenOptions={{
          headerShown: false,
        }}
      >
        <Stack.Screen name="Authorization" component={AuthorizationView} />
        <Stack.Screen name="Registration" component={RegistrationView} />
        <Stack.Screen name="Home" component={HomeView} />
        <Stack.Screen name="User" component={UserView} />
        <Stack.Screen name="EditUser" component={EditUserView} />
        <Stack.Screen name="Statistic" component={StatisticView} />
        <Stack.Screen name="Result" component={ResultView} />
        <Stack.Screen name="Loading" component={LoadingView} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}