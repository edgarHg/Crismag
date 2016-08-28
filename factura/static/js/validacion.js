//script de boostrap de template

    /*====Select Box====*/
    $(function () {
        $(".chzn-select").chosen();
        $(".chzn-select-deselect").chosen({
        allow_single_deselect: true
        });
    });

    /*====TAGS INPUT====*/
    $(function () {
        $('#tags_1').tagsInput({
            width: 'auto'
        });
        $('#tags_2').tagsInput({
            width: 'auto',
            onChange: function (elem, elem_tags) {
                var languages = ['php', 'ruby', 'javascript'];
                $('.tag', elem_tags).each(function () {
                    if ($(this).text().search(new RegExp('\\b(' + languages.join('|') + ')\\b')) >= 0) $(this).css('background-color', 'yellow');
                });
            }
        });
    });
    /*====Select Box====*/
    $(function () {
        $(".chzn-select").chosen();
        $(".chzn-select-deselect").chosen({
            allow_single_deselect: true
        });
    });
    /*====Color Picker====*/
    $(function () {
        $('.colorpicker').colorpicker({
            format: 'hex'
        });
        $('.pick-color').colorpicker();
    });
    /*====DATE Time Picker====*/
    $(function () {
        $('#datetimepicker1').datetimepicker({
            language: 'pt-BR'
        });
    });
    $(function () {
        $('#datetimepicker11').datetimepicker({
            language: 'pt-BR'
        });
    });
    $(function () {
        $('#datetimepicker3').datetimepicker({
            pickDate: false
        });
    });
    $(function () {
        $('#datetimepicker4').datetimepicker({
            pickTime: false
        });
    });
    $(function () {
        $('#datetimepicker44').datetimepicker({
            pickTime: false
        });
    });
    $(function () {
        $('#datetimepicker444').datetimepicker({
            pickTime: false
        });
    });
    
    $(function () {
        $('#datetimepicker8').datetimepicker({
            pickTime: false
        });
    });
    /*DATE RANGE PICKER*/
    $(function () {
        $('#reportrange').daterangepicker({
            ranges: {
                'Today': ['today', 'today'],
                'Yesterday': ['yesterday', 'yesterday'],
                'Last 7 Days': [Date.today().add({
                    days: -6
                }), 'today'],
                'Last 30 Days': [Date.today().add({
                    days: -29
                }), 'today'],
                'This Month': [Date.today().moveToFirstDayOfMonth(), Date.today().moveToLastDayOfMonth()],
                'Last Month': [Date.today().moveToFirstDayOfMonth().add({
                    months: -1
                }), Date.today().moveToFirstDayOfMonth().add({
                    days: -1
                })]
            },
            opens: 'left',
            format: 'dd/MM/yyyy',
            separator: ' to ',
            startDate: Date.today().add({
                days: -29
            }),
            endDate: Date.today(),
            minDate: '01/01/2012',
            maxDate: '12/31/2013',
            locale: {
                applyLabel: 'Submit',
                fromLabel: 'From',
                toLabel: 'To',
                customRangeLabel: 'Custom Range',
                daysOfWeek: ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
                monthNames: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                firstDay: 1
            },
            showWeekNumbers: true,
            buttonClasses: ['btn-danger']
        },
        function (start, end) {
            $('#reportrange span').html(start.toString('MMMM d, yyyy') + ' - ' + end.toString('MMMM d, yyyy'));
        });
        //Set the initial state of the picker label
        $('#reportrange span').html(Date.today().add({
            days: -29
        }).toString('MMMM d, yyyy') + ' - ' + Date.today().toString('MMMM d, yyyy'));
    });
    $(function () {
        $('#reservation').daterangepicker();
    });

/*===============================================
TBALE THEMES
==================================================*/
$(function() {
        $(".paper-table").tablecloth({
          theme: "paper",
          striped: true,
          sortable: true,
          condensed: false
        });
      });
