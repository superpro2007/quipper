$(".like").click(function () {
  var postid;
  postid = $(this).attr("postid");
  var path;
  path = "/quip/" + postid + "/like";
  $.get(path, function (data) {
    var buttonid;
    buttonid = "#quip_" + postid;
    if (data == 0) {
      $(buttonid).html("🤍 Like");
    } else {
      $(buttonid).html("❤️ " + data);
    }
  });
});
