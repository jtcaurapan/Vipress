var x;
x=$(document);
x.ready(Iniciar);


function Iniciar(){
  var menuBtn = $('.menu-icon');
      menuBtn.click(MobileMenu);


      var btn = $('.btnVerMas');
      btn.click(BtnVerMas);

      var btns = $('.btnSeminario');
      btns.click(IrSeminarios);

/*
      var btnRegister = $('.btnRegister');
      btnRegister.click(registro); */
}
function MobileMenu(){
  var   menu = $('.navigation ul');

  if (menu.hasClass('show')) {

    menu.removeClass('show');

  }else{
    menu.addClass('show');
  }
}


function BtnVerMas(){

  alert('Por ahora solo se pueden crear seminarios!')

}

function IrSeminarios(){

  return location.href="/seminario/nuevo";
}
