document.addEventListener('DOMContentLoaded', function() {
  let toggleButtons = document.querySelectorAll('.toggle-answer');

  toggleButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          let answer = this.parentElement.nextElementSibling;
          answer.classList.toggle('hidden');
      });
  });
});