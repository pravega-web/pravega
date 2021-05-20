// Central App
var app = angular.module('pravega', []);

app.controller('quadSparkController', ($scope, $http) => {
    console.log('QuadSpark controller loaded...');

    $scope.pageName = 'Quadspark';
    // Amount to pay - Built into page
    $scope.amt = 200

    // Event Name
    $scope.event = 'Quadspark'

    // Payment Button
    $scope.pay = () => {

        // Ask server for new order ID
        $http({
            'method': 'GET',
            'url': '/rpay/new',
            'params': {
                'amt': $scope.amt * 100
            }
        }).then((res) => {
            // Success
            console.log(res.data);

            // Order ID
            $scope.o_id = res.data.id;

            // Options
            var options = {
                "key": "rzp_test_EvTHllcABdpWnr", // Enter the Key ID generated from the Dashboard
                "amount": ($scope.amt * 100) + '', // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                "currency": "INR",
                "name": "Pravega'21",
                "description": $scope.event,
                "image": "/old_front_end/img/pravega21_logo.svg",
                "order_id": $scope.o_id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                // "callback_url": "/rpay/handle?oid="+$scope.o_id,
                "handler": function (response) {
                    console.log('Recieved confirmation, now validating...');
                    $scope.handle(response)
                },
                "theme": {
                    "color": "#3399cc"
                }
            };


            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function (response) {
                alert(response.error.code);
                alert(response.error.description);
                alert(response.error.source);
                alert(response.error.step);
                alert(response.error.reason);
                alert(response.error.metadata.order_id);
                alert(response.error.metadata.payment_id);
            });

            rzp1.open();

        }, (res) => {
            alert(res)
        })

    }

    $scope.handle = (response) => {

        // alert(response.razorpay_payment_id);
        // alert(response.razorpay_order_id);
        // alert(response.razorpay_signature)}
        $scope.rpay_response = response;
        $http({
            'method': 'POST',
            'url': '/rpay/handle',
            'data': {
                'oid': $scope.o_id,
                'pid': response.razorpay_payment_id,
                'sign': response.razorpay_signature
            }
        }).then((res) => {
            $scope.ressss = res.data
            $scope.register()
        }, (res) => { alert(JSON.stringify(res)) })
    }

    $scope.register = function () {
        $http({
            method: 'POST',
            url: '/api/event/registration',
            data: {
                'name': $scope.name,
                'email': $scope.email,
                'date': new Date(),
                'event': $scope.event,
                'rpay': {
                    'oid': $scope.o_id,
                    'pid': $scope.rpay_response.razorpay_payment_id,
                    'sign': $scope.rpay_response.razorpay_signature
                },
                'meta': {
                    'admit': 1
                },
                "grades": $scope.grades,
                "phone": $scope.phone
            }
        }).then((res)=>{$scope.success='Successful registration. Please check your inbox for the confirmation email.'},(res)=>{$scope.failure = "Transaction successful but the registartion on the Pravega Server was unsuccessful. Please contact Pravega Web Team with the following id - "+$scope.o_id})
    }
})