$(document).ready(function () {

    // Attach click event to "Generate Question" button
    $("#generateButton").click(function () {
        askQuestion();
    });

});



function askQuestion() {

    $('#generateButton').addClass("is-loading");
    var userInput = $("#userInput").val();

    // Make an AJAX request to the Flask backend
    $.ajax({
        type: 'POST',
        url: '/ask-chatgpt',
        contentType: 'application/json',
        data: JSON.stringify({ user_input: userInput }),
        success: function (response) {

            console.log(response); // Log the entire response in the browser

            $("#answer-container").append(response);

            $('#generateButton').removeClass("is-loading");

        },
        error: function (error) {
            console.error("Error: ", error);
        }
    });
}

