// fade out message alerts
function fade_alerts() {
  alerts = document.getElementsByClassName("alert msg");
  var i = alerts.length;
  for (let elem of alerts) {
    i--;
    time = 3250 + 1000 * i;
    setTimeout(function () {
      $(elem).fadeOut("slow");
    }, time);
  }
}

// call fade out after DOMContentLoaded
window.addEventListener("DOMContentLoaded", (event) => {
  fade_alerts();
});

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
