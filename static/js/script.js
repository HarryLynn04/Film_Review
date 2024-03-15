

function formatText(command) {
    var textArea = document.getElementById('id_Description');
    var start = textArea.selectionStart;
    var end = textArea.selectionEnd;
    var text = textArea.value;
    var tag = '';

    switch (command) {
        case 'bold':
            tag = 'b';
            break;
        case 'italic':
            tag = 'i';
            break;
        case 'underline':
            tag = 'u';
            break;

        case 'spoiler':
            tagOpen = "<span class='spoiler' onclick='toggleSpoiler(this)' style='background-color: black; color: black; cursor: pointer;'>";
            tagClose = "</span>";
            break;
        // Add more cases as needed
    }

    var beforeText = text.substring(0, start);
    var selectedText = text.substring(start, end);
    var afterText = text.substring(end);
    var tagOpen = '<' + tag + '>';
    var tagClose = '</' + tag + '>';

    textArea.value = beforeText + tagOpen + selectedText + tagClose + afterText;

    // Adjust cursor position to after the closing tag
    var newPos = start + tagOpen.length + selectedText.length + tagClose.length;
    textArea.setSelectionRange(newPos, newPos);
}

function displayFormattedReview() {
    var textArea = document.getElementById('id_Description');
    var formattedTextDiv = document.getElementById('formattedText');

    // Convert newline characters to <br> tags for proper HTML rendering
    var htmlContent = textArea.value.replace(/\n/g, '<br>');

    // Set the innerHTML of the display element to interpret the HTML tags
    formattedTextDiv.innerHTML = htmlContent;
}


function toggleSpoiler(element) {
    if (element.style.color === "black") {
        element.style.color = "white"; // Makes the text visible against a black background
    } else {
        element.style.color = "black"; // Hides the text again
    }
}
