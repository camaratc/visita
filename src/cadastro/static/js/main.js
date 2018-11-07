// Inicializar o Select do Materialize

$(document).ready(() => {
    $('select').formSelect();
    $(".dropdown-trigger").dropdown({
        inDuration: 300,
        outDuration: 225,
        constrain_width: false,
        hover: true,
        gutter: ($('.dropdown-content').width()*3)/2.5 + 5,
        coverTrigger: false,
        belowOrigin: false,
        alignment: 'left'
    });
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

        let found = false;

        if(searchField.length !== 0){
            document.getElementById('itensBusca').innerHTML = '<ul id="result" class="lista-results"></ul>';
        }
        else{
            document.getElementById('itensBusca').innerHTML = '';
        }

        $.getJSON('http://sispor/api/pessoas/', (data) => {
            let count = 0;

            $.each(data, (key, value) => {
                if(count == 5){
                    return false;
                }

                if(value.fields.nome.search(expression) != -1 || value.fields.cpf.search(expression) != -1){
                    if(count === 0){
                        $('#result').append(`<li value='${ value.pk }' onClick='selecionarVisitante(this);'><div class='firstItem'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                        found = true;
                    }
                    else{
                        $('#result').append(`<li value='${ value.pk }' onClick='selecionarVisitante(this);'><div class='itemListaBusca'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                    }

                    count++;
                }
            });

            if(!found){
                $('#result').append(`<li onClick='fecharBox();'><div class='firstItem'>Nenhum registro encontrado.</div></li>`);
            }
        });
    });
});

function selecionarVisitante(elem){
    document.getElementById('itensBusca').innerHTML = '';
    document.getElementById('id_pessoa').value = elem.value;
    document.getElementById('search').value = elem.textContent;
}

function fecharBox(){
    document.getElementById('itensBusca').innerHTML = '';
    document.getElementById('search').value = '';
}

$(document).ready(() => {
    $('#search-visitantes').keyup(() => {
        $('#result').html('');

        let searchField = $('#search-visitantes').val();
        let expression = new RegExp(searchField, "i");

        let found = false;

        if(searchField.length !== 0){
            document.getElementById('visitantes-busca').innerHTML = '<ul id="result" class="lista-results"></ul>';
        }
        else{
            document.getElementById('visitante-busca').innerHTML = '';
        }

        $.getJSON('http://sispor/api/pessoas/', (data) => {
            let count = 0;

            $.each(data, (key, value) => {
                if(count == 5){
                    return false;
                }

                if(value.fields.nome.search(expression) != -1 || value.fields.cpf.search(expression) != -1){
                    if(count === 0){
                        $('#result').append(`<li value='${ value.pk }' onClick='editarVisitante(this);'><div class='firstItem'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                        found = true;
                    }
                    else{
                        $('#result').append(`<li value='${ value.pk }' onClick='editarVisitante(this);'><div class='itemListaBusca'>${ value.fields.nome } (${ value.fields.cpf })</div></li>`);
                    }

                    count++;
                }
            });

            if(!found){
                $('#result').append(`<li onClick='fecharBoxVisitante();'><div class='firstItem'>Nenhum registro encontrado.</div></li>`);
            }
        });
    });
});

function editarVisitante(item){
    window.location=`/visitante/${item.value}`;
}

function fecharBoxVisitante(){
    document.getElementById('visitantes-busca').innerHTML = '';
    document.getElementById('search-visitantes').value = '';
}
