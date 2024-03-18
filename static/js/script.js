let myButtonContainer = document.querySelector(".btn_up"); // Target the container

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    myButtonContainer.style.display = "block"; // Show the container
    document.getElementById("myBtn").style.display = "block";
  } else {
    myButtonContainer.style.display = "none"; // Hide the container
    document.getElementById("myBtn").style.display = "none";
  }
}




// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
