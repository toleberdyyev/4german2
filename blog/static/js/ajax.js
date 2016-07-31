
$(document).ready(function(){
  $('#comment').submit(function(){
    var post_id= $('.post').attr('id');
    var username = $('#username_author').html()
    var author=$('#id_author').val(username)
    var text = $('#id_text').val()
    var content = $('#comments_wall').html()
    var data_l = `
    <div class="comments_row">
    <p><b><a>${ username }</a> </b> right now  </p>
    <p class='pots_text'>${text}</p>
  </div>
    `
    var str=$(this).serialize()
    if (text != ''){
    $.ajax({
      type:'POST',
      data:str,
      success:function(html){
       $('#comments_wall').html(html)
       $('#id_author').val('')
       $('#id_text').val('')
       grecaptcha.reset();
      }
})}else{
  console.log('empty')
  grecaptcha.reset();
}
    return false;

  })



$('#newpost02').click(function(){
  if( $(this).html()=='cancel'){
    $(this).html('new post')
    $('#newpost01').slideUp('fast')
  }else{
    $(this).html('cancel')
    $('#newpost01').slideDown('fast')
  }
})


// REPLY BUTTON FUCNTION
$('.reply_btn').click(function(){
  console.log('asd')
  repid=$(this).attr('id')
  login=$('.'+repid).attr('id')
  id=repid.substring(3,repid.length)
  console.log(id,login)
  $('#reply_for').html('reply for <a>'+login+'</a>. or')
  $('#reply_for').slideDown('fast')
  $('#reply_for_cancel').slideDown('fast')
})

$('#reply_for_cancel').click(function(){
  console.log('asd')
  $('#reply_for').html('')
  $('#reply_for').slideUp('fast')
  $('#reply_for_cancel').slideUp('fast')

})

})
