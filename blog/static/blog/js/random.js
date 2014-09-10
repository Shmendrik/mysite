$(function() {
	var offset = $("#fixed").offset();
	var topPadding = 15;
	$(window).scroll(function() {
		if ($(window).scrollTop() > offset.top) {
			$("#fixed").stop().animate({marginTop: $(window).scrollTop() - offset.top + topPadding});
		}
		else {$("#fixed").stop().animate({marginTop: 0});};});
	});
