var bigint = require('bigint');

var b = bigint('782910138827292261791972728324982')
    .sub('182373273283402171237474774728373')
    .div(8)
    .toString()
;
console.log(b);
