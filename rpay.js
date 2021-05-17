const Razorpay = require('razorpay');
const crypto = require('crypto');

// Create new instance
var instance = new Razorpay({
    key_id: 'rzp_test_EvTHllcABdpWnr',
    key_secret: 'e1iBCFvXvYtF31lNpcb5CKbM',
});


module.exports = (app) => {

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
    app.post('/rpay/handle',(req,res)=>{
        console.log('POST',req.body, req.query);

        rpay_oid = req.body.oid;
        // rpay_pid = req.body.razorpay_payment_id;
        // rpay_sign = req.body.razorpay_signature;
        rpay_pid = req.body.pid;
        rpay_sign = req.body.sign;

        const text = rpay_oid+'|'+rpay_pid
        const key = 'e1iBCFvXvYtF31lNpcb5CKbM'

        rpay_gen_sign = crypto.createHmac('sha256', key)
            .update(text)
            .digest('hex')

        console.log(rpay_gen_sign, rpay_sign);

        if(rpay_gen_sign == rpay_sign){
            res.send('OK');
        } else {
            res.send('Payment Invalid: If you were charged, please contact the Pravega Team. Details on the website.');
        }    
    })

    app.post('/api/event/registration',(req,res)=>{
        console.log(req.body);
        res.send('Registered on Server!')
    })
}