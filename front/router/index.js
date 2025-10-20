import React from "react";
import HomeView from "../views/HomeView";
import AuthorizationView from "../views/AuthorizationView";
import LoadingView from "../views/LoadingView";
import RegistrationView from "../views/RegistrationView";
import ResultView from "../views/ResultView";
import StatisticView from "../views/StatisticView";
import UserView from "../views/UserView";

import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

const Stack = createStackNavigator();

export default function Router() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeView} />
        <Stack.Screen name="Authorization" component={AuthorizationView} />
        <Stack.Screen name="Loading" component={LoadingView} />
        <Stack.Screen name="Registration" component={RegistrationView} />
        <Stack.Screen name="Result" component={ResultView} />
        <Stack.Screen name="Statistic" component={StatisticView} />
        <Stack.Screen name="User" component={UserView} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
