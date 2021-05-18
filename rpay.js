const Razorpay = require('razorpay');
const crypto = require('crypto');

// Create new instance
var instance = new Razorpay({
    key_id: 'rzp_test_EvTHllcABdpWnr',
    key_secret: 'e1iBCFvXvYtF31lNpcb5CKbM',
});


module.exports = (app, AWS) => {

    // Generate new key
    app.get('/rpay/new', (req, res) => {

        // Log
        console.log('New Payment Initiated Rs', req.query.amt);

        // Options
        var options = {
            amount: req.query.amt,  // amount in the smallest currency unit
            currency: "INR"
        };

        // Create new order and send the deets to clientboy
        instance.orders.create(options, function (err, order) {
            if (err) {
                throw err;
            }
            res.json(order);
            console.log('Payment ID sent to client');
        });

    })


    // Handling the success
    app.post('/rpay/handle', (req, res) => {
        console.log('POST', req.body, req.query);

        rpay_oid = req.body.oid;
        // rpay_pid = req.body.razorpay_payment_id;
        // rpay_sign = req.body.razorpay_signature;
        rpay_pid = req.body.pid;
        rpay_sign = req.body.sign;

        const text = rpay_oid + '|' + rpay_pid
        const key = 'e1iBCFvXvYtF31lNpcb5CKbM'

        rpay_gen_sign = crypto.createHmac('sha256', key)
            .update(text)
            .digest('hex')

        console.log(rpay_gen_sign, rpay_sign);

        if (rpay_gen_sign == rpay_sign) {
            res.send('OK');
        } else {
            res.send('Payment Invalid: If you were charged, please contact the Pravega Team. Details on the website.');
        }
    })

    app.post('/api/event/registration', (req, res) => {
        console.log(req.body);
        res.send('Registered on Server!')
    })
}

function sendMail(AWS, deets) {
    // Create sendEmail params 
    var params = {
        Destination: { /* required */
            CcAddresses: [],
            ToAddresses: [deets.email]
        },
        Message: { /* required */
            Body: { /* required */
                Html: {
                    Charset: "UTF-8",
                    Data: "HTML_FORMAT_BODY"
                },
                Text: {
                    Charset: "UTF-8",
                    Data: "TEXT_FORMAT_BODY"
                }
            },
            Subject: {
                Charset: 'UTF-8',
                Data: 'Test email'
            }
        },
        // TODO: Add our email
        Source: 'SENDER_EMAIL_ADDRESS', /* required */
        // TODO: Check with Shaker
        ReplyToAddresses: [
            'EMAIL_ADDRESS',
            /* more items */
        ],
    };

    // Create the promise and SES service object
    var sendPromise = new AWS.SES({ apiVersion: '2010-12-01' }).sendEmail(params).promise();

    // Handle promise's fulfilled/rejected states
    sendPromise.then(
        function (data) {
            console.log(data.MessageId);
        }).catch(
            function (err) {
                console.error(err, err.stack);
            });
}