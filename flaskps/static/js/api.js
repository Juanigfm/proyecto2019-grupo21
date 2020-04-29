

    // var misCabeceras = new Headers();

    // var miInit = { method: 'GET',
    //             headers: misCabeceras,
    //             mode: 'cors',
    //             cache: 'default' };

    $( document ).ready(function() {
        var localidades = document.querySelector('#contenido')
        var tiposDocumento = document.querySelector('#contenido')
        getTipoDocumento();
        getLocalidades();
    });

    function getTipoDocumento() {
        fetch('https://api-referencias.proyecto2019.linti.unlp.edu.ar/localidad')
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            // localidades.innerHTML = '<option value="0">Seleccione</option>'
            myJson.forEach(element => localidades.innerHTML = localidades.innerHTML + '<option value="'+element.id+'">'+element.nombre+'</option>');
        }).catch(function(error) {
            console.log('Hubo un problema con la petición Fetch:' + error.message);
        });
    } 
    
    function getLocalidades() {
        fetch('https://api-referencias.proyecto2019.linti.unlp.edu.ar/tipo-documento')
        .then(function(response) {
            return response.json();
        })
        .then(function(myJson) {
            // idSelected = document.getElementById('hiddenIdLocalidad').value;
            // tiposDocumento.innerHTML = '<option value="0">Seleccione</option>'
            // myJson.forEach(element => tiposDocumento.innerHTML = tiposDocumento.innerHTML + '<option value="'+element.id+' '+((String(element.id) == String(idSelected)) ? 'selected' : '')+'">'+element.nombre+'</option>');
            myJson.forEach(element => tiposDocumento.innerHTML = tiposDocumento.innerHTML + '<option value="'+element.id+'">'+element.nombre+'</option>');
        })
        .catch(function(error) {
            console.log('Hubo un problema con la petición Fetch:' + error.message);
        });
        console.log(tiposDocumento.innerHTML);
    } 
