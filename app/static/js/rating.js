var nota11 = document.getElementById("nota11");
var nota12 = document.getElementById("nota12");
var nota13 = document.getElementById("nota13");
var nota14 = document.getElementById("nota14");
var nota15 = document.getElementById("nota15");

var nota21 = document.getElementById("nota21");
var nota22 = document.getElementById("nota22");
var nota23 = document.getElementById("nota23");
var nota24 = document.getElementById("nota24");
var nota25 = document.getElementById("nota25");

var nota31 = document.getElementById("nota31");
var nota32 = document.getElementById("nota32");
var nota33 = document.getElementById("nota33");
var nota34 = document.getElementById("nota34");
var nota35 = document.getElementById("nota35");

var nota41 = document.getElementById("nota41");
var nota42 = document.getElementById("nota42");
var nota43 = document.getElementById("nota43");
var nota44 = document.getElementById("nota44");
var nota45 = document.getElementById("nota45");

var nota51 = document.getElementById("nota51");
var nota52 = document.getElementById("nota52");
var nota53 = document.getElementById("nota53");
var nota54 = document.getElementById("nota54");
var nota55 = document.getElementById("nota55");

var nota1 = document.getElementById("nota1");
var nota2 = document.getElementById("nota2");
var nota3 = document.getElementById("nota3");
var nota4 = document.getElementById("nota4");
var nota5 = document.getElementById("nota5");

// Nota 1.

nota11.addEventListener("click", function(){
    this.classList.remove("far"); // Desmarcada.
    this.classList.add("fas"); // Marcada.
    nota12.classList.remove("fas");
    nota12.classList.add("far");
    nota13.classList.remove("fas");
    nota13.classList.add("far");
    nota14.classList.remove("fas");
    nota14.classList.add("far");
    nota15.classList.remove("fas");
    nota15.classList.add("far");
    nota1.value = 1;
});

nota12.addEventListener("click", function(){
    nota11.classList.remove("far");
    nota11.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota13.classList.remove("fas");
    nota13.classList.add("far");
    nota14.classList.remove("fas");
    nota14.classList.add("far");
    nota15.classList.remove("fas");
    nota15.classList.add("far");
    nota1.value = 2;
});

nota13.addEventListener("click", function(){
    nota11.classList.remove("far");
    nota11.classList.add("fas");
    nota12.classList.remove("far");
    nota12.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota14.classList.remove("fas");
    nota14.classList.add("far");
    nota15.classList.remove("fas");
    nota15.classList.add("far");
    nota1.value = 3;
});

nota14.addEventListener("click", function(){
    nota11.classList.remove("far");
    nota11.classList.add("fas");
    nota12.classList.remove("far");
    nota12.classList.add("fas");
    nota13.classList.remove("far");
    nota13.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota15.classList.remove("fas");
    nota15.classList.add("far");
    nota1.value = 4;
});

nota15.addEventListener("click", function(){
    nota11.classList.remove("far");
    nota11.classList.add("fas");
    nota12.classList.remove("far");
    nota12.classList.add("fas");
    nota13.classList.remove("far");
    nota13.classList.add("fas");
    nota14.classList.remove("far");
    nota14.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota1.value = 5;
});

// Nota 2.

nota21.addEventListener("click", function(){
    this.classList.remove("far"); // Desmarcada.
    this.classList.add("fas"); // Marcada.
    nota22.classList.remove("fas");
    nota22.classList.add("far");
    nota23.classList.remove("fas");
    nota23.classList.add("far");
    nota24.classList.remove("fas");
    nota24.classList.add("far");
    nota25.classList.remove("fas");
    nota25.classList.add("far");
    nota2.value = 1;
});

nota22.addEventListener("click", function(){
    nota21.classList.remove("far");
    nota21.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota23.classList.remove("fas");
    nota23.classList.add("far");
    nota24.classList.remove("fas");
    nota24.classList.add("far");
    nota25.classList.remove("fas");
    nota25.classList.add("far");
    nota2.value = 2;
});

nota23.addEventListener("click", function(){
    nota21.classList.remove("far");
    nota21.classList.add("fas");
    nota22.classList.remove("far");
    nota22.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota24.classList.remove("fas");
    nota24.classList.add("far");
    nota25.classList.remove("fas");
    nota25.classList.add("far");
    nota2.value = 3;
});

nota24.addEventListener("click", function(){
    nota21.classList.remove("far");
    nota21.classList.add("fas");
    nota22.classList.remove("far");
    nota22.classList.add("fas");
    nota23.classList.remove("far");
    nota23.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota25.classList.remove("fas");
    nota25.classList.add("far");
    nota2.value = 4;
});

nota25.addEventListener("click", function(){
    nota21.classList.remove("far");
    nota21.classList.add("fas");
    nota22.classList.remove("far");
    nota22.classList.add("fas");
    nota23.classList.remove("far");
    nota23.classList.add("fas");
    nota24.classList.remove("far");
    nota24.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota2.value = 5;
});

// Nota 3.

