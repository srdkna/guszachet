-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 12 2023 г., 12:14
-- Версия сервера: 5.7.39
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sklad`
--

-- --------------------------------------------------------

--
-- Структура таблицы `gruz`
--

CREATE TABLE `gruz` (
  `id_gruz` int(11) NOT NULL,
  `name` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `gruz`
--

INSERT INTO `gruz` (`id_gruz`, `name`) VALUES
(1, 'huawey');

-- --------------------------------------------------------

--
-- Структура таблицы `position`
--

CREATE TABLE `position` (
  `id_pos` int(11) NOT NULL,
  `id_gruz` int(11) DEFAULT NULL,
  `id_stelaj` int(11) NOT NULL,
  `number_yaceek` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `massa` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `position`
--

INSERT INTO `position` (`id_pos`, `id_gruz`, `id_stelaj`, `number_yaceek`, `massa`, `date`) VALUES
(1, 1, 1, '1', '100', '2023-04-11');

-- --------------------------------------------------------

--
-- Структура таблицы `stelaj`
--

CREATE TABLE `stelaj` (
  `id_stelaj` int(11) NOT NULL,
  `namber` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `kol_vo_yaceek` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dop_massa` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `stelaj`
--

INSERT INTO `stelaj` (`id_stelaj`, `namber`, `kol_vo_yaceek`, `dop_massa`) VALUES
(1, '1', '1', '100');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `gruz`
--
ALTER TABLE `gruz`
  ADD PRIMARY KEY (`id_gruz`);

--
-- Индексы таблицы `position`
--
ALTER TABLE `position`
  ADD PRIMARY KEY (`id_pos`),
  ADD KEY `id_stelaj` (`id_stelaj`),
  ADD KEY `id_gruz` (`id_gruz`);

--
-- Индексы таблицы `stelaj`
--
ALTER TABLE `stelaj`
  ADD PRIMARY KEY (`id_stelaj`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `gruz`
--
ALTER TABLE `gruz`
  MODIFY `id_gruz` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `position`
--
ALTER TABLE `position`
  MODIFY `id_pos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `stelaj`
--
ALTER TABLE `stelaj`
  MODIFY `id_stelaj` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `position`
--
ALTER TABLE `position`
  ADD CONSTRAINT `position_ibfk_1` FOREIGN KEY (`id_gruz`) REFERENCES `gruz` (`id_gruz`),
  ADD CONSTRAINT `position_ibfk_2` FOREIGN KEY (`id_stelaj`) REFERENCES `stelaj` (`id_stelaj`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