$(function() {
      $('.data-grid').dataTable({ "sDom": "<'row-fluid'<'span6'l><'span6'f>r>t<'row-fluid'<'span6'i><'span6'p>>"
          });
      });     
/**=========================
LEFT NAV ICON ANIMATION 
==============================**/
$(function () {
    $(".left-primary-nav a").hover(function () {
        $(this).stop().animate({
            fontSize: "30px"
        }, 200);
    }, function () {
        $(this).stop().animate({
            fontSize: "24px"
        }, 100);
    });
});

$(function(){
    $("a.switcher").bind("click", function(e){
        e.preventDefault();
        var theid = $(this).attr("id");
        var theproducts = $("ul#products");
        var classNames = $(this).attr('class').split(' ');
        var gridthumb = "images/grid-default-thumb.png";
        var listthumb = "images/list-default-thumb.png";
        if($(this).hasClass("active")) {
            // if currently clicked button has the active class
            // then we do nothing!
            return false;
        } else {
            // otherwise we are clicking on the inactive button
            // and in the process of switching views!
            if(theid == "gridview") {
                $(this).addClass("active");
                $("#listview").removeClass("active");
                // remove the list class and change to grid
                theproducts.removeClass("list");
                theproducts.addClass("grid");
                // update all thumbnails to larger size
                $("img.thumb").attr("src",gridthumb);
            }
            else if(theid == "listview") {
                $(this).addClass("active");
                $("#gridview").removeClass("active");
                // remove the grid view and change to list
                theproducts.removeClass("grid")
                theproducts.addClass("list");
                // update all thumbnails to smaller size
                $("img.thumb").attr("src",listthumb);
            } 
        }
    });
});


//fin del script del boostrap del template


//scrip para que funcione el ajax en django

$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
}); 

//fin del script para que funcione el ajax en django

//validacion de formulario del personal

