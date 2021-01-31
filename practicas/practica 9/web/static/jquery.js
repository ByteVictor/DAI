
const ip_api = 'http://192.168.137.128:5000/api';

// código jQuery que se ejecuta al cargar la página
$(function () {

    // evento para cuando cambia el valor introducido en un <input id="buscar" $gt;
      $('#buscar').change(function(){
        let titulo_buscar = $(this).val()
        console.log(titulo_buscar)
        
        let htmlString = '';
        htmlString += `<tr>
        <th scope="col">Título</th>
        <th scope="col">Categoría</th>
        <th scope="col">Acción</th>
        </tr>`

        $.ajax({
          url: ip_api+'/buscarpelis?titulo='+encodeURIComponent(titulo_buscar),

          type: 'GET',
          
          dataType: 'json',

          success : function(json) {          
            //tabla.append("<tr><td>cosa</td></tr>")
            $.each(json, function (i, v) {
              htmlString += `
              <tr id="${v._id}">
              <td>${v.Title}</td>
              <td>${v.Category}</td>
              <td><button class="btn btn-danger btn-sm mr-2" onclick="Pulso('${v._id}')">Borrar</button></td>
              </tr>` 

              console.log(i + " peli: " + v.Title);
            })
            $("table").html(htmlString);
          },

          error : function(xhr, status) {
            alert('Error en la petición a la API');
          },

        })}
      );
});

// Click en el botón
function Pulso(id_peli) {
  // Para poner otra vez funciones jQuery en el DOM actual
  $(function () {
    console.log(id_peli)

    $.ajax({
      url: ip_api+'/pelis/'+id_peli,

      type: 'DELETE',

      success : function(json) {
        $("#"+id_peli).hide();
      },

      error : function(xhr, status) {
        alert('No se ha podido borrar correctamente');
      },
    })
  });

}