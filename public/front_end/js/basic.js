var app = angular.module('pravegaApp', [])
app.controller('d_controller', function ($scope) {
  console.log('app')
  $scope.msg = 'log'
})

app.controller('login_controller', function ($scope, $http) {
  console.log('Login controller loaded...')
  $scope.errorLevel = false;

  $scope.username = ''

  $scope.validate = (access) => {

    console.log('Logging in as ', access)

    if ($scope.username == '') {
      // window.location.reload();
    }

    var creds = {
      'username': $scope.username,
      'password': $scope.pword
    }

    console.log(creds);

    $http({
      'method': 'POST',
      'url': '/api/login',
      'data': creds
    }).then(
      (res) => {
        console.log('Auth success')
        sessionStorage.setItem('_id', res.data[0]._id)
        window.location = '/userhome'
      },
      (res) => {
        console.log(res.data)
        if (res.status == 401) {
          console.log('Error')
          $scope.errorCode = 'Invalid email or password.'
          $scope.errorLevel = true
        }
      }
    )

  }

})


app.controller('userhome_controller', function ($scope, $http) {
  console.log('User homepage controller loaded...')

  if (!sessionStorage.getItem('_id')) {
    console.log('Not signed in')
    window.location.replace('/login');
  }

  $http({
    'method': "POST",
    'url': '/api/find/user',
    'data': { '_id': sessionStorage.getItem('_id') }
  }).then(
    (data) => {
      var user = data.data[0]
      $scope.name = user.name
      $scope.email = user.email
      $scope.edu = user.edu
      $scope.phone = user.phone
      $scope.trId = user.meta.trId
      $scope.availcredits = user.meta.credit
      $scope.ca = user.ca
      $scope.pword = user.pword
      $scope.old_pword = user.pword
      $scope.refId = user.refId
      $scope.close_eye = 'visibility_off'

      $scope.refs = user.meta.refs

      $scope.vendorlink = "https://pravega.glitch.me/vendor?_id=" + user._id

      var qr = new QRCode(document.getElementById("qrcode"), {
        text: "https://pravega.glitch.me/vendor?_id=" + user._id,
        correctLevel: QRCode.CorrectLevel.H
      });

      $scope.share_ca_code = function () {

        if (window.navigator.share) {
          navigator.share({
            title: 'Pravega 2021',
            text: 'Pravega 2021 workshops are live! Use my code \n' + $scope.refId + '\n and register today! \n',
            url: 'https://bit.ly/PravegaAug',
          }).then(() => console.log('Successful share'))
            .catch((error) => console.log('Error sharing', error));
        }
      }

      // Password.
      $scope.pUpdate = function () {

        // Update user
        user.pword = $scope.pword;

        console.log(user);

        $http({
          'method': 'POST',
          'url': '/api/update/user',
          'data': user
        }).then((res) => { window.location.reload() }, (err) => { console.log(err) })

      }

    },
    (err) => { console.error(err) }
  )

})

app.controller('vendor_controller', function ($scope, $http) {
  console.log('Vendor controller loaded...')

  const urlParams = new URLSearchParams(window.location.search);
  const myParam = urlParams.get('_id');

  $scope.user_id = myParam;

  $scope.credit = function () {

    $http({
      'method': 'POST',
      'url': '/api/credit',
      'data': {
        '_id': $scope.user_id,
        'trId': $scope.trId,
        'credit': $scope.credits
      }
    }).then(
      (res) => {
        console.log(res.data);
        alert(res.data)
      },
      (err) => { console.error(err); alert(res.data) }
    )
  }


})


// var app = angular.module('pravegaApp')

// app.controller('d_controller',function ($scope){
//   console.log('demo controller loaded...')
// })

app.controller('signup_controller', function ($scope, $http) {
  console.log('CA SignUp controller loaded...')

  $scope.validate = () => {

    var newUser = {
      'name': $scope.name,
      'email': $scope.email.toLowerCase(),
      'pword': $scope.pword,
      'edu': $scope.edu,
      'phone': $scope.phone,
      'ca': {
        'is': true,
        'credit': 0
      }
    }

    $http({
      'method': 'POST',
      'url': '/api/create/user',
      'data': newUser
    }).then(
      (res) => {
        console.log('Success')
        $scope.response = 'Succesfully created CA account, refresh page for new entry'
      },
      (res) => {
        console.log(res.data)
        $scope.response = 'Error! If error persists, contact Website Coordinators'
      }
    )

  }

})


app.controller('rpay_controller', ($scope, $http) => {

  // Amount to pay - Built into page
  $scope.amt = 3000

  // Event Name
  $scope.event = 'Demo Event'

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
        "prefill": {
          "name": "Chinmay K Haritas",
          "email": "chinmayharitas@gmail.com",
          "contact": "8073441473"
        },
        "notes": {
          "event": $scope.event
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
        'meta':{
          'admit':1
        }
      }
    })
  }
})