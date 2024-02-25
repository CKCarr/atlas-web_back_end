// full_server/controllers/StudentsController.js
const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((data) => {
        response.status(200).send(`This is the list of our students
Number of students in CS: ${data.CS.length}. List: ${data.CS.join(', ')}
Number of students in SWE: ${data.SWE.length}. List: ${data.SWE.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    readDatabase(process.argv[2])
      .then((data) => {
        if (request.params.major === 'CS') {
          response.status(200).send(`List: ${data.CS.join(', ')}`);
        } else if (request.params.major === 'SWE') {
          response.status(200).send(`List: ${data.SWE.join(', ')}`);
        } else {
          response.status(500).send('Major parameter must be CS or SWE');
        }
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
