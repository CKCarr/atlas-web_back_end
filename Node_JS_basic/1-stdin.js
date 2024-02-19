/**
 * 1. Using Process stdin

Create a program named 1-stdin.js that will be executed through command line:

It should display the message Welcome to Holberton School,
what is your name? (followed by a new line)
The user should be able to input their name on a new line
The program should display Your name is: INPUT
When the user ends the program,
it should display
This important software is now closing (followed by a new line)

Requirements:

Your code will be tested through a child process,
make sure you have everything you need for that
 */
// Display the welcome message
process.stdout.write('Welcome to Holberton School, what is your name?\n');
// listen for data from standard input
process.stdin.on('data', (data) => {
  // data is a buffer object that needs to be converted to string
  const name = data.toString().trim();
  process.stdout.write(`Your name is: ${name}\n`);
  // after the user input, the process should exit
  process.exit();
});

// Listen for the 'exit' event to display a closing message
process.on('exit', () => {
  console.log('This important software is now closing\n');
});
