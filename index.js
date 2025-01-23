//run uid.py as a child process and get the output and display it in the console
// connect to maraiDB and insert the data into the database
const express = require('express');
const { spawn } = require('child_process');
const pyProg = spawn('python', ['uid.py']);
const maraiDB = require('mariadb');
//connect to db
const connection = maraiDB.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Tritium1769',
    database: 'poker'
});

const app = express();

//if table does not exist create it
connection.connect(function(err) {
    if (err) throw err;
    console.log('Connected!');
    var sql = "CREATE TABLE IF NOT EXISTS users (name VARCHAR(255) AUTO_INCREMENT PRIMARY KEY, uid INT, credit INT)";
    connection.query(sql, function(err, result) {
        if (err) throw err;
        console.log("Table created");
    });
    var sql = "CREATE TABLE IF NOT EXISTS transaction (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), credit INT, sign CHAR(1), date TIMESTAMP)";
    connection.query(sql, function(err, result) {
        if (err) throw err;
        console.log("Table created");
    });
});

pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
});

app.get('/register/:name', (req, res) => {
    //insert into users (name, uid, credit) values ('name', uid, 0)
    //get uid from python script
    uid = pyProg.stdout.on('data', function(data) {
        return data.toString();
    });
    var sql = `INSERT INTO users (name, uid, credit) VALUES ('${req.params.name}', ${uid}, 350)`;
    connection.query(sql, function(err, result) {
        if (err) throw err;
        console.log(`${req.params.name} inserted`);
    });
    res.sendStatus(201);
});

app.get('/read', (req, res) => {
    //get uid from python script and return a user with that uid
    uid = pyProg.stdout.on('data', function(data) {
        return data.toString();
    });
    var sql = `SELECT * FROM users WHERE uid = ${uid}`;
    connection.query(sql, function(err, result) {
        if (err) throw err;
        console.log(result);
    });
    res.send(result);
});