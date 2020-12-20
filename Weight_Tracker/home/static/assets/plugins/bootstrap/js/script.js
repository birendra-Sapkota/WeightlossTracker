//
//$(document).ready(() => {
//    // SideNav Initialization
//
//  })

});

 $(document).ready(function(){
//  $(".button-collapse").sideNav();
//      new WOW().init();

 $(window).scroll(function(){
    if ($(window).scrollTop() > 100){
      $('.navbar').addClass( "bg-dark");
    } else {
      $('.navbar').removeClass("bg-dark");
    }
  });
 });