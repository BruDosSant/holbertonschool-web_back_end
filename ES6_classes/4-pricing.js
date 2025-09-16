import Currency from "./3-currency";
export default class Pricing {
    constructor(amount, currency) {
        if (typeof amount !== 'number') {
            throw new TypeError('el monto debe ser un numero');
        }
        this._amount = amount;

        if (!(currency instanceof Currency)) {
            throw new TypeError('la moneda debe ser una instancia de la clase Currency');
        }
        this._currency = currency;
    }
    get amount() {
        return this._amount;
    }
    set amount(newAmount) {
        if (typeof newAmount !== 'number') {
            throw new TypeError('el monto debe ser un numero');
        }
        this._amount = newAmount;
    }
    get currency() {
        return this._currency;
    }
    set currency(newCurrency) {
        if (!(newCurrency instanceof Currency)) {
            throw new TypeError('la moneda debe ser una instancia de la clase Currency');
        }
        this._currency = newCurrency;
    }
    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this.currency.code})`;
    }
    static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
