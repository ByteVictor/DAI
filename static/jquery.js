
// código jQuery que se ejecuta al cargar la página
$(function () {

    // evento para cuando cambia el valor introducido en un <input id="buscar" $gt;
      $('#buscar').change(function(){
        let value = $(this).val()
        console.log(value)
        
        $.ajax({
          type : 'GET',
          
        )}
      );

      

    });
    
    // Click en el botón
    function Pulso(value) {
      // Para poner otra vez funciones jQuery en el DOM actual
      $(function () {
        console.log(value)
        
    
      });
    
    }

}