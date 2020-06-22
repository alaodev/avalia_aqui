var cadastro = document.getElementById('tituloCadastro');
var texto_cadastro = "print('Cadastre-se!')";

function escrever(str, el) {
    el.innerHTML = '>>> '
    var char = str.split('').reverse();
    var typer = setInterval(function() {
        if (!char.length) return clearInterval(typer);
        var next = char.pop();
        el.innerHTML += next;
    }, 100);
}

escrever(texto_cadastro, cadastro);
