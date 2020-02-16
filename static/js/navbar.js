$(document).ready(function(){
  // $(document).on('click','.line_1',function(){
  //   // alert('pacchaiamman');
  //   console.log('pacchaiamman');
  // });
  $('.line').on('click',function(){
    $('.home-menu-left').addClass('home-menu-on');
    $('.home-menu').addClass('home-on');
  });
  $('.close').on('click',function(){
    $('.home-menu-left').removeClass('home-menu-on');
    $('.home-menu').removeClass('home-on');
  });
  $(window).on('scroll',function(){
    var scroll = $(window).scrollTop();
    // alert('pacchaiamman');
    if($(window).width()<900){
      // alert('window is 900')

    }else{
      if($(this).scrollTop()>100){
        $('.nav_bar_detail').addClass('detail_nav');
        console.log('scroll');
        $('.home-nav').addClass('home_nav_onscroll');
        $('.line_1').addClass('line_1_scroll');
        $('.line_2').addClass('line_1_scroll');
        $('.line_3').addClass('line_1_scroll');
      }else{
        $('.nav_bar_detail').removeClass('detail_nav');
        $('.home-nav').removeClass('home_nav_onscroll');
        $('.line_1').removeClass('line_1_scroll');
        $('.line_2').removeClass('line_1_scroll');
        $('.line_3').removeClass('line_1_scroll');
      }
    }
  });
    // }

  // const dummy_logo = document.querySelector('.dummy_logo');
  // const dummy_img = document.querySelector('.dummy-img');
  // const dummy_home_menu = document.querySelector('.dummy_home_menu');
  // const onscroll_ask = document.querySelector('.ask');
  // const onscroll_drop = document.querySelector('.drop');
  // const onscroll_ans = document.querySelector('.ans');
  // const onscroll_profile = document.querySelector('.profile');
  // const profile = document.querySelector('.home-menu-left');
  // const onscroll_nav_slice = document.querySelector(".nav-slice");
  // const onscroll_nav_slice_li = document.querySelector(".nav-slice_li");
  // const question_content = document.querySelector('.question_cont');
  // const home_nav = document.querySelector('.home-nav');
  //
  // var scroll = $(window).scrollTop();
  //   $(window).scroll(function(){
  //     if($(this).scrollTop()>100){
  //       console.log('scroll');
  //       home_nav.classList.remove('home-nav');
  //       home_nav.classList.add('onscroll_home_nav');
  //     }
  //     else{
  //       home_nav.classList.add('home-nav');
  //       home_nav.classList.remove('onscroll_home_nav');
  //       // dummy_img.classList.remove('onscroll_img');
  //       // dummy_img.classList.add('dummy_img');
  //     }
  //   });
  // // var resize = $(window.innerWidth)
});
