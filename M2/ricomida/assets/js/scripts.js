new Splide(".splide", {
    type: "loop",
    gap: "1rem",
    perPage: 4,
    breakpoints: {
      576: {
        destroy: true,
      },
      768: {
        perPage: 3,
      },
    },
  }).mount();
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );

$('#enviarCorreo').on('click', function(){
    alert('El correo fue enviado correctamente...');
});

$('.change_color').on('dblclick', function(){
    $(this).toggleClass( "use_red" )
});

$('h4.card-title').on('click', function(){
    // Puede que el selector no sea tan especifico
    $(".card-text").toggleClass( "invisible" )
});