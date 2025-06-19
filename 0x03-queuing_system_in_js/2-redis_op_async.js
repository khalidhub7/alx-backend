import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client
  .on('connect', () => {
    console.log(
      'Redis client connected to the server',
    );
  })
  .on('error', (err) => {
    console.log(
      `Redis client not connected to the server: ${err}`,
    );
  });

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, res) => {
    redis.print(err, res);
  });
};

const displaySchoolValue = (schoolName) => {
  const getsync = promisify(client.get).bind(client);
  getsync(schoolName)
    .then((res) => console.log(res))
    .catch((err) => console.log(err));
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
