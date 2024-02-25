// models/makeup.model.js
import pool from '../config/db.connect';

class MakeupModel {
    constructor(connection) {
      this.connection = connection;
    }
  
    getAllMakeup() {
      return new Promise((resolve, reject) => {
        const query = 'SELECT * FROM makeup';
        this.connection.query(query, (err, results) => {
          if (err) {
            reject(err);
          } else {
            resolve(results);
          }
        });
      });
    }
  }
  
  module.exports = MakeupModel;
  