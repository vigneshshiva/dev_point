$(document).ready(function(){
  $('.comment_ok').on('click',function(){
    const input_comt = $('.input_qut').val();
    const button_id = $(this).attr('button-id')
    console.log(button_id);
    console.log(input_comt);
    $.ajax({
      type:'POST',
      url:'/comment',
      data :{'input':input_comt,'id':button_id},
      success:function(data){
        if(data.success == 'empty'){
          console.log('empty');
          alert('empty value is not allowed')
        }
        else{
          question_comment_list();
          console.log('full');
        }
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
          like_count(like);

        }else{
          $('.like_button').html('Unlike')
          like_count(like);

        }
      }
    });
  }

  function like_count(id_like){
    $.ajax({
      type:'POST',
      url:'/like_count',
      data:{'like_id':id_like},
      success :function(data){
        l = data.success
        $('.ll').html(l);
      }
    });
}
function question_comment_list(){
  const compt = $('.comment_ok').attr('button-id')
  console.log(compt);
  $.ajax({
    type:'POST',
    url:'/comment_list_view',
    data:{'pk_c':compt},
    success: function(data){
      $.each(data.comment,function(key,val){
        $('.comment_list').append('<div comment-id="'+val.id+'" class="comment_list_inner_div"><h1 class="comment_answer">'+val.comment+'</h1><div class="comment_footer"><p class="comment_user">'+val.user_answer__username+'</p></div></div>');
        });
    }
  });
}
  function answer_list(){
    const data_detail = $('.data_detail_id').val();
    $.ajax({
      type:'POST',
      url: '/answer_list',
      data:{'answer_list_id':data_detail},
      success : function(data){
        $.each(data.answer_answer,function(key,val){
          // $('.answer_list').clear();
          $('.answer_list').append('<div answer-id="'+val.id+'" class="answer_list_inner_div"><a class="answer_answer">'+val.answer+'</a><div class="answer_footer"><p class="answer_user">'+val.user_answer__username+'</p></div></div>');
          });
        }
    });
  }
  $('.comment_none').hide();
  $(document).on('click','.comment_btn',function(){
    $('.comment_none').show();
  });
  $(document).on('click','.comment_ok',function(){
    $('.comment_section').hide();
  });
  $(document).on('click','.comment_close',function(){
    $('.comment_section').hide();
  });

    $(document).on('click','.like_button',function(){
      const like_id = $(this).attr('like-id');
      console.log(like_id);
      like_pro();
    });

    $(document).on('click','.answer_button_detail',function(){
      var answer = $("#id_answer").val();
      var detail_id = $(this).attr('id_question');
      console.log(answer);
      $.ajax({
        type:'POST',
        url:'/answer',
        data:{'answer':answer,'detail_id':detail_id},
        success: function(data){
          if(data.success){
            answer_list();
            // like_pro();
          }
        }
      });
    });
});

// $(document).on('click','.like_answer',function(){
  //   const like_id = $(this).attr('like_id');
  //   console.log(like_id);
  //   $.ajax({
    //     type:'POST',
    //     url:'/answer_like',
    //     data:{'like_id':like_id},
    //     success : function(data){
      //       console.log('jai narashimaperumal');
      //       if(data.success=='answer_unliked'){
        //         console.log(like_id);
        //         console.log('narashimaperumal');
        //       }else{
          //         $('like_answer').html('Unlike')
          //         console.log('narashimaperumal potri ');
          //
          //         // $('.like_button').html('unlike')
          //       }
          //     }
          //   });
          // // }
          // });
