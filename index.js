const eksisozluk = require('eksisozluk-api');

eksisozluk.entry.getEntry('1').then(
    (data) => {
        console.log(data);
    }
);

eksisozluk.user.getUser('ssg').then(
    (data) => {
        console.log(data);
    }
);

eksisozluk.startServer();