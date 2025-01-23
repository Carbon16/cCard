//run uid.py as a child process and get the output and display it in the console
const { spawn } = require('child_process');
const pyProg = spawn('python', ['uid.py']);

pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
});

pyProg.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
});