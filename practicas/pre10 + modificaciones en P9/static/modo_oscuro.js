
function toggleModoOscuro() {
    if (this.checked){
        Cookies.set('modoOscuro', true);
        console.log("DarkMode Cookie: " + Cookies.get('modoOscuro'));
        
        $(["[class*='-light']"] ).each((i,ele)=>{
            $(ele).toggleClass('bg-dark')
            $(ele).toggleClass('text-dark')
            $(ele).toggleClass('border-dark')
            $(ele).toggleClass('navbar-dark')
        })

        $("#columna-main").toggleClass("bg-secondary")
        $("table").toggleClass("text-light")
        $(".custom-control").toggleClass("text-light")

        $("footer").toggleClass("bg-dark bg-light bg-secondary text-dark text-light")

    } else {
        Cookies.set('modoOscuro', false);
        console.log("DarkMode Cookie: " + Cookies.get('modoOscuro'));

        $(["[class*='-dark']"] ).each((i,ele)=>{
            $(ele).toggleClass('bg-dark')
            $(ele).toggleClass('text-dark')
            $(ele).toggleClass('border-dark')
            $(ele).toggleClass('navbar-dark')
        })
        
        $("#columna-main").toggleClass("bg-secondary")
        $("table").toggleClass("text-light")
        $(".custom-control").toggleClass("text-light")

        $("footer").toggleClass("bg-dark bg-light bg-secondary text-dark text-light")

    }
}

$(function () {

    $('#darkSwitch').change( toggleModoOscuro );
    
    if( Cookies.get('modoOscuro') === 'undefined' ){
        console.log("Cooki sin definir: " + Cookies.get('modoOscuro'));
        Cookies.set('modoOscuro', false);
        //console.log(Cookies.get('modoOscuro'));
    } else {
        console.log("La cookie es: " + Cookies.get('modoOscuro'));
        if( Cookies.get('modoOscuro') == 'true' ){
            $("#darkSwitch").prop('checked', Cookies.get('modoOscuro')).change();
        }
    }

    console.log(Cookies.get('modoOscuro'));
});