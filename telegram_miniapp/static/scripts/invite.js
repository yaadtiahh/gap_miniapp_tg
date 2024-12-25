document.addEventListener('DOMContentLoaded', function () {
  // Проверяем доступность объекта Telegram WebApp API
  const tg = window.Telegram.WebApp;

  if (!tg) {
    console.error('Telegram WebApp API недоступен.');
    return;
  }

  // Получаем элемент кнопки
  const shareButton = document.getElementById('shareButton');
  if (!shareButton) {
    console.error('Кнопка с id="shareButton" не найдена.');
    return;
  }

  // Добавляем обработчик события
  shareButton.addEventListener('click', function () {
    tg.shareLink(
      'https://example.com', // Ссылка, которой вы хотите поделиться
      'Посмотри на это приложение!' // Дополнительное сообщение
    ).catch((error) => {
      console.error('Ошибка при вызове tg.shareLink:', error);
    });
  });
});