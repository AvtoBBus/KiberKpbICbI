import React from 'react';
import Router from './router';
import { LogBox } from 'react-native';

// Показать все предупреждения
LogBox.ignoreAllLogs(false);

export default function App() {
  // Обработчик ошибок
  if (typeof ErrorUtils !== 'undefined') {
    ErrorUtils.setGlobalHandler((error, isFatal) => {
      console.error('Глобальная ошибка:', error);
    });
  }
  return <Router />;
}