-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 25, 2020 at 07:04 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `goodreads`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin1`
--

CREATE TABLE `admin1` (
  `Email` varchar(20) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `Mobileno` varchar(10) NOT NULL,
  `otp` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin1`
--

INSERT INTO `admin1` (`Email`, `Password`, `Mobileno`, `otp`) VALUES
('admin@gmail.com', '123', '6280995201', 0);

-- --------------------------------------------------------

--
-- Table structure for table `billdetails`
--

CREATE TABLE `billdetails` (
  `billdetailsid` int(11) NOT NULL,
  `billid` int(11) NOT NULL,
  `bookid` int(11) NOT NULL,
  `price` float NOT NULL,
  `qty` int(11) NOT NULL,
  `ratingstatus` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `billdetails`
--

INSERT INTO `billdetails` (`billdetailsid`, `billid`, `bookid`, `price`, `qty`, `ratingstatus`) VALUES
(7, 11, 1, 2479, 1, 'pending'),
(8, 11, 4, 2471, 1, 'pending'),
(9, 12, 5, 1149, 1, 'pending'),
(10, 12, 6, 497, 1, 'pending'),
(11, 13, 1, 2479, 1, 'pending'),
(12, 14, 1, 2479, 1, 'pending'),
(13, 15, 1, 2479, 1, 'pending'),
(14, 16, 1, 2479, 1, 'pending'),
(15, 17, 4, 2471, 1, 'pending'),
(16, 18, 36, 400, 1, 'pending'),
(17, 19, 4, 22239, 3, 'pending'),
(18, 21, 5, 1149, 1, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `bills`
--

CREATE TABLE `bills` (
  `billid` int(11) NOT NULL,
  `totalamount` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `mobile` varchar(12) NOT NULL,
  `status` varchar(100) NOT NULL,
  `typeofbill` varchar(100) NOT NULL,
  `dateoforder` date NOT NULL,
  `rating` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bills`
--

INSERT INTO `bills` (`billid`, `totalamount`, `email`, `address`, `mobile`, `status`, `typeofbill`, `dateoforder`, `rating`) VALUES
(11, '4950.0', 'naiya96sharma@gmail.com', 'Green Field', '8360886084', 'sucess', 'done', '2019-11-25', 'done'),
(12, '1646.0', 'naiya96sharma@gmail.com', 'Green Field', '8360886084', 'sucess', 'done', '2019-11-25', 'done'),
(13, '2479.0', 'naiya96sharma@gmail.com', 'Green Field', '8360886084', 'sucess', 'done', '2019-11-26', 'pending'),
(14, '2479.0', 'naiya96sharma@gmail.com', 'Green Field', '8360886084', 'sucess', 'done', '2019-11-27', 'pending'),
(15, '2479.0', 'naiya96sharma@gmail.com', 'Green Field', '9023443280', 'pending', 'Cash', '2019-11-27', 'pending'),
(16, '2479.0', 'naiya96sharma@gmail.com', 'Green Field', '9023443280', 'pending', 'Cash', '2019-11-27', 'pending'),
(17, '2471.0', 'naiya96sharma@gmail.com', 'Green Field', '9023443280', 'pending', 'Cash', '2019-11-27', 'pending'),
(18, '400.0', 'abc@gmail.com', 'dsfdfvd', '6280995201', 'pending', 'Cash', '2020-05-23', 'pending'),
(19, '7413.0', 'abc@gmail.com', 'dsfdfvd', '6280995201', 'complete', 'By Card', '2020-05-23', 'pending'),
(20, '7413.0', 'abc@gmail.com', 'dsfdfvd', '6280995201', 'complete', 'By Card', '2020-05-23', 'pending'),
(21, '1149.0', 'abc@gmail.com', 'dsfdfvd', '6280995201', 'complete', 'By Card', '2020-05-23', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bookid` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` varchar(300) NOT NULL,
  `price` float NOT NULL,
  `edition` varchar(20) NOT NULL,
  `author` varchar(20) NOT NULL,
  `genre` varchar(20) NOT NULL,
  `catname` varchar(100) NOT NULL,
  `photo` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bookid`, `title`, `description`, `price`, `edition`, `author`, `genre`, `catname`, `photo`) VALUES
(1, 'Wings of Fire', 'An Autobiography of Abdul Kala', 2479, '1st', 'Arun Tiwari and A. P', 'Autobiography', 'Non-Fiction', 'categoryphotos/1879brands.jpg'),
(4, 'The Story Of My Experiments With Truth', 'Mahatma Gandhi Autobiography', 2471, '1st', 'Mahatma Gandhi', 'Autobiography', 'Non-Fiction', 'categoryphotos/2758gandhi.jpg'),
(5, 'Nelson Mandela: A Biography', 'Biography on Nelson Mandela', 1149, '1st', 'Mamta Sharma', 'Biography', 'Non-Fiction', 'categoryphotos/7308mandela.jpg'),
(6, 'The Autobiography of Benjamin Franklin ', 'Autobiography of Benjamin Franklin ', 497, '1st', 'Benjamin Franklin', 'Autobiography', 'Non-Fiction', 'categoryphotos/450benjamin.jpg'),
(7, 'The Story of My Life', 'An Autobiography of Helen Keller', 877, '1st', 'Helen Keller', 'Autobiography', 'Non-Fiction', 'categoryphotos/6164helen.jpg'),
(8, 'Rising Out of Hatred', 'Rising Out of Hatred tells the story of how white-supremacist ideas migrated from the far-right fringe to the White House through the intensely personal saga of one man who eventually disavowed everything he was taught to believe, at tremendous personal cost', 656, '1st', ' Eli Saslow', 'Based on Politics', 'Non-Fiction', 'categoryphotos/2683rising.jpg'),
(9, 'Bad Blood', 'story of the breathtaking rise and shocking collapse of Theranos, the one-time multibillion-dollar biotech startup founded by Elizabeth Holmes—now the subject of the HBO documentary The Inventor—by the prize-winning journalist who first broke the story and pursued it to the end.', 2788, '1st', 'JOHN CARREYROU', 'Based on Business', 'Non-Fiction', 'categoryphotos/7939bad.jpg'),
(10, 'Almost Everything', 'Anne Lamott calls for each of us to rediscover the nuggets of hope and wisdom that are buried within us that can make life sweeter than we ever imagined. Almost Everything pinpoints these moments of insight as it shines an encouraging light forward.', 234, '1st', ' ANNE LAMOTT', 'Philosophy | Religio', 'Non-Fiction', 'categoryphotos/8964almost.jpg'),
(11, 'Brief Answers to the Big Questions', '“Hawking’s parting gift to humanity . . . a book every thinking person worried about humanity’s future should read.”—NPR', 578, '1st', 'STEPHEN HAWKING', 'Science | Biography ', 'Non-Fiction', 'categoryphotos/1347ques.jpg'),
(12, 'The World of Lore: Dreadful Places', 'Captivating stories of the places where human evil has left a nefarious mark, featuring stories from the podcast Lore—now a streaming television series—including “Echoes,” “Withering Heights,” and “Behind Closed Doors” as well as rare material.', 287, '1st', 'AARON MAHNKE', ' History', 'Non-Fiction', 'categoryphotos/1140lore.jpg'),
(13, 'On the Other Side of Freedom THE CASE FOR HOPE', 'From the internationally recognized civil rights activist/organizer and host of the podcast Pod Save the People, a meditation on resistance, justice, and freedom, and an intimate portrait of a movement from the front lines.', 2479, '1st', 'DERAY MCKESSON', ' Biography & Memoir ', 'Non-Fiction', 'categoryphotos/2049freedom.jpg'),
(14, 'Presidents of War THE EPIC STORY, FROM 1807 TO MODERN TIMES', 'From a preeminent presidential historian comes a “monumental and profoundly important” (Ron Chernow) saga of America’s wartime chief executives', 344, '1st', 'MICHAEL BESCHLOSS', ' Military History | ', 'Non-Fiction', 'categoryphotos/4199warjpg.jpg'),
(15, 'Crashed HOW A DECADE OF FINANCIAL CRISES CHANGED THE WORLD', '“An intelligent explanation of the mechanisms that produced the crisis and the response to it…One of the great strengths of Tooze’s book is to demonstrate the deeply intertwined nature of the European and American financial systems.”–', 900, '1st', 'ADAM TOOZE', ' Economics | Managem', 'Non-Fiction', 'categoryphotos/977crashed.jpg'),
(16, 'Cook Like a Pro RECIPES AND TIPS FOR HOME COOKS: A COOKBOOK', 'ABOUT COOK LIKE A PRO In her new cookbook, Cook Like a Pro, Ina Garten shares a brand-new collection of recipes, tips, and techniques, so readers can cook with confidence no matter how much experience they have in the kitchen.', 500, '1st', ' INA GARTEN', ' Regional & Ethnic C', 'Non-Fiction', 'categoryphotos/4942cook.jpg'),
(17, 'The Spy and the Traitor THE GREATEST ESPIONAGE STORY OF THE COLD WAR', ' The celebrated author of Double Cross and Rogue Heroes returns with his greatest spy story yet, a thrilling Americans-era tale of Oleg Gordievsky, the Russian whose secret work helped hasten the end of the Cold War.', 765, '1st', 'BEN MACINTYRE', 'History | Politics |', 'Non-Fiction', 'categoryphotos/2179ben.jpg'),
(18, 'Comfort in an Instant 75 COMFORT FOOD RECIPES FOR YOUR PRESSURE COOKER, MULTICOOKER, AND INSTANT POT®: A COOKBOOK', 'With 75 all-new recipes–50 of which can be made in under an hour start to finish–Melissa Clark brings her easy sophistication to comfort food classics for any electric pressure cooker, multicooker, or Instant Pot.', 432, '1st', 'MELISSA CLARK', ' Cooking Methods', 'Non-Fiction', 'categoryphotos/9555cookbook.jpg'),
(19, 'The White Darkness', ' a powerful true story of adventure and obsession in the Antarctic, lavishly illustrated with color photographs', 497, '1st', 'DAVID GRANN', ' History | Biography', 'Non-Fiction', 'categoryphotos/5157white.jpg'),
(20, 'On Desperate Ground THE EPIC STORY OF CHOSIN RESERVOIR–THE GREATEST BATTLE OF THE KOREAN WAR', 'A masterpiece of thorough research, deft pacing and arresting detail…This war story — the fight to break out of a frozen hell near the Chosin Reservoir — has been told many times before. But Sides tells it exceedingly well, with fresh research, gritty scenes and cinematic sweep.”—Washington Post', 809, '1st', 'HAMPTON SIDES', '1950 – Present Milit', 'Non-Fiction', 'categoryphotos/7888desperate.jpg'),
(21, 'Heirs of the Founders HENRY CLAY, JOHN CALHOUN AND DANIEL WEBSTER, THE SECOND GENERATION OF AMERICAN GIANTS', 'From New York Times bestselling historian H. W. Brands comes the riveting story of how, in nineteenth-century America, a new set of political giants battled to complete the unfinished work of the Founding Fathers and decide the future of our democracy', 766, '1st', ' H. W. BRANDS', ' 19th Century U.S. H', 'Non-Fiction', 'categoryphotos/1257brands.jpg'),
(22, 'You’re the Only One I Can Tell INSIDE THE LANGUAGE OF WOMEN’S FRIENDSHIPS', 'This warm, wise exploration of female friendship from the #1 New York Times bestselling author of You Just Don’t Understand will help women lean into these powerful relationships.', 777, '1st', 'DEBORAH TANNEN', 'Personal Growth', 'Non-Fiction', 'categoryphotos/7216women.jpg'),
(23, 'How to Change Your Mind WHAT THE NEW SCIENCE OF PSYCHEDELICS TEACHES US ABOUT CONSCIOUSNESS, DYING, ADDICTION, DEPRESSION, AND TRANSCENDENCE', 'A brilliant and brave investigation into the medical and scientific revolution taking place around psychedelic drugs–and the spellbinding story of his own life-changing psychedelic experiences', 655, '1st', ' MICHAEL POLLAN', ' Philosophy | Biogra', 'Non-Fiction', 'categoryphotos/9797mind.jpg'),
(30, 'The trials of Apollo', 'Action packed novel', 200, '1st', 'Rick Riordan', 'ActionAdventure', 'Fiction', 'categoryphotos/8102Apollo.jpg'),
(31, 'Immortal Plunder', 'rettwet', 300, '', 'KellySt Clare', 'ActionAdventure', 'Fiction', 'categoryphotos/919ImmortalPlunder.jpg'),
(32, 'Invasion', 'based on warriors', 400, 'fourth edition', 'KF Breene', 'ActionAdventure', 'Fiction', 'categoryphotos/1593Invasion.jpg'),
(33, 'Iron Tide Rising', '', 350, 'sixth edition', 'Carrie Riyan', 'ActionAdventure', 'Fiction', 'categoryphotos/3962Irontide.jpg'),
(34, 'The Magic Pole', 'the story revolves around magi', 500, '', 'Jasmine Hansson', 'ActionAdventure', 'Fiction', 'categoryphotos/6351TheMagicPole.jpg'),
(35, 'Kingdom Of Ash', 'A Throne Of Glass Novel', 450, '', 'Saara J .Maas', 'ActionAdventure', 'Fiction', 'categoryphotos/8893KingdomofAsh.jpg'),
(36, 'Turning darkness into night', '', 400, '', 'Marrie Brennan', 'Fantasy', 'Fiction', 'categoryphotos/8648Darkness.jpg'),
(37, 'Game of Thrones', '', 500, '', 'George R R Martin', 'Fantasy', 'Fiction', 'categoryphotos/8183Gameofthrones.jpg'),
(38, 'Hell in a Handbasket', '', 500, '', 'Denise Grover Swank', 'Fantasy', 'Fiction', 'categoryphotos/2681Handbasket.jpg'),
(39, 'Harry Potter', 'illustrated by Jim Kay', 600, '', 'JK Rowling', 'Fantasy', 'Fiction', 'categoryphotos/793HarryPotter.jpg'),
(40, 'The Revenge Of Magic', '', 350, '', 'James Riley', 'Fantasy', 'Fiction', 'categoryphotos/2822Magic.jpg'),
(41, 'Monster Portraits', '', 650, '', 'Del Samartay', 'Fantasy', 'Fiction', 'categoryphotos/2627Monster.jpg'),
(42, 'On a Sunbeam', '', 450, '', 'Tillie Walden', 'Fantasy', 'Fiction', 'categoryphotos/5328Sunbean.jpg'),
(43, 'Sunny Side', '', 500, '', 'Glen David Gold', 'Fantasy', 'Fiction', 'categoryphotos/6220Sunny.jpg'),
(44, 'Magic And Witches', 'cursed blood series', 600, '', 'Devyn Jayse', 'Fantasy', 'Fiction', 'categoryphotos/6507witches.jpg'),
(45, 'Blood Water Paint', '', 600, '', 'Joy Mucculough', 'Young Adult', 'Fiction', 'categoryphotos/3180blood.jpg'),
(46, 'Divergent', '', 550, '', 'Veronica Roth', 'Young Adult', 'Fiction', 'categoryphotos/4421Divergent.jpg'),
(47, 'Earthshine', 'from the insurrection series', 600, '', 'Kadee Carder', 'Young Adult', 'Fiction', 'categoryphotos/2306Earthshine.jpg'),
(48, 'Fallen', '', 450, '', 'Lauen Kate', 'Young Adult', 'Fiction', 'categoryphotos/558Fallen.jpg'),
(49, 'Blood Heir', '', 600, '', 'Amelie Wen Zhao', 'Young Adult', 'Fiction', 'categoryphotos/2489heir.jpg'),
(50, 'The Girl In Room', '', 400, '', 'Chetan Bhagat', 'Young Adult', 'Fiction', 'categoryphotos/9316Thegirl.jpg'),
(51, 'Gentleman', 'Bryn And Synin Series', 700, '', 'HP Mallory', 'Romance', 'Fiction', 'categoryphotos/7805Gentleman.jpg'),
(52, 'Someone to Honor', '', 600, '', 'Mary  Balogh', 'Romance', 'Fiction', 'categoryphotos/6674Honor.jpg'),
(53, 'The Montbryce Legacy vol ', '', 730, 'eight edition', 'Anna  Markland', 'Romance', 'Fiction', 'categoryphotos/6850Legacy.jpg'),
(54, 'An Affair With Notorious Heiress', 'known for beautiful emotional deeply Romance', 340, '', 'Lorraine Heath', 'Romance', 'Fiction', 'categoryphotos/832Lorraine.jpg'),
(55, 'Meet Cute', '', 500, '', 'Heelena Hunting', 'Romance', 'Fiction', 'categoryphotos/2163Meet.jpg'),
(56, 'Compeeled by the Vampire', '', 200, '', 'Kellie Mcallen', 'Romance', 'Fiction', 'categoryphotos/548Vam.jpg'),
(57, 'A voice in trhe Wind', '', 450, '', 'Francinie Rivers', 'Romance', 'Fiction', 'categoryphotos/8221Voice.jpg'),
(58, 'The Accidental War', '', 600, '', 'Walter Jon Williams', 'Science Fiction', 'Fiction', 'categoryphotos/9018AccidentalWar.jpg'),
(59, 'Blackwater', '', 300, '', 'Christian Galacer', 'Science Fiction', 'Fiction', 'categoryphotos/5373Blackwater.jpg'),
(60, 'Best Of British', '', 350, 'seventh edition', 'Donna Scott', 'Science Fiction', 'Fiction', 'categoryphotos/9684British.jpg'),
(61, 'The Immortal Storm', 'Ahistory of science fiction', 400, '', 'Sam Moscowitz', 'Science Fiction', 'Fiction', 'categoryphotos/5112ImmortalStorm.jpg'),
(62, 'Infinite Worlds', 'The Fantastic visions of Science fiction art', 600, '', 'Vincent Difate', 'Science Fiction', 'Fiction', 'categoryphotos/7565InfiniteWorlds.jpg'),
(63, 'The Language Of The Night', '', 300, '', 'Ursukla K.le Guin', 'Science Fiction', 'Fiction', 'categoryphotos/1702Languageofnight.jpg'),
(64, 'The Canopy Of Time', '', 670, '', 'Brian Aldiss', 'Speculative Fiction', 'Fiction', 'categoryphotos/9165Canopy.jpg'),
(65, 'Crown Of Infinity', 'Who claims this galaxy?', 250, '', 'John M. Faucette', 'Speculative Fiction', 'Fiction', 'categoryphotos/2214Crown.jpg'),
(66, 'The House Of Hades', '', 450, '', 'Rick Riordan', 'Speculative Fiction', 'Fiction', 'categoryphotos/30House.jpg'),
(67, 'The Sky Is Filled With Ships', '', 1000, '', 'Richard C Meredith', 'Speculative Fiction', 'Fiction', 'categoryphotos/6906Sky.jpg'),
(68, 'Price Of Vengeance', 'A dreamscape Warriors Novel', 1050, '', 'Kurt D Springs', 'Speculative Fiction', 'Fiction', 'categoryphotos/1242Vengeance.jpg'),
(69, 'Crucible', '', 2000, '', 'James Rollins', 'Thriller/Suspense', 'Fiction', 'categoryphotos/1798Crucible.jpg'),
(70, 'Labyrinth', '', 1013, '', 'Catherine Coulter', 'Thriller/Suspense', 'Fiction', 'categoryphotos/4605Labyrinth.jpg'),
(71, 'A ladder to the sky', '', 780, '', 'John Boyne', 'Thriller/Suspense', 'Fiction', 'categoryphotos/1320Ladder.jpg'),
(72, 'A Steep Price', '', 800, '', 'Robert Dugoni', 'Thriller/Suspense', 'Fiction', 'categoryphotos/1407Price.jpg'),
(73, 'Samaritan', '', 960, '', 'Richard', 'Thriller/Suspense', 'Fiction', 'categoryphotos/8288Samaritan.jpg'),
(74, 'The Shadow District', '', 800, '', 'Arnaldour Indridason', 'Thriller/Suspense', 'Fiction', 'categoryphotos/7113Shadow.jpg'),
(75, 'Animal Man', '', 780, '', 'Jim Lennire', 'Comics', 'Fiction', 'categoryphotos/2378Animal Man (2011-) - Annual 001-000.jpg'),
(76, 'Bat Girl', '', 600, '', 'Simonni', 'Comics', 'Fiction', 'categoryphotos/9000Batgirl (2011-) - Annual 001-000.jpg'),
(77, 'Aquamen And The Others', '', 700, '', 'Martinzz', 'Comics', 'Fiction', 'categoryphotos/3733Aquaman and the Others 001-000.jpg'),
(78, 'Astonishing X Men', '', 400, '', 'Rosanus Woodard', 'Comics', 'Fiction', 'categoryphotos/6050Astonishing X-Men (2017-) 005-000.jpg'),
(79, 'Constatine', '', 560, '', 'Salazer  Leistine', 'Comics', 'Fiction', 'categoryphotos/5081Constantine (2013-) 017-001.jpg'),
(80, 'Bizarro', '', 670, '', 'Corson', 'Comics', 'Fiction', 'categoryphotos/8472Bizarro (2015-) 001-001.jpg'),
(81, 'tyt', 'df', 567, 'six', 'vdf', 'scs', 'Fiction', 'categoryphotos/8451TheMagicPole.jpg'),
(82, '', 'scs', 567, 'scx', 'xas', '', 'Fiction', 'categoryphotos/273Stuart.jpg'),
(83, 'book of rings', 'Action packed novel', 287, '1st', ' Eli Saslow', 'Based on action,susp', 'Fiction', 'categoryphotos/2947blond-1866951_1920.jpg'),
(84, 'sam sam sam', 'dgjh', 45, '1', 'author1', ' History | Biography', 'Fiction', 'categoryphotos/5818Screenshot from 2020-05-19 23-32-10.png');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `catname` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `catphoto` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`catname`, `description`, `catphoto`) VALUES
('Fiction', 'It includes imaginary things such as action,comedy,suspense and thriller.', 'categoryphotos/9744books.jpg'),
('Non-Fiction', 'Based on Real life', 'categoryphotos/4810pexels-photo-46274.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `ebooks`
--

CREATE TABLE `ebooks` (
  `ebookid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `file` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ebooks`
--

INSERT INTO `ebooks` (`ebookid`, `pid`, `title`, `description`, `file`) VALUES
(5, 7, 'Nelson Mandela: A Biography', 'Biography based on the life of Nelson Mandela', 'categoryphotos/4715the-autobiography-of-nelson-mandela.pdf'),
(6, 7, 'The Story of My Life', 'An Autobiography of Hellen Keller', 'categoryphotos/7544The Story of My Life, by Helen Keller.pdf'),
(7, 7, 'Rising Out of Hatred', 'based on history and politics', 'categoryphotos/260the-autobiography-of-nelson-mandela.pdf'),
(8, 7, 'The Story Of My Experiments With Truth', 'An Autobiography of Mahatama Gandhi', 'categoryphotos/9180The Story of My Life, by Helen Keller.pdf'),
(9, 8, 'The World of Lore: Dreadful Places', 'Based on Haunted Places', 'categoryphotos/8345the-autobiography-of-nelson-mandela.pdf'),
(10, 8, 'The White Darkness', 'based on history and politics', 'categoryphotos/6701The Story of My Life, by Helen Keller.pdf'),
(11, 8, 'The trials of Appolo', 'Action Adventure', 'categoryphotos/9281the-autobiography-of-nelson-mandela.pdf'),
(12, 9, 'Bad Blood', 'Based on philosiphy', 'categoryphotos/6325the-autobiography-of-nelson-mandela.pdf'),
(13, 9, 'Brief Answers to the Big Questions', 'Answering to questions of people', 'categoryphotos/3668The Story of My Life, by Helen Keller.pdf'),
(14, 9, 'Autobiography of Benjamin Franklin', 'An Autobiography of Benjamin Franklin', 'categoryphotos/1086The Story of My Life, by Helen Keller.pdf'),
(16, 9, 'Rising Out of Hatred', 'based on Politics', 'categoryphotos/7313the-autobiography-of-nelson-mandela.pdf'),
(17, 10, 'Almost Everything', 'Based on philosophy', 'categoryphotos/5796the-autobiography-of-nelson-mandela.pdf'),
(18, 10, 'Freedom THE CASE FOR HOPE', 'Biography', 'categoryphotos/7710The Story of My Life, by Helen Keller.pdf'),
(19, 11, 'Presidents of War THE EPIC STORY, FROM 1807 TO MODERN TIMES', 'Military History', 'categoryphotos/7038the-autobiography-of-nelson-mandela.pdf'),
(20, 11, 'The Story of My Life', 'An Autobiography of Hellen Keller', 'categoryphotos/3508The Story of My Life, by Helen Keller.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `packages`
--

CREATE TABLE `packages` (
  `pid` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `noofbooks` int(10) NOT NULL,
  `validity` varchar(50) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `packages`
--

INSERT INTO `packages` (`pid`, `name`, `noofbooks`, `validity`, `price`) VALUES
(7, 'Combo Offer', 5, '2months', 2479),
(8, 'prime membership', 3, '6 months', 1149),
(9, 'Christmas Dhamaka', 4, '1 months', 560),
(10, 'New Year special', 2, '1 month', 360),
(11, 'Premium Discounts', 2, '4 months', 700);

-- --------------------------------------------------------

--
-- Table structure for table `ratings`
--

CREATE TABLE `ratings` (
  `ratingid` int(11) NOT NULL,
  `rating` float NOT NULL,
  `bookid` int(11) NOT NULL,
  `review` varchar(500) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ratings`
--

INSERT INTO `ratings` (`ratingid`, `rating`, `bookid`, `review`, `email`) VALUES
(1, 4, 1, 'this this my first review', 'naiya96sharma@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `sample`
--

CREATE TABLE `sample` (
  `sid` int(10) NOT NULL,
  `bookid` int(10) NOT NULL,
  `description` varchar(200) NOT NULL,
  `photo` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sample`
--

INSERT INTO `sample` (`sid`, `bookid`, `description`, `photo`) VALUES
(8, 1, 'Based on Real life', 'categoryphotos/4379APJ1.JPG'),
(9, 1, 'An Autobiography of Abdul Kalam', 'categoryphotos/3897APJ2.jpg'),
(10, 1, 'Mahatma Gandhi Autobiography', 'categoryphotos/6530APJ3.JPG'),
(11, 30, 'Action packed novel', 'categoryphotos/2547almosteverything.PNG'),
(12, 30, 'Action packed novel', 'categoryphotos/1061almosteverything.PNG'),
(13, 30, 'great place for holidays', 'categoryphotos/5581Screenshot from 2020-05-19 14-23-06.png'),
(14, 1, 'sdg', 'categoryphotos/6275Screenshot from 2020-05-19 14-22-12.png');

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `subscriptionid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `status` varchar(10) NOT NULL,
  `dateofbuy` varchar(100) NOT NULL,
  `amount` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subscription`
--

INSERT INTO `subscription` (`subscriptionid`, `pid`, `email`, `status`, `dateofbuy`, `amount`) VALUES
(2, 7, 'naiya96sharma@gmail.com', 'Active', '2019-11-22', '2479'),
(3, 8, 'naiya96sharma@gmail.com', 'Active', '2019-11-22', '1149'),
(4, 8, 'naiya96sharma@gmail.com', 'Active', '2019-11-22', '1149'),
(5, 7, 'naiya96sharma@gmail.com', 'Active', '2019-11-22', '2479'),
(6, 9, 'naiya96sharma@gmail.com', 'Active', '2019-12-04', '560'),
(7, 7, 'naiya96sharma@gmail.com', 'Active', '2019-12-04', '2479'),
(8, 7, 'abc@gmail.com', 'Active', '2020-05-22', '2479');

-- --------------------------------------------------------

--
-- Table structure for table `usersignup`
--

CREATE TABLE `usersignup` (
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `state` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usersignup`
--

INSERT INTO `usersignup` (`email`, `password`, `name`, `address`, `state`, `mobile`, `photo`) VALUES
('abc@gmail.com', '123', 'RADHIKA', 'dsfdfvd', 'punjab', '6280995201', 'categoryphotos/newpics/1779equilateral.PNG'),
('borohacati@mailinator.net', '123456789', 'Mariam Whitaker', 'Amet beatae consequ', 'Impedit aperiam asp', '6280995201', 'categoryphotos/newpics/7689Screenshot from 2020-05-19 14-22-25.png'),
('rifezuv@mailinator.net', 'Pa$$w0rd!', 'Brenden Frank', 'Cum impedit laborum', 'Amet nulla aute non', '6280995201', 'categoryphotos/newpics/7901Screenshot from 2020-05-21 12-33-24.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin1`
--
ALTER TABLE `admin1`
  ADD PRIMARY KEY (`Email`);

--
-- Indexes for table `billdetails`
--
ALTER TABLE `billdetails`
  ADD PRIMARY KEY (`billdetailsid`);

--
-- Indexes for table `bills`
--
ALTER TABLE `bills`
  ADD PRIMARY KEY (`billid`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bookid`),
  ADD KEY `catname` (`catname`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`catname`);

--
-- Indexes for table `ebooks`
--
ALTER TABLE `ebooks`
  ADD PRIMARY KEY (`ebookid`),
  ADD KEY `pid` (`pid`);

--
-- Indexes for table `packages`
--
ALTER TABLE `packages`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `ratings`
--
ALTER TABLE `ratings`
  ADD PRIMARY KEY (`ratingid`),
  ADD UNIQUE KEY `bookid` (`bookid`);

--
-- Indexes for table `sample`
--
ALTER TABLE `sample`
  ADD PRIMARY KEY (`sid`),
  ADD KEY `bookid` (`bookid`);

--
-- Indexes for table `subscription`
--
ALTER TABLE `subscription`
  ADD PRIMARY KEY (`subscriptionid`),
  ADD KEY `pid` (`pid`,`email`);

--
-- Indexes for table `usersignup`
--
ALTER TABLE `usersignup`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `billdetails`
--
ALTER TABLE `billdetails`
  MODIFY `billdetailsid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `bills`
--
ALTER TABLE `bills`
  MODIFY `billid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `bookid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- AUTO_INCREMENT for table `ebooks`
--
ALTER TABLE `ebooks`
  MODIFY `ebookid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `packages`
--
ALTER TABLE `packages`
  MODIFY `pid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `ratings`
--
ALTER TABLE `ratings`
  MODIFY `ratingid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `sample`
--
ALTER TABLE `sample`
  MODIFY `sid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `subscription`
--
ALTER TABLE `subscription`
  MODIFY `subscriptionid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`catname`) REFERENCES `category` (`catname`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ebooks`
--
ALTER TABLE `ebooks`
  ADD CONSTRAINT `ebooks_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `packages` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `ratings`
--
ALTER TABLE `ratings`
  ADD CONSTRAINT `ratings_ibfk_1` FOREIGN KEY (`bookid`) REFERENCES `books` (`bookid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sample`
--
ALTER TABLE `sample`
  ADD CONSTRAINT `sample_ibfk_1` FOREIGN KEY (`bookid`) REFERENCES `books` (`bookid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `subscription`
--
ALTER TABLE `subscription`
  ADD CONSTRAINT `subscription_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `packages` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
