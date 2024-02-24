// full_server/controllers/StudentsController.js
const readDatabase = require('../utils');

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const studentsByField = await readDatabase('./databse.csv');
      let response = 'This is the list of our students\n';
      for (const [field, names] of Object.entries(studentsByField).sort()) {
        response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }
      return res.status(200).send(response.trim());
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const { major } = req.params;
      if (!['CS', 'SWE'].includes(major)) {
        return res.status(500).send('Major parameter must be CS or SWE');
      }
      const studentsByField = await readDatabase(process.argv[2]);
      const names = studentsByField[major] || [];
      return res.status(200).send(`List: ${names.join(', ')}`);
    } catch (error) {
      return res.status(500).send('Cannot load the database');
    }
  }
}

module.export = StudentsController;
