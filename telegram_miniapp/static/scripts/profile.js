document.addEventListener('DOMContentLoaded', function () {
  const questItems = document.querySelectorAll('.quest-item');

  questItems.forEach(item => {
      item.addEventListener('click', function () {
          const questId = this.dataset.id;

          fetch(`/quests/complete/${questId}/`, {
              method: 'POST',
              headers: {
                  'X-CSRFToken': getCSRFToken(),
                  'Content-Type': 'application/json'
              },
          })
          .then(response => response.json())
          .then(data => {
              if (data.success) {
                  this.classList.add('completed');
                  setTimeout(() => {
                      this.style.display = 'none';
                  }, 2000);
              }
          });
      });
  });

  function getCSRFToken() {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.startsWith('csrftoken=')) {
              return cookie.substring('csrftoken='.length);
          }
      }
      return '';
  }
});