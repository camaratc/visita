$(document).ready(function () {
    $.getJSON('https://raw.githubusercontent.com/camaratc/visitas/master/cadastro/static/js/estados_cidades.json', function (data) {
        var items = [];
        var options = '<option value="" selected disabled>Selecionar Estado</option>';

        $.each(data, function (key, val) {
            options += '<option value="' + val.sigla + '">' + val.nome + '</option>';
        });

        $("#id_estado").html(options);

        $("#id_estado").change(function () {
            var options_cidades = '<option value="" selected disabled>Selecionar Cidade</option>';
            var str = "";

            $("#id_estado option:selected").each(function () {
                str += $(this).text();
            });

            $.each(data, function (key, val) {
                if (val.nome == str) {
                    $.each(val.cidades, function (key_city, val_city) {
                        options_cidades += '<option value="' + val_city + '">' + val_city + '</option>';
                    });
                }
            });
            $("#id_cidade").html(options_cidades);

            $('select').formSelect();
        }).change();

    });
});