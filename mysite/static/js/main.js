//MODAL
$('.close').click(function(){
  $('.modal_wrap').hide();
  $('body').css({overflow: 'auto'});
});


$('.open_modal').click(function(){
  $('.modal_wrap').show();
  $('body').css({overflow: 'hidden'});
});


//MODAL-SLIDER
$('.close').click(function(){
  $('.modal-wrap-slider').fadeOut();
  $('body').css({overflow: 'auto'});
});


$('.open_modal').click(function(){
  $('.modal-wrap-slider').show();
  $('body').css({overflow: 'hidden'});
});

//MOB_MENU
$('.menu_btn').click(function(){
  $('.mob_nav').slideToggle();
  $('body').toggleClass('body_hidden');
});

 $('body').click(function(e){
     if( $(e.target).closest('.mob_menu').length)
       return;
    $('.mob_nav').slideUp();
  $('body').removeClass('body_hidden');
});

let statusGallery = false;
$('.slider4-item').click(function(){
  $('body').css({overflow: 'hidden'});
  $('.modal-wrap-slider').fadeIn();
  let id = $(this).attr('data-id');


  $.post('initgallery.php', {id: id}, function(response){
    console.log(response);
    response = JSON.parse(response);

    if(statusGallery == false)
    {
      statusGallery = true;
    }
    else
    {
      $('.slider-for, .slider-nav').slick('destroy');
      $('.slider-for, .slider-nav').empty();
    }

    for(var i in response)
    {
      $('.slider-for').append('<div class="big_img" style="background: url(./upload/img/'+ response[i].img +')no-repeat center/cover;"></div>');
      $('.slider-nav').append('<div class="small_img" style="background: url(./upload/img/'+ response[i].img +')no-repeat center/cover;"></div>');
    }

    initGallery();

  });

}); // gallery


$('.prices_btn').click(function(){
  $('html, body').animate({scrollTop: $('.service_table').offset().top -80}, 'slow');
});

$('.order_btn').click(function(){
  $('html, body').animate({scrollTop: $('.order').offset().top -0}, 'slow');
});

$('#order_form').submit(function(){
  let u_name = $('input[name="u_name"]').val();
  let u_phone = $('input[name="u_phone"]').val();
  let u_mess = $('textarea[name="u_mess"]').val();

  if(u_name == '')
  {
    $('input[name="u_name"]').css({background: '#fb9'});
  }
  else if(u_phone == '')
  {
    $('input[name="u_phone"]').css({background: '#fb9'});
  }
  else
  {
    $.post('send.php', {func: 'call_box', name: u_name, phone: u_phone, mess: u_mess}, function(response){
      if(response == true)
      {
        $('.pop-up').fadeIn().delay(2000).fadeOut();
        setTimeout(function(){
          window.location.reload();
        }, 3000);
      }
    })

  }

  return false;
});