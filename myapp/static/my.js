$(document).ready(function () {
    $(".deletepolicy").click(function () {
		var deleteurl = $(this).data('url');
		$("#delete_pol").data('url', deleteurl);
	});

	$("#policy_delete_continue").click(function () {

		var deleteurl = $("#delete_pol").data('url');
		$.ajax({
			url: deleteurl,
			type: "DELETE",
			contentType: false,
			processData: false,
			success: function (res) {
				location.reload();
			},
		});
	});
});