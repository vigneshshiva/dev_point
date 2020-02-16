$(window).on('load',function(){
$('.email_valid').hide();
$('.password_otp').hide();
});
$(document).on('click','.forgot_your_password',function(){
  console.log('pachaiamman');
  $('.login_close').hide();
  $('.email_valid').show();
});
$(document).on('click','.send_email',function(){
  console.log('email');
  const user_mail = $('.email_password').val();
  if(user_mail == ''){
    alert('empty field');
  }else{
    $.ajax({
      type:'POST',
      url:'/email',
      data:{'val':user_mail},
      success : function(data){
        console.log('mess success');
        if(data.success){
          alert('mail send successfully');
          $('.email_valid').hide();
          $('.password_otp').show();
        }else{
          alert('invalid email');
        }
      }
    });
  }
    
});
$(document).on('click','.save_signup',function(){
  console.log('pacchaiamman');
  const username = $('#id_username').val();
  const email = $('.email_register').val();
  console.log(email);
  console.log(username);
  const password1 = $('#id_password1').val();
  const password2 =$('#id_password2').val();
  signup_process(username,email,password1,password2);
});
function signup_process(username,email,password1,password2){
  console.log('pacchaiamman');
  $.ajax({
    type:'POST',
    url:'/signup',
    data:{'username':username,'email':email,'password1':password1,'password2':password2},
    success: function(data){
      if(data.username){
        console.log('username error');
        alert('username already taken!');
      }else if(data.email){
          console.log('email error');
          alert('email already taken!');
      }else if(data.password){
          console.log('password error');
          alert('password does not match');
      }else{
        alert('user created');
        window.location.href="home"
        window.onload();
      }
    }
  });
}
  function login_process(user,password){
    console.log('pacchaiamman');
    $.ajax({
      type:'POST',
      url:'/login',
      data:{'email':user,'password':password},
      success: function(data){
        if (data.success){
          window.location.href="home"
        }
      }
    });
  }
  $(document).on('click','.save_login',function(){
    console.log('pacchaiamman')
    const user = $('.emailinput').val();
    console.log(user)
    const password = $('#id_password').val();
    console.log(password)
    login_process(user,password);
  });
