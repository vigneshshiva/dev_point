$(document).ready(function(){
  $('.pacchaiamman').on('click',function(){
    const input_comt = $('.input_qut').val();
    const button_id = $(this).attr('button-id')
    console.log(button_id);
    console.log(input_comt);
    $.ajax({
      type:'POST',
      url:'/comment',
      data :{'input':input_comt,'id':button_id},
      success:function(data){
        question_comment_list();

      }
    });
  });

  question_comment_list();
  answer_list();
  function like_pro(){
    const like = $('.data_detail_id').val();
    $.ajax({
      type:'POST',
      url:'/like',
      data:{'like_id':like},
      success : function(data){
        if(data.success=='is_liked'){
          $('.like_button').html('like')
        }else{
          $('.like_button').html('unlike')
        }
      }
    });
  }
  $(document).on('click','.like_answer',function(){
    const like_id = $(this).attr('like_id');
    console.log(like_id);
    // like_answer(like_id);
  // function like_answer(narashimaperumal){
  // like_count(like_id);
    // const like = $('.data_detail_id').val();
    $.ajax({
      type:'POST',
      url:'/answer_like',
      data:{'like_id':like_id},
      success : function(data){
        console.log('jai narashimaperumal');
        if(data.success=='answer_unliked'){
          console.log(like_id);
          console.log('narashimaperumal');
        }else{
          $('like_answer').html('Unlike')
          console.log('narashimaperumal potri ');

          // $('.like_button').html('unlike')
        }
      }
    });
  // }
  });

  function like_count(id_like){
    // console.log(count);
    $.ajax({
      type:'POST',
      url:'/like_count',
      data:{'like_id':id_like},
      success :function(data){
        // $.each(data.count,function(key,val){
        //   console.log(count);
        // });
        // if(data.cou){
          // console.log(data.cou);
        // }
        // console.log(count);
        // $('.like_button_count').append('<p>"'+count+'"</p>')
      }
    });
}
function question_comment_list(){
  const compt = $('.pacchaiamman').attr('button-id')
  console.log(compt);
  $.ajax({
    type:'POST',
    url:'/comment_list_view',
    data:{'pk_c':compt},
    success: function(data){
      console.log('pacchaiamman');
      $.each(data.comment,function(key,val){
        $('.comment_list').append('<div comment-id="'+val.id+'" class="comment_list_inner_div"><h1 class="comment_answer">'+val.comment+'</h1><div class="comment_footer"><p class="comment_user">'+val.user_answer__username+'</p><button class="button_like">like</></div></div>');
        });
    }
  });
}
  function answer_list(){
    const data_detail = $('.data_detail_id').val();
    console.log('pacchaiamman pacchaiamman');
    $.ajax({
      type:'POST',
      url: '/answer_list',
      data:{'answer_list_id':data_detail},
      success : function(data){
        $.each(data.answer_answer,function(key,val){

          $('.answer_list').append('<div answer-id="'+val.id+'" class="answer_list_inner_div"><a href="#" class="answer_answer">'+val.answer+'</a><div class="answer_footer"><p class="answer_user">'+val.user_answer__username+'</p>{% include "html/like_unlike_button.html" %}<button type="button" class="like_answer '+val.id+'" like_id="'+val.id+'" name="button">like</button></div></div>');

          });
        }
    });
  }
  $('.comment_none').hide();
  $(document).on('click','.comment_btn',function(){
    $('.comment_none').show();
    console.log('pacchaiamman manathieswara');
  });
  $(document).on('click','.pacchaiamman',function(){
    $('.comment_section').hide();
    console.log('pacchaiammanmanathieswara');
  });
  $(document).on('click','.pacchaiamman_close',function(){
    $('.comment_section').hide();
    console.log('pacchaiamman manathieswara');
  });

    $(document).on('click','.like_button',function(){
      const like_id = $(this).attr('like-id');
      console.log(like_id);
      like_pro();
      like_count(like_id);
    });

    $(document).on('click','.answer_button_detail',function(){
      console.log('answer')
      var answer = $("#id_answer").val();
      var detail_id = $(this).attr('id_question');
      console.log(answer);
      $.ajax({
        type:'POST',
        url:'/answer',
        data:{'answer':answer,'detail_id':detail_id},
        success: function(data){
          if(data.success){
            alert('answer submited "pacchaiamman potri"');
            answer_list();
            like_pro();
          }
        }
      });
    });
});
