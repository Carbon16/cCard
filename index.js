const mariadb = require('mariadb');
const express = require('express');
const app = express();
const { spawn } = require('child_process');
const pyProg = spawn('python', ['uid.py']);


const pool = mariadb.createPool({
    host: 'localhost',
    user: 'root',
    password: 'Tritium1769',
    database: 'poker',
    connectionLimit: 5
});

pool.getConnection()
    .then(conn => {
        console.log('Connected to MariaDB');

        conn.query("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), uid INT, credit INT)")
            .then(() => {
                console.log("Table created or already exists");
            })
    }).catch(err => {
        console.log('Error connecting to MariaDB');
        pool.end();
});

app.get('/user', (req, res) => {
    pool.getConnection()
        .then(conn => {
            conn.query("SELECT * FROM users")
                .then(rows => {
                    res.send(rows);
                })
                .catch(err => {
                    res.send(err);
                })
                .finally(() => {
                    conn.release();
                });
        });
});

app.get('/user/:uid', (req, res) => {
    pool.getConnection()
        .then(conn => {
            conn.query("SELECT * FROM users WHERE uid = ?", [req.params.uid])
                .then(rows => {
                    res.send(rows);
                })
                .catch(err => {
                    res.send(err);
                })
                .finally(() => {
                    conn.release();
                });
        });
});

app.get('/scan', async (req, res) => {
    // scan the users card
    uid = await pyProg.stdout.on('data', function(data) {
        return data.toString();
    });
    console.log(uid)
    res.send(uid);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});