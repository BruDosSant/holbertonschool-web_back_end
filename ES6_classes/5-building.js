export default class Building {
    constructor(sqft) {
        if (typeof sqft !== 'number') {
            throw new TypeError('el area debe ser un numero');
        }
        this._sqft = sqft;

        if (this.constructor !== Building) {
            if (typeof this.evacuationWarningMessage !== 'function') {
                throw new TypeError('Debe implementar el metodo evacuationWarningMessage');
            }
        }
    }
    get sqft() {
        return this._sqft;
    }
}