const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  let responseText = 'This is the list of our students\n';

  try {
    const studentsReport = await countStudents(database);
    responseText += studentsReport;
    res.status(200).send(responseText);
  } catch (err) {
    res.status(200).send(`${responseText}${err.message}`);
  }
});

app.listen(1245);

module.exports = app;
