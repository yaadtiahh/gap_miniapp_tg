// Проверяем, доступны ли данные пользователя
const user = window.Telegram.WebApp.initDataUnsafe?.user;

if (user) {
    // Если данные есть, показываем никнейм
    document.getElementById('username').innerText = user.username || 'Никнейм не указан';
} else {
    // Логируем ошибку, если данные недоступны
    console.error('Данные пользователя не получены');
}