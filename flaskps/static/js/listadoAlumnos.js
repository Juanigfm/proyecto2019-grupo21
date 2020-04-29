$(document).ready(function(){
	// Activate tooltip
	$('[data-toggle="tooltip"]').tooltip();

// 	// Select/Deselect checkboxes
// 	var checkbox = $('table tbody input[type="checkbox"]');
// 	$("#selectAll").click(function(){
// 		if(this.checked){
// 			checkbox.each(function(){
// 				this.checked = true;
// 			});
// 		} else{
// 			checkbox.each(function(){
// 				this.checked = false;
// 			});
// 		}
// 	});
// 	checkbox.click(function(){
// 		if(!this.checked){
// 			$("#selectAll").prop("checked", false);
// 		}
// 	});
// });
});
function borrarAlumno(e){
	// console.log(e.currentTarget.parentNode.parentNode.children[2].innerHTML);
	document.getElementById('hiddenAluId').value = e.currentTarget.parentNode.parentNode.children[2].innerHTML;
};
function borrarDocente(e){
	// console.log(e.currentTarget.parentNode.parentNode.children[2].innerHTML);
	document.getElementById('hiddenDocId').value = e.currentTarget.parentNode.parentNode.children[2].innerHTML;
};
function borrarUser(e){
	document.getElementById('hiddenEmailD').value = e.currentTarget.parentNode.parentNode.children[2].innerHTML;
};
function editarUser(e){
	document.getElementById('hiddenEmailU').value = e.currentTarget.parentNode.parentNode.children[2].innerHTML;
};
function stateUser(e){
	document.getElementById('hiddenEmailS').value = e.currentTarget.parentNode.parentNode.children[2].innerHTML;
};
function borrarUser2(e,id){
	document.getElementById('hiddenEmailD').value = id;
};
function borrarUser3(e,id,clid,doc_id){
	document.getElementById('idDocenteEliminar').value = id;
	document.getElementById('idCicloDocenteEliminar').value = clid;
	document.getElementById('idCiclo2DocenteEliminar').value = doc_id;
};
function borrarUser4(e,id,clid,doc_id){
	document.getElementById('idAlumnoEliminar').value = id;
	document.getElementById('idCicloAlumnoEliminar').value = clid;
	document.getElementById('idCiclo2AlumnoEliminar').value = doc_id;
};
function modUser(e,email){
	document.getElementById('emailMod').value = email;
	document.getElementById('formModificar').submit();
};
function detUser(e, val){
	document.getElementById('detMod').value = val;
	document.getElementById('formDetalle').submit();
};
function detUserDoc(e, val){
	document.getElementById('detModDoc').value = val;
	document.getElementById('formDetalleDoc').submit();
};

function detUserAlu(e, val){
	document.getElementById('detModAlumno').value = val;
	document.getElementById('formDetalleAlu').submit();
};

function borrarInstrumento(e){
	document.getElementById('hiddenAluId').value = e;
};
