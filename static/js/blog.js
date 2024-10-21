

    document.addEventListener('DOMContentLoaded', function () {
        const likeButtons = document.querySelectorAll('.toggle-like');
        likeButtons.forEach(button => {
            button.addEventListener('click', function () {
                const likeIcon = this.querySelector('.like-icon');
                if (likeIcon.src.includes('heart-e.png')) {
                    likeIcon.src = "{% static 'images/heart-red1.png' %}";
                    // Add code here to handle like action, e.g., send AJAX request to server
                } else {
                    likeIcon.src = "{% static 'images/heart-e.png' %}";
                    // Add code here to handle unlike action, e.g., send AJAX request to server
                }
            });
        });
    });