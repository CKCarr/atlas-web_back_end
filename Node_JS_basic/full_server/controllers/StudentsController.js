// full_server/controllers/StudentsController.js
const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const data = await readDatabase(process.argv[2]);
      response.writeHead(200, { 'Content-Type': 'text/plain' });
      response.write('This is the list of our students\n');

      const fields = Object.keys(data).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
      for (const field of fields) {
        response.write(`Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`);
      }

      response.end();
    } catch (error) {
      response.writeHead(500, { 'Content-Type': 'text/plain' });
      response.end(`Cannot load the database: ${error.message}`);
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.query;
    if (!major || (major !== 'CS' && major !== 'SWE')) {
      response.writeHead(500, { 'Content-Type': 'text/plain' });
      response.end('Major parameter must be CS or SWE');
      return;
    }

    try {
      const data = await readDatabase(process.argv[2]);
      response.writeHead(200, { 'Content-Type': 'text/plain' });

      if (!data[major]) {
        response.end(`No students in ${major}`);
        return;
      }

      response.end(`List: ${data[major].join(', ')}`);
    } catch (error) {
      response.writeHead(500, { 'Content-Type': 'text/plain' });
      response.end(`Cannot load the database: ${error.message}`);
    }
  }
}

module.exports = StudentsController;
