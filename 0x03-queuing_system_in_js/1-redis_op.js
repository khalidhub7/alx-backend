import { createClient, print } from 'redis';

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

function displaySchoolValue (schoolName) {
  conn.get(schoolName, (err, value) => {
    if (err) {
      console.log(err.message);
      return;
    }
    console.log(value);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
