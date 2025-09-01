export default function cleanSet(set, startString) {
  if (!startString) return ''; // Maneja undefined o ''
  return [...set]
    .filter(val => val.startsWith(startString))
    .map(val => val.slice(startString.length))
    .join('-');
}
