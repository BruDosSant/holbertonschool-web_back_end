const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');
  if (lines.length === 0) {
    console.log('Number of students: 0');
    return;
  }


  const studentsByField = {};

  for (let i = 1; i < lines.length; i += 1) {
    const row = lines[i].split(',');
    if (row.length >= 4) {
      const firstName = row[0].trim();
      const field = row[3].trim();
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstName);
    }
  }

  const total = Object.values(studentsByField).reduce(
    (acc, arr) => acc + arr.length,
    0
  );
  console.log(`Number of students: ${total}`);

  for (const field in studentsByField) {
    if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
      const list = studentsByField[field].join(', ');
      console.log(
        `Number of students in ${field}: ${studentsByField[field].length}. List: ${list}`
      );
    }
  }
}

module.exports = countStudents;
