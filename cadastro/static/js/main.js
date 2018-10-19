// Inicializar o Select do Materialize

$(document).ready(() => {
    $('select').formSelect();
});

$(document).ready(() => { 
    let $cpf = $("#id_cpf");
    $cpf.mask('000.000.000-00', { reverse: false });
});

// AJAX para busca de visitantes

$(document).ready(() => {
    $('#search').keyup(() => {
        $('#result').html('');

        let searchField = $('#search').val();
        let expression = new RegExp(searchField, "i");

        $.getJSON('http://127.0.0.1:8000/api/pessoas/', (data) => {
            $.each(data, (key, value) => {
                if(value.fields.nome.search(expression) != -1 || value.fields.cpf.search(expression) != -1){
                    $('#result').append(`<li>${ value.fields.nome } - ${ value.fields.cpf }</li>`);
                }
            });
        });
    });
});