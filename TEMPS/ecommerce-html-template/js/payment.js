$(function(){
  $(".sinif").keyup(function(e){
    var deger=$(this).val().length;
    if(e.keyCode == 8){//backspace başı
      $(this).css("background-color", "#bbbbff");
      if(deger==0){
        if(this.id=="b"){
        $("#a").focus();
          if($("#a").val().length==4)
            {
              $("#a").select();
            }
        $("#a").css("background-color", "#bbbbff");
       }
    else if(this.id=="c"){
        $("#b").focus();
      if($("#b").val().length==4)
            {
              $("#b").select();
            }
        $("#b").css("background-color", "#bbbbff");
       }
    else if(this.id=="d"){
        $("#c").focus();
      if($("#c").val().length==4)
            {
              $("#c").select();
            }
        $("#c").css("background-color", "#bbbbff");
       }
      }
    }//backspace sonu
    else{
  if(deger>3){
    if(this.id=="a"){
        $("#b").focus();
      if($("#b").val().length==4)
            {
              $("#b").select();
            }
       }
    else if(this.id=="b"){
        $("#c").focus();
      if($("#c").val().length==4)
            {
              $("#c").select();
            }
       }
    else if(this.id=="c"){
        $("#d").focus();
      if($("#d").val().length==4)
            {
              $("#d").select();
            }
       }
      $(this).css("background-color", "#bbffbb");
      $(this).next(".sinif").next().css("background-color", "#666666");
     }
    else if(deger.length<0){
      $("#sonuc").html("eksi");
    }
    else {
      $(this).css("background-color", "#ffbbbb");
      $("#sonuc").html("xxxx");
    }
    }
    var kartNo=$("#a").val()+$("#b").val()+$("#c").val()+$("#d").val();
    $("#sonuc").html(kartNo);
});
  });