$(function () {
                // validate signup form on keyup and submit
                $("#signupForm").validate({
                    rules: {
                        first_name: "required",
                        last_name: "required",
                        sexo:"required",
                        id_tipo_usuario:"required",
                        localidad:"required",

                        asesor:"required",



                        pais:"required",
                        estado:"required",
                        direccion:"required",
                        codigo_postal:"required",

                        agencia:"required",
                        puesto:"required",
                        username: {
                            required: true,
                            minlength: 5,
                            maxlength: 30,
                        },
                        fecha_nacimiento: {
                            required: true
                        },
                        telefono: {
                            required: true,
                            maxlength: 10,
                            minlength: 10
                        },
                        password: {
                            required: true,
                            minlength: 5
                        },
                        confirm_password: {
                            required: true,
                            minlength: 5,
                            equalTo: "#password"
                        },
                        email: {
                            required: true,
                            email: true
                        },
                        topic: {
                            required: "#newsletter:checked",
                            minlength: 1
                        },
                        agree: "required",
                        padre: "required",
                        nombre: "required",
                        fecha_ultimo_cambio:"required",
                        id_lugar:"required",
                        id_agencia:"required",
                        id_depatamento:"required",
                        director:"required",
                        tel:"required",

                        
                        id_precio:"required",
                        id_precio2:"required",
                        tipo_comunicacion:"required",
                        comentario:"required",
                        status:"required",
                        fecha_seguimiento:"required",
                        folio:"required",
                        pago:"required",

                        llevallega:"required",
                        dv1:"required",
                        personal1:"required",
                        chaperon1:"required",
                        otro1:"required",
                        recibeentraga:"required",
                        dv2:"required",
                        personal2:"required",
                        chaperon2:"required",
                        otro2:"required",
                        reserva:"required",

                        user:"required",
                        nuevo:"required",

                        programa:"required",
                        salida:"required",
                        vigencia:"required",
                        ninos:"required",
                        ninas:"required",

                        claveprecio:"required",
                        precio_promo:"required",
                        tipo_cambio:"required",
                        fecha_inicial:"required",
                        fecha_final:"required",
                        names:"required",
                        apes:"required",
                        datos:"required",

                    },
                    messages: {
                        first_name: "Por favor, escribe el nombre",
                        last_name: "Por favor, escribe los apellidos",
                        sexo:"Por favor, seleccione el sexo",
                        id_tipo_usuario:"Por favor, seleccione el tipo de usuario",
                        pais:"Por favor, seleccione el pais",
                        estado:"Por favor, seleccione el estado",
                        direccion:"Por favor, ingrese la direccion",
                        codigo_postal:"Por favor, ingrese el codigo postal",
                        localidad:"Por favor, seleccione la localidad",
                        agencia:"Por favor, seleccione la agencia",
                        puesto:"Por favor, seleccione el puesto",
                        fecha_nacimiento:"Por favor, ingrese su la fecha de nacimineto",
                        

                        id_precio:"Por favor, seleccione el programa",
                        id_precio2:"Por favor, seleccione el precio",
                        tipo_comunicacion:"Por favor, seleccione el tipo de comuicación",
                        comentario:"Por favor, escriba el comentario",
                        status:"Seleccione una opción",
                        fecha_seguimiento:"Ingrese la nueva fecha de seguimiento",
                        folio:"Ingrese el folio de pago",
                        pago:"Ingrese la cantidad a pagar",
                        
                        llevallega:"Campo requerido",
                        dv1:"Ingrese datos del vuelo",
                        personal1:"Campo requerido",
                        chaperon1:"Campo requerido",
                        otro1:"Escriba el nombre completo",
                        recibeentraga:"Campo requerido",
                        dv2:"Ingrese datos del vuelo",
                        personal2:"Campo requerido",
                        chaperon2:"Campo requerido",
                        otro2:"Escriba el nombre completo",

                        reserva:"Escriba el numero de reserva",

                        user:"Escriba el nombre del usuario",
                        nuevo:"Escriba la nueva contraseña",

                        programa:"Seleccione el programa",
                        salida:"Seleccione la salida",
                        vigencia:"Ingrese la fecha de salida",
                        ninos:"Ingrese la cantidad de niños para este paquete",
                        ninas:"Ingrese la cantidad de niñas para este paquete",


                        telefono:{
                            required: "Ingrese el numero de Telefono",
                            maxlength: "Maximo 10 dígitos",
                            minlength: "Minimo 10 dígitos"
                        },
                        username: {
                            required: "Por favor, escribe el nombre de usuario(Nesesario para entrar al sistema)",
                            minlength: "Your username must consist of at least 5 characters"
                        },
                        password: {
                            required: "Por favor, ingrese la contraseña",
                            minlength: "LA contraseña debe tener al menos 5 caracteres"
                        },
                        confirm_password: {
                            required: "Por favor, ingrese la contraseña",
                            minlength: "La contraseña debe tener al menos 5 caracteres",
                            equalTo: "Por favor, introduzca la misma contraseña que el anterior"
                        },
                        email: "Por favor, introduzca una dirección e-mail válida",
                        agree: "Por favor, acepte nuestra política de privacidad",
                        
                        padre: "Este campo es requerido",
                        nombre: "Ingrese el nombre",
                        fecha_ultimo_cambio: "Ingrese la fecha",
                        id_lugar: "Ingrese el lugar",
                        id_agencia: "Ingrese la agencia",
                        id_depatamento: "Ingrese el departamento",
                        director:"Ingrese el nombre del director",
                        tel:"Ingrese el el telefono",


                        claveprecio:"Seleccione la clave del precio",
                        precio_promo:"Ingrese el precio",
                        tipo_cambio:"Seleccione la moneda",
                        fecha_inicial:"Ingrese la fecha inicial",
                        fecha_final:"Ingrese la fecha final",
                        names:"Ingrese el nombre",
                        apes:"Ingrese los apellidos",
                        datos:"Campo requerido",

                        asesor:"Campo requerido",





                    }
                });
                
///////////////// convertir a mayuscula   
 
                $('#firstname').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                $('#lastname').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                $('#apmat').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                $('#direccion').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                 $('#id_descripcion').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                 $('#nombre_papa').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                 $('#apellidos_p').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                 $('#Nombre_Razons').blur(function(){
                    this.value = this.value.toUpperCase();
                });
                 $('#apellidos_m').blur(function(){
                    this.value = this.value.toUpperCase();
                 });
                $('#rfc').blur(function(){
                    this.value = this.value.toUpperCase();
                 });

                  


                 
                
/////////////////  fin de convertir a mayuscula 
                
                 
                // propose username by combining first- and lastname
                
                //code to hide topic selection, disable for demo
                var newsletter = $("#newsletter");
                // newsletter topics are optional, hide at first
                var inital = newsletter.is(":checked");
                var topics = $("#newsletter_topics")[inital ? "removeClass" : "addClass"]("disable-topic");
                var topicInputs = topics.find("input").attr("disabled", !inital);
                // show when newsletter is checked
                newsletter.click(function () {
                    topics[this.checked ? "removeClass" : "addClass"]("disable-topic");
                    topicInputs.attr("disabled", !this.checked);
                });
            });

            $(function () {
                var container = $('div.error-container ');
                // validate the form when it is submitted
                var validator = $("#form2").validate({
                    errorContainer: container,
                    errorLabelContainer: $("ol", container),
                    wrapper: 'li',
                    meta: "validate"
                });
                $(".cancel").click(function () {
                    validator.resetForm();
                });
            });

