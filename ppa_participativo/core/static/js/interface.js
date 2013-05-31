/* Ativando os tabs da tela inicial*/

$(document).ready(function(){     
   $('input[id^="id_dt_"]').datepicker({ dateFormat: "dd/mm/yy" }); 
   $('input[id^="id_dt_"]').datepicker("option", "monthNames", ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]);
   $('input[id^="id_dt_"]').datepicker("option", "dayNamesMin", ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]);
   $('input[id^="id_dt_"]').datepicker("option", "gotoCurrent", true );
   $('input[id^="id_dt_"]').mask("99/99/9999");
   // $('div[class="actions row"]').css("margin-right","3px");

   // $remover();
   
   // Verificar o motivo do não aplicação do efeito.
   $('input[id*="cpf"]').mask("999.999.999-99");
   $('input[id*="cnpj"]').mask("99.999.999/9999-99");
   $('input[id*="telefone"]').mask("(99) 9999-9999");
   $('input[id^="id_cep"]').mask("99999-999");
   $('input[id^="id_dat"][class="vTimeField"]').mask("99:99");

   /*Fim do Js para formulário de contato nas janelas modal JQuery*/

   $(window).keydown(function(event){
      if(event.keyCode == 13) {
         event.preventDefault();
         return false;
      }
   });

   if (!$('[id^="id_"]').val()){
      // $('[id^="id_"]').val('');
      $('[id^="id_"]:not([id^="id_cpf"])').attr('disabled', true);
      $('#submit_cadastro').attr('disabled', true);
      $('#id_cpf').attr('placeholder', 'Digite o CPF para verificar');
   }

   $('[id^="id_"]').each(function( index ) {
      $(this).attr('tabindex', index+1);
   });

   function verificar(){
      $.ajax({                                    
         url: '/verificar_cadastro/',
         type: "POST",
         data: {'cpf': $("#id_cpf").val()},
         dataType: "json",
         success: function(retorno){
            if(retorno.existe_cpf == 'false' && retorno.existe_erro == 'false'){
               $('[id^="id_"]:not([id^="id_cpf"])').val('');
               $('[id^="id_"]:not([id^="id_cpf"])').attr('disabled', false);
               $('#submit_cadastro').attr('disabled', false);
               $('#submit_cadastro').val('Participar');
            }else{
               if (retorno.pessoa){
                  $('[id^="id_"]:not([id^="id_cpf"])').each(function( index ) {
                     $(this).val(retorno.pessoa[$(this).attr('id').replace('id_', '')]);
                  });
                  $('[id^="id_"]:not([id^="id_cpf"])').attr('disabled', true);
                  $('.errorlist').hide();
                  $('#submit_cadastro').attr('disabled', false);
                  $('#submit_cadastro').val('Votar');
               }else{
                  $('[id^="id_"]:not([id^="id_cpf"])').val('');
                  $('#submit_cadastro').val('Participar');
               }
               $('#mensagem_erro').html(retorno.mensagem_erro);
               $('#modal_mensagem_erro').modal('show');
            }
         },
         error: function(xhr, er){
            alert('Busca Setores '+xhr.status + ' ' + xhr.statusText + ' '+ er);
         }        
      });
   };
   
   $('#id_cpf').blur(function() {
      verificar();
   });

   $('#id_cpf').keyup(function(e) {
      if (e.which == 13) {
         verificar();
      }
   });

   $('#verificar_cadastro').click(function(){
      verificar();
   });
});
