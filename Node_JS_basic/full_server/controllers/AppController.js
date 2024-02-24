// full_server/controllers/AppController.js
export default class AppController {
  static getHomepage(req, res) {
    return res.status(200).send('Hello Holberton School!');
  }
}

module.export = AppController;