//fin de validacion de formulaio del personal

//validacion de formulario del witget de cliente
            $(function () {
                /*==JQUERY STEPY==*/
                $('#stepy').stepy({
                    backLabel: 'Regresar',
                    nextLabel: 'Siguiente',
                    block: true,
                    description: true,
                    legend: false,
                    titleClick: true,
                    titleTarget: '#stepy_tabby'
                });
                $('#stepy1').stepy({
                    backLabel: 'Regresar',
                    nextLabel: 'Siguiente',
                    block: true,
                    description: true,
                    legend: false,
                    titleClick: true,
                    titleTarget: '#stepy_tabby1'
                });
                $('#stepy_form').stepy({
                    backLabel: 'Regresar',
                    nextLabel: 'Siguiente',
                    errorImage: true,
                    block: true,
                    description: true,
                    legend: false,
                    titleClick: true,
                    titleTarget: '#top_tabby',
                    validate: true
                });
                $('#stepy_form').validate({
                    errorPlacement: function (error, element) {
                        $('#stepy_form div.stepy-error').append(error);
                    },
                    rules: {                        
                        localidad:"required",
                        Nombre_Razons:"required",
                        rfc:"required",
                        first_name:"required",
                        last_name:"required",
                        apmat:"required",
                        username: {
                            required: true,
                            minlength: 5,
                            maxlength: 30,
                        },
                        
                        telefono: {
                            maxlength: 10,
                            minlength: 10,
                            digits: true
                        },
                        codigo_postal: {
                            maxlength: 7,
                            minlength: 5,
                            digits: true
                        },
                        celular: {
                            maxlength: 10,
                            minlength: 10,
                            digits: true
                        },
                        password: {
                            required: true,
                            minlength: 5
                        },
                        confirm_password: {
                            required: true,
                            minlength: 5,
                            equalTo: "#password"
                        },
                        email: {
                            required: true,
                            email: true
                        },
                        topic: {
                            required: "#newsletter:checked",
                            minlength: 1
                        },
                        


                        telefono_p: {
                            
                            maxlength: 10,
                            minlength: 10,
                        },
                        email_p: {
                            email: true
                        },

                        
                        telefono_m: {
                            maxlength: 10,
                            minlength: 10,
                        },
                        email_m: {
                            email: true
                        },
                        pais:"required",
                        estado:"required",

                    },
                    messages: {
                        first_name: "Por favor, escribe el nombre",
                        last_name: "Por favor, escribe los apellidos",
                        id_tipo_usuario:"Por favor, seleccione el tipo de usuario",
                        Nombre_Razons:"Por favor, escribe la razon social",
                        rfc:"Por favor, escribe el RFC",
                        localidad:"Por favor, seleccione la localidad",
                        escuela:"Por favor, seleccione la escuela",
                        nacionalidad:"Por favor, seleccione el puesto",
                        fecha_nacimiento:"Por favor, ingrese su la fecha de nacimineto",
                        telefono:{
                            required: "Ingrese el numero de Telefono",
                            maxlength: "Maximo 10 dígitos",
                            minlength: "Minimo 10 dígitos",
                            digits: "Por favor use sólamente dígitos.",
                        },
                        codigo_postal:{
                            required: "Ingrese el código postal",
                            maxlength: "Maximo 7 dígitos",
                            minlength: "Minimo 5 dígitos",
                            digits: "Por favor use sólamente dígitos.",
                        },
                        celular:{
                            required: "Ingrese el numero de celular",
                            maxlength: "Maximo 10 dígitos",
                            minlength: "Minimo 10 dígitos",
                            digits: "Por favor use sólamente dígitos.",
                        },
                        username: {
                            required: "Por favor, escribe el nombre de usuario(Nesesario para entrar al sistema)",
                            minlength: "Your username must consist of at least 5 characters"
                        },
                        password: {
                            required: "Por favor, ingrese la contraseña",
                            minlength: "LA contraseña debe tener al menos 5 caracteres"
                        },
                        confirm_password: {
                            required: "Por favor, ingrese la contraseña",
                            minlength: "La contraseña debe tener al menos 5 caracteres",
                            equalTo: "Por favor, introduzca la misma contraseña que el anterior"
                        },
                        email: "Por favor, introduzca una dirección e-mail válida",
                        agree: "Por favor, acepte nuestra política de privacidad",

                        nombre: "Ingrese el nombre",
                        talla: "Por favor, ingrese su talla",
                        personalidad: "Por favor, seleccione su personalidad",
                        sabe_nadar: "Por favor, seleccione si sabe nadar",
                        viaja_con: "Por favor, seleccione ¿con quien viaja?",
                        fuente: "Por favor, seleccione ¿Como se etero de nuestros programas?",
                        fiesta: "Por favor, seleccione ¿Si asiste a fiesta?",


                        pais:"Seleccion el pais por favor",
                        estado:"Seleccion el Estado por favor",
                        discapacidad_fm:"Campo requerido",
                        desorden_pns:"Campo requerido",
                        restriccion_aliment:"Campo requerido",
                        padecimiento_aler:"Campo requerido",
                        restriccion_acde:"Campo requerido",
                        medicamento_dv:"Campo requerido",
                        cirugia_accidente:"Campo requerido",



                        nombre_papa:"Campo requerido",
                        apellidos_p:"Campo requerido",
                        telefono_p: {
                            required: "Ingrese el numero de Telefono",
                            maxlength: "Maximo 10 dígitos",
                            minlength: "Minimo 10 dígitos",
                            digits: "Por favor use sólamente dígitos."
                        },
                        email_p: {
                            required: "Campo requerido",
                            email: "Por favor, introduzca una dirección e-mail válida"
                        },

                        nombre_mama:"Campo requerido",
                        apellidos_m:"Campo requerido",
                        telefono_m: {
                            required: "Ingrese el numero de Telefono",
                            maxlength: "Maximo 10 dígitos",
                            minlength: "Minimo 10 dígitos",
                            digits: "Por favor use sólamente dígitos."
                        },
                        email_m: {
                            required: "Campo requerido",
                            email: "Por favor, introduzca una dirección e-mail válida"
                        },


                        
                    }
                });
            });
               

