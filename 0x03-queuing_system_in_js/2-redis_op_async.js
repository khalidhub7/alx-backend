import { createClient, print } from 'redis';
import { promisify } from 'util';

const conn = createClient();

conn.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

conn.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool (schoolName, value) {
  conn.set(schoolName, value, print);
}

const asyncget = promisify(conn.get).bind(conn);

function displaySchoolValue (schoolName) {
  asyncget(schoolName).then((value) => {
    console.log(value);
  }).catch((err) => {
    console.log(err.message);
  });
}

setNewSchool('Holberton', 'School');
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
