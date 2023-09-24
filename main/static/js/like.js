$(".like").click(function () {
  var postid;
  postid = $(this).attr("postid");
  var path;
  path = "/quip/" + postid + "/like";
  $.get(path, function (likes_amount) {
    var buttonid;
    buttonid = "#quip_" + postid;
    if (likes_amount == 0) {
      $(buttonid).html("🤍 Like");
    } else {
      $(buttonid).html("❤️ " + likes_amount);
    }
  });
});
