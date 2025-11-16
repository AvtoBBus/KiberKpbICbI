/**
 * Преобразует объект констант в массив опций для dropdown
 * @param {Object} obj — объект в формате { 0: "Текст", 1: "Текст", ... }
 * @returns {Array} — массив [{ value: number, label: string }]
 */
export const mapToOptions = (obj = {}) =>
  Object.keys(obj).map((key) => ({
    value: Number(key),
    label: obj[key],
  }));