// fin de validacion de formulario de wiget de cliente

//estados municipios con ajax
$(document).ready(function() {
$('#pais').change(function(event){ //id del select
        $.post("/buscar_estados/", {id_pais:$('#pais').val()}, //nombre de la vista  + id del select
            function(data){
           
            var options = '<option value="">--Selecciona el estado--</option>';
            for (var i = 0; i < data.length; i++)
            {
                options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["nombre"] +'</option>'
            }
            $('#estado').html(options); //nombre del slect donde se va a mostrar
            $("#estado option:first").attr('selected', 'selected');
        }, "json");
    });
});

$(document).ready(function() {
$('#estado').change(function(event){ //id del select
        $.post("/buscar_municipios/", {id_estado:$('#estado').val()}, //nombre de la vista  + id del select
            function(data){
           
            var options = '<option value="">--Selecciona el municipio--</option>';
            for (var i = 0; i < data.length; i++)
            {
                options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["nombre"] +'</option>'
            }
            $('#id_municipios').html(options); //nombre del slect donde se va a mostrar
            $("#id_municipios option:first").attr('selected', 'selected');
        }, "json");
    });
});
//fin de estados municipios con ajax

//busqueda de pais cliente con ajax
$(document).ready(function() {
$('#paisc').change(function(event){ //id del select
        $.post("/buscar_estados/", {id_pais:$('#paisc').val()}, //nombre de la vista  + id del select
            function(data){
           
            var options = '<option value="">--Selecciona el estado--</option>';
            for (var i = 0; i < data.length; i++)
            {
                options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["nombre"] +'</option>'
            }
            $('#estadoc').html(options); //nombre del slect donde se va a mostrar
            $("#estadoc option:first").attr('selected', 'selected');
        }, "json");
    });
});
//fin de busqueda de precios con ajax

