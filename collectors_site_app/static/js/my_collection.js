$('.collection-imgs').click(function(){
    let src = $(this).attr("src");
    let alt = $(this).attr("alt");
    let postId = $(this).attr("data-id");
    $(".modal").addClass("is-active");
    $('#show-img').attr('src', src);
    $('#description').text(alt);
    $('#modalLink').attr('href', `/view_post/${postId}`)
});

$(".modal-close").click(function() {
    $(".modal").removeClass("is-active");
 });