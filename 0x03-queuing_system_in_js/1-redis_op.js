import redis from 'redis';

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
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, res) => (
    console.log(err ? err.message : res)
  ));
};

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
