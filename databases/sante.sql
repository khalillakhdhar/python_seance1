-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 03 mars 2021 à 16:12
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sante`
--

-- --------------------------------------------------------

--
-- Structure de la table `glycemi`
--

CREATE TABLE `glycemi` (
  `id_gl` int(11) NOT NULL,
  `valeur` float NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `id_personne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `imc`
--

CREATE TABLE `imc` (
  `id_imc` int(11) NOT NULL,
  `poid` float NOT NULL,
  `taille` float NOT NULL,
  `valeur` int(11) NOT NULL,
  `date_heure` timestamp NOT NULL DEFAULT current_timestamp(),
  `id_personne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `personne`
--

CREATE TABLE `personne` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `etat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `personne`
--

INSERT INTO `personne` (`id`, `nom`, `age`, `etat`) VALUES
(1, 'User 1', 22, 'bonne santé'),
(2, 'khalil', 30, 'acceptable'),
(3, 'teste', 30, 'je teste');

-- --------------------------------------------------------

--
-- Structure de la table `rythme`
--

CREATE TABLE `rythme` (
  `id` int(11) NOT NULL,
  `valeur` int(11) NOT NULL,
  `date_heure` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id_user` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `glycemi`
--
ALTER TABLE `glycemi`
  ADD PRIMARY KEY (`id_gl`),
  ADD KEY `id_personne` (`id_personne`);

--
-- Index pour la table `imc`
--
ALTER TABLE `imc`
  ADD PRIMARY KEY (`id_imc`),
  ADD KEY `id_personne` (`id_personne`);

--
-- Index pour la table `personne`
--
ALTER TABLE `personne`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `rythme`
--
ALTER TABLE `rythme`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rythme_ibfk_1` (`id_user`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `glycemi`
--
ALTER TABLE `glycemi`
  MODIFY `id_gl` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `imc`
--
ALTER TABLE `imc`
  MODIFY `id_imc` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `personne`
--
ALTER TABLE `personne`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `rythme`
--
ALTER TABLE `rythme`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `glycemi`
--
ALTER TABLE `glycemi`
  ADD CONSTRAINT `glycemi_ibfk_1` FOREIGN KEY (`id_personne`) REFERENCES `personne` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `imc`
--
ALTER TABLE `imc`
  ADD CONSTRAINT `imc_ibfk_1` FOREIGN KEY (`id_personne`) REFERENCES `personne` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `rythme`
--
ALTER TABLE `rythme`
  ADD CONSTRAINT `rythme_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `personne` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
