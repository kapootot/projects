var frisby = require('frisby');

frisby.create('Ensure we are dealing with a teapot')
  .get('http://httpbin.org/status/418')
  .expectStatus(418)
.toss()