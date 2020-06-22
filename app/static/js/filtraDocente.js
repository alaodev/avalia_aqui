var inputFiltro = document.querySelector("#inputFiltro");

inputFiltro.addEventListener("input", function() {
    var docentes = document.querySelectorAll("#docente");
    if(this.value.length > 0) {
        docentes.forEach(docente => {
            var d = docente;
            var nomeDocente = d.querySelector("#nomeDocente");
            var nome = nomeDocente.textContent;
            var expressao = new RegExp(this.value, "i");
            nome = nome.trim();
            if(!expressao.test(nome)) {
                docente.classList.add("inv");
            }else {
                docente.classList.remove("inv");
            }
        });
    }else {
        docentes.forEach(docente => {
            docente.classList.remove("inv");
        });
    }
});