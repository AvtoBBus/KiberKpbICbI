export const mapToOptions = (obj = {}) =>
  Object.keys(obj).map((key) => ({
    value: isNaN(Number(key)) ? key : Number(key),
    label: obj[key],
  }));
