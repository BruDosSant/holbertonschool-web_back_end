const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
    const lineas = data.split('\n').filter((linea) => linea.trim() !== '');
    lineas.shift();

    const StudentsByField = {};
    let AllStudents = 0;

    lineas.forEach((linea) => {
      const StudentData = linea.split(',');
      if (StudentData.length >= 4) {
        const FirstName = StudentData[0];
        const Field = StudentData[3];

        if (!StudentsByField[Field]) StudentsByField[Field] = [];
        StudentsByField[Field].push(FirstName);
        AllStudents += 1;
      }
    });

    console.log(`Number of students: ${AllStudents}`);
    let result = `Number of students: ${AllStudents}`;
    Object.entries(StudentsByField).forEach(([field, list]) => {
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      result += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
    });
    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
