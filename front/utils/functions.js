export const mapToOptions = (obj = {}) =>
  Object.keys(obj).map((key) => ({
    value: isNaN(Number(key)) ? key : Number(key),
    label: obj[key],
  }));

export function summarizeDayStats(list = []) {
  return list.reduce(
    (acc, item) => {
      acc.Calories += item.Calories || 0;
      acc.Protein += item.Protein || 0;
      acc.Fats += item.Fat || 0;
      acc.Carbonatest += item.Carbonates || 0;
      return acc;
    },
    { Calories: 0, Protein: 0, Fats: 0, Carbonatest: 0 }
  );
}

export function getToday() {
  const d = new Date();
  const day = String(d.getDate()).padStart(2, "0");
  const month = String(d.getMonth() + 1).padStart(2, "0");
  const year = d.getFullYear();
  return `${year}-${month}-${day}`;
}