nota31.addEventListener("click", function(){
    this.classList.remove("far"); // Desmarcada.
    this.classList.add("fas"); // Marcada.
    nota32.classList.remove("fas");
    nota32.classList.add("far");
    nota33.classList.remove("fas");
    nota33.classList.add("far");
    nota34.classList.remove("fas");
    nota34.classList.add("far");
    nota35.classList.remove("fas");
    nota35.classList.add("far");
    nota3.value = 1;
});

nota32.addEventListener("click", function(){
    nota31.classList.remove("far");
    nota31.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota33.classList.remove("fas");
    nota33.classList.add("far");
    nota34.classList.remove("fas");
    nota34.classList.add("far");
    nota35.classList.remove("fas");
    nota35.classList.add("far");
    nota3.value = 2;
});

nota33.addEventListener("click", function(){
    nota31.classList.remove("far");
    nota31.classList.add("fas");
    nota32.classList.remove("far");
    nota32.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota34.classList.remove("fas");
    nota34.classList.add("far");
    nota35.classList.remove("fas");
    nota35.classList.add("far");
    nota3.value = 3;
});

nota34.addEventListener("click", function(){
    nota31.classList.remove("far");
    nota31.classList.add("fas");
    nota32.classList.remove("far");
    nota32.classList.add("fas");
    nota33.classList.remove("far");
    nota33.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota35.classList.remove("fas");
    nota35.classList.add("far");
    nota3.value = 4;
});

nota35.addEventListener("click", function(){
    nota31.classList.remove("far");
    nota31.classList.add("fas");
    nota32.classList.remove("far");
    nota32.classList.add("fas");
    nota33.classList.remove("far");
    nota33.classList.add("fas");
    nota34.classList.remove("far");
    nota34.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota3.value = 5;
});

// Nota 4.

nota41.addEventListener("click", function(){
    this.classList.remove("far"); // Desmarcada.
    this.classList.add("fas"); // Marcada.
    nota42.classList.remove("fas");
    nota42.classList.add("far");
    nota43.classList.remove("fas");
    nota43.classList.add("far");
    nota44.classList.remove("fas");
    nota44.classList.add("far");
    nota45.classList.remove("fas");
    nota45.classList.add("far");
    nota4.value = 1;
});

nota42.addEventListener("click", function(){
    nota41.classList.remove("far");
    nota41.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota43.classList.remove("fas");
    nota43.classList.add("far");
    nota44.classList.remove("fas");
    nota44.classList.add("far");
    nota45.classList.remove("fas");
    nota45.classList.add("far");
    nota4.value = 2;
});

nota43.addEventListener("click", function(){
    nota41.classList.remove("far");
    nota41.classList.add("fas");
    nota42.classList.remove("far");
    nota42.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota44.classList.remove("fas");
    nota44.classList.add("far");
    nota45.classList.remove("fas");
    nota45.classList.add("far");
    nota4.value = 3;
});

nota44.addEventListener("click", function(){
    nota41.classList.remove("far");
    nota41.classList.add("fas");
    nota42.classList.remove("far");
    nota42.classList.add("fas");
    nota43.classList.remove("far");
    nota43.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota45.classList.remove("fas");
    nota45.classList.add("far");
    nota4.value = 4;
});

nota45.addEventListener("click", function(){
    nota41.classList.remove("far");
    nota41.classList.add("fas");
    nota42.classList.remove("far");
    nota42.classList.add("fas");
    nota43.classList.remove("far");
    nota43.classList.add("fas");
    nota44.classList.remove("far");
    nota44.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota4.value = 5;
});

// Nota 5.

nota51.addEventListener("click", function(){
    this.classList.remove("far"); // Desmarcada.
    this.classList.add("fas"); // Marcada.
    nota52.classList.remove("fas");
    nota52.classList.add("far");
    nota53.classList.remove("fas");
    nota53.classList.add("far");
    nota54.classList.remove("fas");
    nota54.classList.add("far");
    nota55.classList.remove("fas");
    nota55.classList.add("far");
    nota5.value = 1;
});

nota52.addEventListener("click", function(){
    nota51.classList.remove("far");
    nota51.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota53.classList.remove("fas");
    nota53.classList.add("far");
    nota54.classList.remove("fas");
    nota54.classList.add("far");
    nota55.classList.remove("fas");
    nota55.classList.add("far");
    nota5.value = 2;
});

nota53.addEventListener("click", function(){
    nota51.classList.remove("far");
    nota51.classList.add("fas");
    nota52.classList.remove("far");
    nota52.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota54.classList.remove("fas");
    nota54.classList.add("far");
    nota55.classList.remove("fas");
    nota55.classList.add("far");
    nota5.value = 3;
});

nota54.addEventListener("click", function(){
    nota51.classList.remove("far");
    nota51.classList.add("fas");
    nota52.classList.remove("far");
    nota52.classList.add("fas");
    nota53.classList.remove("far");
    nota53.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota55.classList.remove("fas");
    nota55.classList.add("far");
    nota5.value = 4;
});

nota55.addEventListener("click", function(){
    nota51.classList.remove("far");
    nota51.classList.add("fas");
    nota52.classList.remove("far");
    nota52.classList.add("fas");
    nota53.classList.remove("far");
    nota53.classList.add("fas");
    nota54.classList.remove("far");
    nota54.classList.add("fas");
    this.classList.remove("far");
    this.classList.add("fas");
    nota5.value = 5;
});