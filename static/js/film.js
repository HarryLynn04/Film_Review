$(document).ready(function() {
    $(".like-btn").each(function () {
        var reviewId = $(this).data("review-id");
        var likeButton = $(this);
        $.ajax({
            url: "{% url 'ReviewFlix:check_like_status' %}",
            type: "GET",
            data: {
                review_id: reviewId,
            },
            dataType: "json",
            success: function (response) {
                if (response.status === "success") {
                    if (response.liked) {
                        likeButton.text("Unlike");
                    } else {
                        likeButton.text("Like");
                    }
                } else {
                    console.error(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    $(".like-btn").click(function () {
        var reviewId = $(this).data("review-id");
        var likeButton = $(this);

        $.ajax({
            url: "{% url 'ReviewFlix:like_review' %}",
            type: "POST",
            data: {
                review_id: reviewId,
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },
            dataType: "json",
            success: function (response) {
                if (response.status === "success") {
                    var newLikes = response.new_likes;
                    $("#likes-count-" + reviewId).text(newLikes);
                    if (likeButton.text() === "Like") {
                        likeButton.text("Unlike");
                    } else {
                        likeButton.text("Like");
                    }
                } else {
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    var filmId = "{{ film.id }}";
    $.ajax({
        type: "GET",
        url: "/ReviewFlix/check_watchlist/",
        data: { film_id: filmId },
        success: function(response) {
            if (response.in_watchlist) {
                $("#watchlist-btn").val("Remove from Watchlist");
                $("#watchlist-form").attr("action", "{% url 'ReviewFlix:remove_from_watchlist' %}");
            } else {
                $("#watchlist-btn").val("Add to Watchlist");
                $("#watchlist-form").attr("action", "{% url 'ReviewFlix:add_to_watchlist' %}");
            }
        }
    });

    $("#watchlist-btn").click(function(e) {
        e.preventDefault();
        var form = $(this).closest("form");
        var action = form.attr("action");
        $.ajax({
            type: "POST",
            url: action,
            data: form.serialize(),
            success: function(response) {
                if ($("#watchlist-btn").val() === "Remove from Watchlist") {
                    $("#watchlist-btn").val("Add to Watchlist");
                    $("#watchlist-form").attr("action", "{% url 'ReviewFlix:add_to_watchlist' %}");
                } else {
                    $("#watchlist-btn").val("Remove from Watchlist");
                    $("#watchlist-form").attr("action", "{% url 'ReviewFlix:remove_from_watchlist' %}");
                }
            }
        });
    });
});