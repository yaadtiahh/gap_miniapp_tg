const tg = window.Telegram.WebApp; // Инициализация Telegram WebApp

tg.ready(); // Убедитесь, что Telegram WebApp готов к работе

// Функция для обрезки ника
function truncateUsername(username) {
  if (username.length > 12) {
    return username.substring(0, 12) + '...';
  }
  return username;
}

// Получаем данные о пользователе
const user = tg.initDataUnsafe?.user;

if (user) {
  // Если данные пользователя доступны, выводим только ник без "@"
  const username = user.username ? `${user.username}` : `${user.first_name} ${user.last_name || ''}`;
  const truncatedUsername = truncateUsername(username); // Обрезаем ник, если нужно
  document.getElementById('tg-username').textContent = truncatedUsername;

  // Получаем аватарку пользователя
  const photoUrl = user.photo_url;

  // Если аватарка существует, устанавливаем ее
  if (photoUrl) {
    let avatarImage = document.getElementById('avatar');
    avatarImage.src = photoUrl;
  } else {
    console.log('Аватарка не установлена.');
  }
} else {
  // Если данных нет, выводим заглушку
  document.getElementById('tg-username').textContent = 'Неизвестный пользователь';
}