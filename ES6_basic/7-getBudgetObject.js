Notice how the keys and the variable names are the same?

Modify the following function’s budget object to simply use the object property value shorthand syntax instead.

export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income: income,
    gdp: gdp,
    capita: capita,
  };

  return budget;
}