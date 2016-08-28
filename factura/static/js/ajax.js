/*____________________________________________________________________*/
function objetoAjax(){
        var xmlhttp=false;
        try {
                xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
                try {
                   xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
                } catch (E) {
                        xmlhttp = false;
                }
        }
        if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
                xmlhttp = new XMLHttpRequest();
        }
        return xmlhttp;
}
/*____________________________________________________________________*/
function ConsultaFiltrado(Pag,objId,objIdVacio){
	divVacios=document.getElementById(objIdVacio);
	if (document.formulario.q.value=="")
           {
            divVacios.innerHTML ="<div class='mensaje' align='justify'>Complete la 		informacion</div>"
          }
        else
        {
	divResultado = document.getElementById(objId);
	valor=document.formulario.q.value
      	 ajax=objetoAjax();
        	ajax.open("GET",Pag "?q=" valor);
        	ajax.onreadystatechange=function() {
             if (ajax.readyState==4) {
                        divResultado.innerHTML = ajax.responseText
                        divVacios.innerHTML =""
                }
        }
        ajax.send(null)
   }
}
/*____________________________________________________________________*/
