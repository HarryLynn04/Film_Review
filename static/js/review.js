document.addEventListener('DOMContentLoaded', function() {
    let starsContainer = document.getElementById('stars');
    for (let i = 1; i <= 5; i++) {
        let star = document.createElement('span');
        star.className = 'star';
        star.addEventListener('click', function() { ranking(i); });
        starsContainer.appendChild(star);
    }

    let stars = document.getElementsByClassName('star');
    let output = document.getElementById('output');

    // Function to update rating
    function ranking(n) {
        for (let i = 0; i < stars.length; i++) {
            stars[i].classList.remove('one', 'two', 'three', 'four', 'five');
            if (i < n) {
                let cls = '';
                if (n === 1) cls = 'one';
                else if (n === 2) cls = 'two';
                else if (n === 3) cls = 'three';
                else if (n === 4) cls = 'four';
                else if (n === 5) cls = 'five';
                stars[i].classList.add(cls);
            }
        }
        output.innerText = 'Rating is: ' + n + '/5';
    }
});
