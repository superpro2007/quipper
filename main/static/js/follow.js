$(".follow").click(function () {
  var userid;
  userid = $(this).attr("userid");
  var path;
  path = "/user/" + userid + "/follow";
  $.get(path, function (is_following) {
    var buttonid;
    buttonid = "#follow_" + userid;
    if (is_following == "True") {
      $(buttonid).html("Unfollow");
    } else {
      $(buttonid).html("Follow");
    }
  });
});
