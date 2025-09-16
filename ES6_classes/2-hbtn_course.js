export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof name !== 'string') {
            throw new TypeError('el nombre debe ser un string');
        }
        this._name = name;
        if  (typeof length !== 'number') {
            throw new TypeError('la duracion debe ser un numero');
        }
        this._length = length;
        if (Array.isArray(students) == false || !students.every(messi => typeof messi === 'string')) {
            throw new TypeError('los estudiantes deben conformar un array');
        }
        this._students = students;
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
}