import React, { createContext, useState, useCallback } from "react";

export const NotificationContext = createContext();

export function NotificationProvider({ children }) {
  const [message, setMessage] = useState(null);

  const showMessage = useCallback((msg) => {
    setMessage(msg);

    setTimeout(() => setMessage(null), 3000);
  }, []);

  return (
    <NotificationContext.Provider value={{ message, showMessage }}>
      {children}
    </NotificationContext.Provider>
  );
}
