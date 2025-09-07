process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.setEncoding('utf8');

process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name) process.stdout.write(`Your name is: ${name.trim()}\r`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
