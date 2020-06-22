var login = document.getElementById('tituloLogin');
var texto_login = "print('Faça seu login!')";

function escrever(str, el) {
    el.innerHTML = '>>> '
    var char = str.split('').reverse();
    var typer = setInterval(function() {
        if (!char.length) return clearInterval(typer);
        var next = char.pop();
        el.innerHTML += next;
    }, 100);
}

escrever(texto_login, login);s
