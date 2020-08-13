document.addEventListener('DOMContentLoaded', function () {
  var el = document.getElementsByClassName('tabs')
  var instance = M.Tabs.init(el[0], {
    // 'swipeable':true
  });


  

  // var elems = document.querySelectorAll('.tap-target');
  // var instances = M.TapTarget.init(elems, {});
  //instances[0].open()

  // document.addEventListener('click', function () {
  //   instances[0].close()
  // })

  var col_elems = document.querySelectorAll('.collapsible');
  var col_instances = M.Collapsible.init(col_elems, {
    'onCloseEnd': turn(),
    'onOpenEnd': ulta(),
    'accordian': false
  });

  function ulta(params) {
    console.log('Opened')
  }

  function turn(params) {
    console.log('Hello');
  }


  var nvwrapheight = document.getElementsByClassName('nav-wrapper')[0].getBoundingClientRect()
  console.log(nvwrapheight)
  document.getElementById('aligner').style.height = nvwrapheight.height + 'px'
  // console.log(nvwrapheight.height + (48-56) +'px')
  // document.getElementById('aligner1').style.height = nvwrapheight.height + 48 +'px'
  document.getElementById('aligner1').style.height = nvwrapheight.height + 'px'
  document.getElementById('aligner2').style.height = nvwrapheight.height + 'px'
  document.getElementById('logo').style.height = (0.8 * nvwrapheight.height) + 'px'
  document.getElementById('logo').style.width = 'auto'
  document.getElementById('homeDisplay').style.height = (screen.availHeight - nvwrapheight) + 'px'


})

var scrollPos = 0
var activated = true;
function scrolll() {
  // console.log('Scrolling...')
  console.log('activated.')
  var pos = document.getElementsByTagName('BODY')[0];
  var abt = document.getElementById('myFoot');
  if (scrollPos < pos.scrollLeft) {
    document.getElementById('schedtab').click()
    console.log('Scrolling down...')
    activated = false;
    console.log(window.location.replace('#desc'))
  }

  scrollPos = pos.scrollLeft;



  // if(pos.scrollTop < abt.offsetTop){
  //   window.scrollTo(0,document.getElementById('abText').offsetTop)
  // } else {
  //   console.log('There you go.')
  // }

  // console.log(abt.offsetTop)
  // abt.scrollIntoView()\
  // pos.scrollTo(0, abt.offsetTop)
}

var start = null;
window.addEventListener("touchstart", function (event) {
  if (event.touches.length === 1) {
    //just one finger touched
    start = event.touches.item(0).clientX;
  } else {
    //a second finger hit the screen, abort the touch
    start = null;
  }
});

window.addEventListener("touchend",function(event){
  var offset = 100;//at least 100px are a swipe
  if(start){
    //the only finger that hit the screen left it
    var end = event.changedTouches.item(0).clientX;

    if(end > start + offset){
      console.log('right click')
      document.getElementById('hometab').click()
    }
    if(end < start - offset ){
      console.log('left click')
      document.getElementById('schedtab').click()
    }
  }
});