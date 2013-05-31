/* Ativando os tabs da tela inicial*/

$(document).ready(function(){
   var votos = 0;
   $('[id^="id_form"][id*="voto"]').each(
      function( index ) {
         if($(this).is(':not(:checked)')){
            $(this).parent().next().children().attr('disabled', true);
            $(this).parent().prev().children().attr('disabled', true);
         }else if(!$(this).parent().next().children().hasClass('erro-accordion')){
            $(this).parent().next().children().attr('disabled', true);
            $(this).parent().prev().children().attr('disabled', true);
            $(this).attr('disabled', true);
         }
         if($(this).is(':checked') && parseInt($('#qtd_votos').html()) == 10)
            votos += 1;
      }
   );
   $('#qtd_votos').html(parseInt($('#qtd_votos').html())-votos);

   $('[id^="id_form"][id*="voto"]').click(function(){
      if($(this).is(':checked')){
         if($(this).parent().next().children().hasClass('erro-accordion')){
            $(this).parent().next().children().children().attr('disabled', false);
            $(this).parent().prev().children().children().attr('disabled', false);

         }else{
            $(this).parent().next().children().attr('disabled', false);
            $(this).parent().prev().children().attr('disabled', false);
         }
         $('#qtd_votos').html(parseInt($('#qtd_votos').html())-1);
      }else{
         if($(this).parent().next().children().hasClass('erro-accordion')){
            $(this).parent().next().children().children().attr('disabled', true);
            $(this).parent().prev().children().children().attr('disabled', true);

         }else{
            $(this).parent().next().children().attr('disabled', true);
            $(this).parent().prev().children().attr('disabled', true);
         }
         if(parseInt($('#qtd_votos').html()) < 10)
            $('#qtd_votos').html(parseInt($('#qtd_votos').html())+1);
      }
   });

   $('#form-votacao').submit(function(){
      $('[id^="id_form"]').attr('disabled', false);
   });

   $('[class="errorlist"]').addClass('alert alert-error corpo-accordion');
   $('[class="errorlist"]').removeClass('errorlist');
});
