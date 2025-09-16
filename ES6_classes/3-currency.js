export default class Currency {
    constructor(code, name) {
        if (typeof name !== 'string' || typeof code !== 'string') {
            throw new TypeError('el nombre y el codigo deben ser un string');
        }
        this._name = name;
        this._code = code;
    }
    get name() {
        return this._name;
    }
    set name(newName) {
        if (typeof newName !== 'string') {
            throw new TypeError('el nombre debe ser un string');
        }
        this._name = newName;
    }
    get code() {
        return this._code;
    }
    set code(newcode) {
        if (typeof newcode !== 'string') {
            throw new TypeError('el nombre debe ser un string');
        }
        this._code = newcode;
    }
    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}