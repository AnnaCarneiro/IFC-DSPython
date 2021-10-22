$(function () { // quando o documento estiver pronto/carregado

    $.ajax({
        url: 'http://localhost:5000/listar_turmadamonica',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(turmadamonica) {
        // percorrer a lista de turma da Monica; 
        for (var i in turmadamonica) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da turminha
                '<td>' + turmadamonica[i].nome + '</td>' +
                '<td>' + turmadamonica[i].idade + '</td>' +
                '<td>' + turmadamonica[i].altura + '</td>' +
                '<td>' + turmadamonica[i].especialidade + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaTurmaDaMonica').append(lin);
        }
    }

});