$(document).ready(function() {
$('#estadoc').change(function(event){ //id del select
        $.post("/buscar_municipios/", {id_estado:$('#estadoc').val()}, //nombre de la vista  + id del select
            function(data){
           
            var options = '<option value="">--Selecciona el municipio--</option>';
            for (var i = 0; i < data.length; i++)
            {
                options += '<option value="'+data[i]["pk"]+'">' +data[i]["fields"]["nombre"] +'</option>'
            }
            $('#id_municipiosc').html(options); //nombre del slect donde se va a mostrar
            $("#id_municipiosc option:first").attr('selected', 'selected');
        }, "json");
    });
});
//fin de estados municipios con ajax

 //busqueda de correo electronico con ajax
$(document).ready(function() {

      $("#rfc").keyup(function(event){

        if (($("#rfc").val().length) > 4){

            $.post("/rfc-jax/",{q:$('#rfc').val()},
               
                function(data) {
                    var options =data[0];
                    if (options == 0){
                        var aviso ="Este RFC Está Disponible";
                        $('#results').html(aviso);
                        $('#btnguardar').show()

                      }
                      if (options == 1){
                        var aviso ="Este RFC No Está Disponible";
                        $('#results').html(aviso);
                        $('#btnguardar').hide()
                      }
                } 
            );      
        }  
      });
   });
//fin busqueda de correo electronico con ajax
//busqueda de nombre de usuario con ajax
  $(document).ready(function() {
      $("#username").keyup(function(event){
        if (($("#username").val().length) > 4){
            $.post( 
                "/demo_user_search/",
                {q:$('#username').val()}, 
                function(data) {
                    var options =data[0];
                    if (options == 0){
                        var aviso ="Este Nombre de Usuario Está Disponible";
                        $('#results').html(aviso);
                        $('#btnguardar').show()

                      }
                      if (options == 1){
                        var aviso ="Este Nombre de Usuario No Está Disponible";
                        $('#results').html(aviso);
                        $('#btnguardar').hide()
                      }
                } 
            );      
        }  
      });
   });
 //fin de busqueda de nombre de usuario con ajax

