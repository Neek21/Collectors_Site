$('.collection-imgs').click(function(){
    let src = $(this).attr("src");
    $(".modal").addClass("is-active");
    $('#show-img').attr('src', src);
});

$(".modal-close").click(function() {
    $(".modal").removeClass("is-active");
 });