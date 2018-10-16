// Inicializar o Select do Materialize

$(document).ready(() => {
    $('select').formSelect();
});

$(document).ready(() => { 
    let $cpf = $("#id_cpf");
    $cpf.mask('000.000.000-00', { reverse: false });
});