//imagen de fondo spinner
 $( document ).ajaxStart( function() {
        $( '#spinner' ).show();
    }).ajaxStop( function() {
        $( '#spinner' ).hide();
    });
//fin de imagen de fondo spinner

//unidad de negocio con generador de clave para el asesor

$(document).ready(function() {
$('#unidadnegocio').hide();
$('#id_tipo_usuario').change(function(event){
    var v = $("#id_tipo_usuario").val();
    if (v==3)
    {

        $('#unidadnegocio').show(); 
                   
    }
    else
        {
            $('#unidadnegocio').hide();
            $('#divclave').hide();
        }
    });
});

$(document).ready(function() {
$('#unidadnegocio').hide();
$('#tipo_u').change(function(event){
    var v = $("#tipo_u").val();
    if (v==3)
    {

        $('#unidadnegocio').show(); 
                   
    }
    else
        {
            $('#unidadnegocio').hide();
            $('#divclave').hide();
        }
    });
});


$(document).ready(function() {
$('#datosfiscales').hide();
$('#solifactura').change(function(event){
    var v = $("#solifactura").val();
    if (v=="Si")
    {

        $('#datosfiscales').show(); 
                   
    }
    else
        {
            $('#datosfiscales').hide();
        }
    });
});



$(document).ready(function() {
$('#divclave').hide();
$('#unidadnego').change(function(event){
    var v = $("#unidadnego").val();
    if (v!=0){

                    $('#divclave').show(); 
                    var firstname1 = $("#firstname").val().charAt(0);
                    var firstname2 = $("#firstname").val().charAt(1);
                    var firstname3 = $("#firstname").val().charAt(2);

                    var lastname = ($("#lastname").val()).charAt(0);

                var nuevo= (v + "-"+ firstname1+ firstname2 +firstname3 +lastname).toUpperCase();
                $("#clave").val(nuevo);
    }
    else
                {
                    $('#divclave').hide();
                }
    });
});
//fin de unidad de negocio con generador de clave para el asesor
//validacion de los campo que solo acepte numeros o letras
$(function(){
                //Para escribir solo letras
                $('#firstname').validCampo(' abcdefghijklmnñopqrstuvwxyzáéiou');
                $('#lastname').validCampo(' abcdefghijklmnñopqrstuvwxyzáéiou');

                //Para escribir solo numeros    
                $('#telefono').validCampo('0123456789');
                $('#celular').validCampo('0123456789');

                $('#comision').validCampo('0123456789');
                $('#cve_banco').validCampo('0123456789');
                
                $('#codigo_postal').validCampo('0123456789');


                
                
});

$(function () {
                $(".chzn-select").chosen();
                $(".chzn-select-deselect").chosen({
                allow_single_deselect: true
                });
});


//scrip para mostrar o ocultar div en los formularios

$(document).ready(function(){
 
    $(".slidingDiv").hide();

    $('.show_hide').click(function(){

        if($("#show_hide").is(':checked')) {  
            $(".slidingDiv").show(); 
            $(".slidingDiv2").hide();
        } else {  
            $(".slidingDiv").hide();
            $(".slidingDiv2").show(); 
        }  
    });
});

$(document).ready(function(){
 
    $("#divp1").show();
    $("#divc1").hide();
    $("#divo1").hide();

    $('#p1').click(function(){

        $("#divp1").show();
        $("#divc1").hide();
        $("#divo1").hide();
    });
    $('#c1').click(function(){

        $("#divp1").hide();
        $("#divc1").show();
        $("#divo1").hide();
    });
    $('#o1').click(function(){

        $("#divp1").hide();
        $("#divc1").hide();
        $("#divo1").show();
    });
});

