import React, { createContext, useState, useCallback } from "react";
import { getToday } from "../utils/functions.js";

export const NotificationContext = createContext();

export function NotificationProvider({ children }) {
  const [messages, setMessages] = useState([]);

  const showMessage = useCallback((text) => {
    const id = crypto.randomUUID();

    setMessages((prev) => {
      let updated = [...prev, { id, text }];

      if (updated.length > 20) {
        updated = updated.slice(updated.length - 20);
      }

      return updated;
    });
  }, []);

  const removeMessage = (id) => {
    setMessages((prev) => prev.filter((m) => m.id !== id));
  };

  return (
    <NotificationContext.Provider
      value={{ messages, showMessage, removeMessage }}
    >
      {children}
    </NotificationContext.Provider>
  );
}

export const DateContext = createContext();

export function DateProvider({ children }) {
  const [date, setDate] = useState(getToday());

  return (
    <DateContext.Provider value={{ date, setDate }}>
      {children}
    </DateContext.Provider>
  );
}
