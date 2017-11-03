
//node.JS email sending option
const request = require('request');

const emailAddresses = ['julien.grondin@ifpi.org','ieuan.rhysowen@ifpi.org','remus.cojocaru@ifpi.org','brunaldo.shabani@ifpi.org'];

let emailToSendTo = emailAddresses[getRandomInt(0,emailAddresses.length-1)].toLowerCase();

function sendEmail(emailAddressToSendTo) {
    let message = 'Hi ' + getFirstName(emailAddressToSendTo) +'<br/><br/>';
    message += 'It is your turn to make the tea today!<br/><br/>Thanks,<br/><br/>TeaBot v1.0';
    // <br/><br/>
    console.log(message);
    let formData = {
        email: emailAddressToSendTo,
        bcc: getBccs(emailAddresses, emailAddressToSendTo),
        subject: 'TeaBot v1.0 - Beta Testing',
        content: message,
    };
    request.post({
        url: 'http://athena.owlphacentri.com/iaps-ugc-sendmail-ws/ugc/sendMail/',
        formData: formData
    }, function optionalCallback(err, httpResponse, body) {
        if (err) {
            return console.error('Failed to send message:', err);
        }
        console.log('Message sent successfully!  Server responded with:', body);
    });
}

sendEmail(emailToSendTo);

function getFirstName(email) {
    switch (email) {
        case 'julien.grondin@ifpi.org':
            return 'Julien';
        case 'ieuan.rhysowen@ifpi.org':
            return 'Yayan';
        case 'remus.cojocaru@ifpi.org':
            return 'Remus';
        case 'brunaldo.shabani@ifpi.org':
            return 'Brunaldo';
        default:
            return 'No idea what this guy\'s name is :/';
    }
}

function getBccs(emails, emailToSendToHere) {
    let toReturn = '';
    for(let i in emails) {
        if(emails.hasOwnProperty(i)) {
            if(emails[i].toLowerCase() !== emailToSendToHere) {
                toReturn += emails[i] + ',';
            }
        }
    }

    return toReturn.substr(0, toReturn.length - 1);
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}