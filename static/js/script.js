
function formatText(command) {
    var textArea = document.getElementById('id_Description'); // Replace with the correct ID of your textarea
    var start = textArea.selectionStart;
    var end = textArea.selectionEnd;
    var selectedText = textArea.value.substring(start, end);
    
    var beforeText = textArea.value.substring(0, start);
    var afterText = textArea.value.substring(end);

    if (command === 'bold') {
        textArea.value = beforeText + '<strong>' + selectedText + '</strong>' + afterText;
    } else if (command === 'italic') {
        textArea.value = beforeText + '<em>' + selectedText + '</em>' + afterText;
    } else if (command === 'underline') {
        textArea.value = beforeText + '<u>' + selectedText + '</u>' + afterText;
    }

    textArea.selectionStart = start;
    textArea.selectionEnd = start + selectedText.length + 7; 
}


document.getElementById('descriptionTextarea').addEventListener('select', function(event) {
    var start = event.target.selectionStart;
    var end = event.target.selectionEnd;
    var selectedText = event.target.value.substring(start, end);

    console.log('Selected text:', selectedText);
});