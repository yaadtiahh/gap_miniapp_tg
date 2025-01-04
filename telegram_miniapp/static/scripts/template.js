// // Инициализация Telegram WebApp
// window.Telegram.WebApp.ready();

// // Получаем данные пользователя
// const user = window.Telegram.WebApp.initDataUnsafe?.user;

// // Проверяем наличие данных
// if (user) {
//     const nickname = user.username || `${user.first_name || ""} ${user.last_name || ""}`.trim();
//     document.getElementById("username").textContent = `${nickname || "Guest"}`;
// } else {
//     console.error("Данные пользователя отсутствуют.");
//     document.getElementById("username").textContent = "Guest";
// }