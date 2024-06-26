const links = document.querySelectorAll('.headers-link');   
if (links.length) {
  links.forEach((link) => {
    link.addEventListener('click', (e) => {
      links.forEach((link) => {
          link.classList.remove('active');
      });
      e.preventDefault();
      link.classList.add('active');
    });
  });
}
$(".navbar-toggler").click(function(){
  $(".slide-out-menu").toggle();
});
// Prevent closing from click inside dropdown
$(document).on('click', '.dropdown-menu', function (e) {
  e.stopPropagation();
});

// make it as accordion for smaller screens
if ($(window).width() < 992) {
  $('.dropdown-menu a').click(function(e){
    e.preventDefault();
      if($(this).next('.submenu').length){
        $(this).next('.submenu').toggle();
      }
      $('.dropdown').on('hide.bs.dropdown', function () {
     $(this).find('.submenu').hide();
  })
  });
}

// show drop down mobile menu
function myFunctiony() {
  $(".library-dropsdown1").toggle();
}
function AllProductFunctiony() {
  $(".all-products1").toggle();
}
function libraryFunction() {
  $(".library-dropsdowns1").toggle();
}
function subFunction() {
  $(".submenu-navs1").toggle();
}
