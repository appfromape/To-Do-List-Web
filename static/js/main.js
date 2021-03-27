$(document).ready(function(){

    $("ul").on("click", "li", function(){
    $(this).toggleClass("completed");
    });
    
    
    $("ul").on("click", "span", function(event){
    $(this).parent().fadeOut(500,function(){
        
        var search_word = $(this).text();
        var qurl="http://127.0.0.1:5000/delete";
        $.ajax({
            type: "POST",
            cache: false,
            data:{keyword:search_word},
            url: qurl,
            dataType: "json"
        })
    
    $(this).remove();
    });
    event.stopPropagation();
    });
    
    $("input[type='text']").keypress(function(event){
    if(event.which === 13){
    event.submit();
    var todoText = $(this).val();
    $(this).val("");
    $("ul").append("<li><span><i class='fa fa-trash'></i></span> " +todoText + "</li>")
    }
    });

    $(".fa-plus").click(function(){
    $("input[type='text']").fadeToggle();
    });
    
    });