

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
        
    }

    var beforeText = text.substring(0, start);
    var selectedText = text.substring(start, end);
    var afterText = text.substring(end);
    var tagOpen = '<' + tag + '>';
    var tagClose = '</' + tag + '>';

    textArea.value = beforeText + tagOpen + selectedText + tagClose + afterText;

    var newPos = start + tagOpen.length + selectedText.length + tagClose.length;
    textArea.setSelectionRange(newPos, newPos);
}

function displayFormattedReview() {
    var textArea = document.getElementById('id_Description');
    var formattedTextDiv = document.getElementById('formattedText');
    var htmlContent = textArea.value.replace(/\n/g, '<br>');

    formattedTextDiv.innerHTML = htmlContent;
}


function toggleSpoiler(element) {
    if (element.style.color === "black") {
        element.style.color = "white"; 
    } else {
        element.style.color = "black"; 
    }
}