$(document).ready(function(){
 
    $("#divp2").show();
    $("#divc2").hide();
    $("#divo2").hide();

    $('#p2').click(function(){

        $("#divp2").show();
        $("#divc2").hide();
        $("#divo2").hide();
    });
    $('#c2').click(function(){

        $("#divp2").hide();
        $("#divc2").show();
        $("#divo2").hide();
    });
    $('#o2').click(function(){

        $("#divp2").hide();
        $("#divc2").hide();
        $("#divo2").show();
    });
});

$(document).ready(function(){
        if ($("#p1").is(":checked")) {
            $("#divp1").show();
            $("#divc1").hide();
            $("#divo1").hide();
        }
        if ($("#c1").is(":checked")) {
            $("#divp1").hide();
            $("#divc1").show();
            $("#divo1").hide();
        }
        if ($("#o1").is(":checked")) {
            $("#divp1").hide();
            $("#divc1").hide();
            $("#divo1").show();
        }
        if ($("#p2").is(":checked")) {
            $("#divp2").show();
            $("#divc2").hide();
            $("#divo2").hide();
        }
        if ($("#c2").is(":checked")) {
            $("#divp2").hide();
            $("#divc2").show();
            $("#divo2").hide();
        }
        if ($("#o2").is(":checked")) {
            $("#divp2").hide();
            $("#divc2").hide();
            $("#divo2").show();
        }

    });

 $(document).ready(function () {
        $('#content').hide();
        $('#m1').hide();
        $('#m2').hide();
       
        $('#id_status_0').click(function () {
          $('#content').show();
          $('#m1').show();
          $('#m2').hide();
         });
        $('#id_status_1').click(function () {
          $('#content').show();
           $('#m2').show();
            $('#m1').hide();
         });

        $('#id_status_2').click(function () {
          $('#content').hide();
          $('#m1').hide();
          $('#m2').hide();
         });
        $('#id_status_3').click(function () {
          $('#content').hide();
          $('#m1').hide();
          $('#m2').hide();
         });
        $('#id_status_4').click(function () {
          $('#content').hide();
          $('#m1').hide();
          $('#m2').hide();
         });
        $('#id_status_5').click(function () {
          $('#content').hide();
          $('#m1').hide();
          $('#m2').hide();
         });

        });

//fin del scrip para mostrar o ocultar div en los formularios

$(document).ready(function(){
 
    $("#divnino").hide();
    $("#divnina").hide();

    $('#nino').click(function(){

        $("#divnino").slideToggle();
    });
    $('#nina').click(function(){

        $("#divnina").slideToggle();
    });
});

$(document).ready(function(){
 
    $("#divpersonal").show();
    $("#divchaperon").hide();

    

    $('#id_status1').click(function(){
        if($("#id_status1").is(':checked')){ 

            $("#divpersonal").show();
            $("#divchaperon").hide();

        }else{
            $("#divpersonal").hide();
            $("#divchaperon").show();
        }

         
    });
});

$(document).ready(function(){
 $("#username").focus(function () {
                    var vrfc = $("#rfc").val();
                    $("#username").val(vrfc);
                    
                });

 $("#direccionp").focus(function () {
                    var paiss = $("#pais").find('option:selected');
                    var paisv = $(paiss).text();


                    var estados = $("#estado").find('option:selected');
                    var estadosv = $(estados).text();

                    var muni = $("#id_municipios").find('option:selected');
                    var muniv = $(muni).text();

                    var direccion = $("#direccion").val();

                    var direccionpapa = paisv +", "+ estadosv +", "+ muniv +", "+ direccion;
                    $("#direccionp").val(direccionpapa);
                    
                });
});

$(document).ready(function(){
$('#stepy_form-next-0').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });

$('#stepy_form-next-1').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });

$('#stepy_form-next-2').click(function(){
            $("html, body").animate({ scrollTop: 0 }, 600);
            return false;
        });

});

