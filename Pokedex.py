import math
import string
import copy
#whoa

from tkinter import *
from PIL import Image, ImageTk

#==============================import math
import string
import copy

#whoa

from tkinter import *

#========================================================List
pokemonList = (
("#001", "Bulbasaur", ("Grass", "Poison")),
("#002", "Ivysaur", ("Grass", "Poison")),
("#003", "Venusaur", ("Grass", "Poison")),
("#004", "Charmander", ("Fire")),
("#005", "Charmeleon", ("Fire")),
("#006", "Charizard", ("Fire", "Flying")),
("#007", "Squirtle", ("Water")),
("#008", "Wartortle", ("Water")),
("#009", "Blastoise", ("Water")),
('#010', 'Caterpie', ('Bug')),
('#011', 'Metapod', ('Bug')),
('#012', 'Butterfree', ('Bug',	'Flying')),
('#013', 'Weedle', ('Bug', 'Poison')),
('#014', 'Kakuna', ('Bug', 'Poison')),
('#015', 'Beedrill', ('Bug', 'Poison')),
('#016', 'Pidgey', ('Normal', 'Flying')),
('#017', 'Pidgeotto', ('Normal', 'Flying')),
('#018', 'Pidgeot', ('Normal', 'Flying')),
('#019', 'Rattata', ('Normal')),
('#020', 'Raticate', ('Normal')),
('#021', 'Spearow', ('Normal', 'Flying')),
('#022', 'Fearow', ('Normal', 'Flying')),
('#023', 'Ekans', ('Poison')),
('#024', 'Arbok', ('Poison')),
('#025', 'Pikachu', ('Electric')),
('#026', 'Raichu', ('Electric')),
('#027', 'Sandshrew', ('Ground')),
('#028', 'Sandslash', ('Ground')),
('#029', 'Nidoran (F)', ('Poison')),
('#030', 'Nidorina', ('Poison')),
('#031', 'Nidoqueen', ('Poison', 'Ground')),
('#032', 'Nidoran (M)', ('Poison')),
('#033', 'Nidorino', ('Poison')),
('#034', 'Nidoking', ('Poison', 'Ground')),
('#035', 'Clefairy', ('Fairy')),
('#036', 'Clefable', ('Fairy')),
('#037', 'Vulpix', ('Fire')),
('#038', 'Ninetails', ('Fire')),
('#039', 'Jigglypuff', ('Normal', 'Fairy')),
('#040', 'Wigglytuff', ('Normal', 'Fairy')),
('#041', 'Zubat', ('Poison', 'Flying')),
('#042', 'Golbat', ('Poison', 'Flying')),
('#043', 'Oddish', ('Grass', 'Poison')),
('#044', 'Gloom', ('Grass', 'Poison')),
('#045', 'Vileplume', ('Grass', 'Poison')),
('#046', 'Paras', ('Bug', 'Grass')),
('#047', 'Parasect', ('Bug', 'Grass')),
('#048', 'Venonat', ('Bug', 'Poison')),
('#049', 'Venomoth', ('Bug', 'Poison')),
('#050', 'Diglett', ('Ground')),
('#051', 'Dugtrio', ('Ground')),
('#052', 'Meowth', ('Normal')),
('#053', 'Persian', ('Normal')),
('#054', 'Psyduck', ('Water')),
('#055', 'Golduck', ('Water')),
('#056', 'Mankey', ('Fighting')),
('#057', 'Primeape', ('Fighting')),
('#058', 'Growlithe', ('Fire')),
('#059', 'Arcanine', ('Fire')),
('#060', 'Poliwag', ('Water')),
('#061', 'Poliwhirl', ('Water')),
('#062', 'Poliwrath', ('Water', 'Fighting')),
('#063', 'Abra', ('Psychic')),
('#064', 'Kadabra', ('Psychic')),
('#065', 'Alakazam', ('Psychic')),
('#066', 'Machop', ('Fighting')),
('#067', 'Machoke', ('Fighting')),
('#068', 'Machamp', ('Fightin')),
('#069', 'Bellsprout', ('Grass', 'Poison')),
('#070', 'Weepinbell', ('Grass', 'Poison')),
('#071', 'Victreebel', ('Grass', 'Poison')),
('#072', 'Tentacool', ('Water', 'Poison')),
('#073', 'Tentacruel', ('Water', 'Poison')),
('#074', 'Geodude', ('Rock', 'Ground')),
('#075', 'Graveler', ('Rock', 'Ground')),
('#076', 'Golem', ('Rock', 'Ground')),
('#077', 'Ponyta', ('Fire')),
('#078', 'Rapidash', ('Fire')),
('#079', 'Slowpoke', ('Water', 'Psychic')),
('#080', 'Slowbro', ('Water', 'Psychic')),
('#081', 'Magnemite', ('Electric', 'Steel')),
('#082', 'Magneton', ('Electric', 'Steel')),
('#083', 'Farfetch\'d', ('Normal', 'Flying')),
('#084', 'Doduo', ('Normal', 'Flying')),
('#085', 'Dodrio', ('Normal', 'Flying')),
('#086', 'Seel', ('Water')),
('#087', 'Dewgong', ('Water', 'Ice')),
('#088', 'Grimer', ('Poison')),
('#089', 'Muk', ('Poison')),
('#090', 'Shellder', ('Water')),
('#091', 'Cloyster', ('Water', 'Ice')),
('#092', 'Gastly', ('Ghost', 'Poison')),
('#093', 'Haunter', ('Ghost', 'Poison')),
('#094', 'Gengar', ('Ghost', 'Poison')),
('#095', 'Onix', ('Rock', 'Ground')),
('#096', 'Drowzee', ('Psychic')),
('#097', 'Hypno', ('Psychic')),
('#098', 'Krabby', ('Water')),
('#099', 'Kingler', ('Water')),
('#100', 'Voltorb', ('Electric')),
('#101', 'Electrode', ('Electric')),
('#102', 'Exeggcute', ('Grass', 'Psychic')),
('#103', 'Exeggutor', ('Grass', 'Psychic')),
('#104', 'Cubone', ('Ground')),
('#105', 'Marowak', ('Ground')),
('#106', 'Hitmonlee', ('Fighting')),
('#107', 'Hitmonchan', ('Fighting')),
('#108', 'Lickitung', ('Normal')),
('#109', 'Koffing', ('Poison')),
('#110', 'Weezing', ('Poison')),
('#111', 'Rhyhorn', ('Ground', 'Rock')),
('#112', 'Rhydon', ('Ground', 'Rock')),
('#113', 'Chansey', ('Normal')),
('#114', 'Tangela', ('Grass')),
('#115', 'Kangaskhan', ('Normal')),
('#116', 'Horsea', ('Water')),
('#117', 'Seadra', ('Water')),
('#118', 'Goldeen', ('Water')),
('#119', 'Seaking', ('Water')),
('#120', 'Staryu', ('Water')),
('#121', 'Starmie', ('Water', 'Psychic')),
('#122', 'Mr. Mime', ('Psychic', 'Fairy')),
('#123', 'Scyther', ('Bug', 'Flying')),
('#124', 'Jynx', ('Ice', 'Psychic')),
('#125', 'Electabuzz', ('Electric')),
('#126', 'Magmar', ('Fire')),
('#127', 'Pinsir', ('Bug')),
('#128', 'Tauros', ('Normal')),
('#129', 'Magikarp', ('Water')),
('#130', 'Gyarados', ('Water', 'Flying')),
('#131', 'Lapras', ('Water', 'Ice')),
('#132', 'Ditto', ('Normal')),
('#133', 'Eevee', ('Normal')),
('#134', 'Vaporeon', ('Water')),
('#135', 'Jolteon', ('Eletric')),
('#136', 'Flareon', ('Fire')),
('#137', 'Porygon', ('Normal')),
('#138', 'Omanyte', ('Rock', 'Water')),
('#139', 'Omastar', ('Rock', 'Water')),
('#140', 'Kabuto', ('Rock', 'Water')),
('#141', 'Kabutops', ('Rock', 'Water')),
('#142', 'Aerodactyl', ('Rock', 'Flying')),
('#143', 'Snorlax', ('Normal')),
('#144', 'Articuno', ('Ice', 'Flying')),
('#145', 'Zapdos', ('Electric', 'Flying')),
('#146', 'Moltres', ('Fire', 'Flying')),
('#147', 'Dratini', ('Dragon')),
('#148', 'Dragonair', ('Dragon')),
('#149', 'Dragonite', ('Dragonite', 'Flying')),
('#150', 'Mewtwo', ('Psychic')),
('#151', 'Mew', ('Psychic'))
)


categoryList = (
('Seed Pokémon'),
('Seed Pokémon'),
('Seed Pokémon'),
('Lizard Pokémon'),
('Flame Pokémon'),
('Flame Pokémon'),
('Young Turtle \n Pokémon'),
('Turtle Pokémon'),
('Shell Pokémon'),
('Caterpillar Pokémon'), #10
('Chrysalis Pokémon'),
('Butterfly Pokémon'),
('Hairy Caterpillar \n Pokémon'),
('Pupa Pokémon'),
('Poison Bee \n Pokémon'),
('Small Bird \n Pokémon'),
('Bird Pokémon'),
('Bird Pokémon'),
('Mouse Pokémon'),
('Mouse Pokémon'),#20
('Small Bird \n Pokémon'),
('Beak Pokémon'),
('Snake Pokémon'),
('Cobra Pokémon'),
('Mouse Pokémon'),#25
('Mouse Pokémon'),
('Mouse Pokémon'),
('Mouse Pokémon'),
('Poison Needle Pokémon'),
('Poison Needle Pokémon'),#30
('Drill Pokémon'),
('Poison Needle Pokémon'),
('Poison Needle Pokémon'),
('Drill Pokémon'),
('Fairy Pokémon'),#35
('Fairy Pokémon'),
('Fox Pokémon'),
('Fox Pokémon'),
('Balloon Pokémon'),
('Balloon Pokémon'),#40
('Bat Pokémon'),
('Bat Pokémon'),
('Weed Pokémon'),
('Weed Pokémon'),
('Flower Pokémon'),#45
('Mushroom Pokémon'),
('Mushroom Pokémon'),
('Insect Pokémon'),
('Poison Moth Pokémon'),
('Mole Pokémon'),#50
('Mole Pokémon'),
('Bakeneko Pokémon'),
('Siamese Cat Pokémon'),
('Duck Pokémon'),
('Duck Pokémon'),#55
('Pig Monkey Pokémon'),
('Pig Monkey Pokémon'),
('Puppy Pokémon'),
('Legend Pokémon'),
('Tadpole Pokémon'),#60
('Tadpole Pokémon'),
('Tadpole Pokémon'),
('Telekinesis Pokémon'),
('Telekinesis Pokémon'),
('Telekinesis Pokémon'),#65
('Superhuman Strength \n Pokémon'),
('Superhuman Strength \n Pokémon'),
('Superhuman Strength \n Pokémon'),
('Flower Pokémon'),
('Flycatcher Pokémon'),#70
('Flycatcher Pokémon'),
('Jellyfish Pokémon'),
('Jellyfish Pokémon'),
('Rock Pokémon'),
('Rock Pokémon'),#75
('Megaton Pokémon'),
('Fire Horse Pokémon'),
('Fire Horse Pokémon'),
('Stupid Pokémon'),
('Hermit Crab Pokémon'),#80
('Magnet Pokémon'),
('Magnet Pokémon'),
('Spot-Billed \n Duck Pokémon'),
('Twin Bird Pokémon'),
('Triplet Bird Pokémon'),#85
('Sea Lion Pokémon'),
('Sea Lion Pokémon'),
('Sludge Pokémon'),
('Sludge Pokémon'),
('Bivalve Pokémon'),#90
('Bivalve Pokémon'),
('Gaseous Pokémon'),
('Gaseous Pokémon'),
('Shadow Pokémon'),
('Rock Snake Pokémon'),#95
('Hypnosis Pokémon'),
('Hypnosis Pokémon'),
('Freshwater Crab \n Pokémon'),
('Pincer Pokémon'),
('Ball Pokémon'),#100
('Ball Pokémon'),
('Egg Pokémon'),
('Coconut Pokémon'),
('Lonely Pokémon'),
('Bone Lover Pokémon'),#105
('Kick Pokémon'),
('Punch Pokémon'),
('Licking Pokémon'),
('Poison Gas Pokémon'),
('Poison Gas Pokémon'), #110
('Spikes Pokémon'),
('Drill Pokémon'),
('Egg Pokémon'),
('Vine Pokémon'),
('Parent Pokémon'), #115
('Dragon Pokémon'),
('Dragon Pokémon'),
('Goldfish Pokémon'),
('Goldfish Pokémon'),
('Star Shape Pokémon'), #120
('Mysterious Pokémon'),
('Barrier Pokémon'),
('Mantis Pokémon'),
('Human Shape Pokémon'),
('Electric Pokémon'), #125
('Spitfire Pokémon'),
('Stag Beetle Pokémon'),
('Wild Bull Pokémon'),
('Fish Pokémon'),
('Atrocius Pokémon'), #130
('Transport Pokémon'),
('Transform Pokémon'),
('Evolution Pokémon'),
('Bubble Jet Pokémon'),
('Lightning Pokémon'), #135
('Flame Pokémon'), 
('Virtual Pokémon'),
('Spiral Pokémon'),
('Spiral Pokémon'),
('Shellfish Pokémon'), #140
('Shellfish Pokémon'), 
('Fossil Pokémon'),
('Sleeping Pokémon'),
('Freeze Pokémon'),
('Electric Pokémon'), #145
('Flame Pokémon'), 
('Dragon Pokémon'),
('Dragon Pokémon'),
('Dragon Pokémon'),
('Genetic Pokémon'), #150
('New Species Pokémon')
)

eggEvolveList = (
(('Monster', 'Grass'), '16'),
(('Monster', 'Grass'), '32'),
(('Monster', 'Grass'), 'Highest \nEvolution'),
(('Monster', 'Dragon'), '16'),
(('Monster', 'Dragon'), '36'),
(('Monster', 'Dragon'), 'Highest \nEvolution'),
(('Monster', 'Water 1'), '16'),
(('Monster', 'Water 1'), '36'),
(('Monster', 'Water 1'), 'Highest \nEvolution'),
(('Bug'), '7'), #10
(('Bug'), '10'),
(('Bug'), 'Highest \nEvolution'),
(('Bug'), '7'),
(('Bug'), '10'),
(('Bug'), 'Highest \nEvolution'),
(('Flying'), '18'),
(('Flying'), '36'),
(('Flying'), 'Highest \nEvolution'),
(('Field'), '20'),
(('Field'), 'Highest \nEvolution'), #20
(('Flying'), '20'),
(('Flying'), 'Highest \nEvolution'),
(('Field', 'Dragon'), '22'),
(('Field', 'Dragon'), 'Highest \nEvolution'),
(('Field', 'Fairy'), 'With Stone'),
(('Field', 'Fairy'), 'Highest \nEvolution'),
(('Field'), '22'),
(('Field'), 'Highest \nEvolution'),
(('Monster', 'Field'), '16'),
(('None'), 'With Stone'), #30
(('None'), 'Highest \nEvolution'),
(('Monster', 'Field'), '16'),
(('Monster', 'Field'), 'With Stone'),
(('Monster', 'Field'), 'Highest \nEvolution'),
(('Fairy'), 'With Stone'),
(('Fairy'), 'Highest \nEvolution'),
(('Field'), 'With Stone'),
(('Field'), 'Highest \nEvolution'),
(('Fairy'), 'With Stone'),
(('Fairy'), 'Highest \nEvolution'), #40
(('Flying'), '22'),
(('Flying'), 'Highest \nEvolution'),
(('Grass'), '21'),
(('Grass'), 'With Stone'),
(('Grass'), 'Highest \nEvolution'),
(('Bug', 'Grass'), '24'),
(('Bug', 'Grass'), 'Highest \nEvolution'),
(('Bug'), '31'),
(('Bug'), 'Highest \nEvolution'),
(('Field'), '26'), #50
(('Field'), 'Highest \nEvolution'),
(('Field'), '28'),
(('Field'), 'Highest \nEvolution'),
(('Water 1', 'Field'), '33'),
(('Water 1', 'Field'), 'Highest \nEvolution'),
(('Field'), '28'),
(('Field'), 'Highest \nEvolution'),
(('Field'), 'With Stone'),
(('Field'), 'Highest \nEvolution'),
(('Water 1'), '25'), #60
(('Water 1'), 'With Stone'),
(('Water 1'), 'Highest \nEvolution'),
(('Human-Like'), '16'),
(('Human-Like'), 'With Trade'),
(('Human-Like'), 'Highest \nEvolution'),
(('Human-Like'), '28'),
(('Human-Like'), 'With Trade'),
(('Human-Like'), 'Highest \nEvolution'),
(('Grass'), '21'),
(('Grass'), 'With Stone'), #70
(('Grass'), 'Highest \nEvolution'),
(('Water 3'), '30'),
(('Water 3'), 'Highest \nEvolution'),
(('Mineral'), '25'),
(('Mineral'), 'With Trade'),
(('Mineral'), 'Highest \nEvolution'),
(('Field'), '40'),
(('Field'), 'Highest \nEvolution'),
(('Monster', 'Water 1'), '37'),
(('Monster', 'Water 1'), 'Highest \nEvolution'), #80
(('Mineral'), '30'),
(('Mineral'), 'Highest \nEvolution'),
(('Flying', 'Field'), 'Highest \nEvolution'),
(('Flying'), '31'),
(('Flying'), 'Highest \nEvolution'),
(('Water 1', 'Field'), '34'),
(('Water 1', 'Field'), 'Highest \nEvolution'),
(('Amorphous'), '38'),
(('Amorphous'), 'Highest \nEvolution'),
(('Water 3'), 'With Stone'), #90
(('Water 3'), 'Highest \nEvolution'),
(('Amorphous'), '25'),
(('Amorphous'), 'With Trade'),
(('Amorphous'), 'Highest \nEvolution'),
(('Mineral'), 'Highest \nEvolution'),
(('Human-Like'), '26'),
(('Human-Like'), 'Highest \nEvolution'),
(('Water 3'), '28'),
(('Water 3'), 'Highest \nEvolution'),
(('Mineral'), '30'), #100
(('Mineral'), 'Highest \nEvolution'),
(('Grass'), 'With Stone'),
(('Grass'), 'Highest \nEvolution'),
(('Monster'), '28'),
(('Monster'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Monster'), 'Highest \nEvolution'),
(('Amorphous'), '35'),
(('Amorphous'), 'Highest \nEvolution'), #110
(('Monster', 'Field'), '42'),
(('Monster', 'Field'), 'Highest \nEvolution'),
(('Fairy'), 'Highest \nEvolution'),
(('Grass'), 'Highest \nEvolution'),
(('Monster'), 'Highest \nEvolution'),
(('Water 1', 'Dragon'), '32'),
(('Water 1', 'Dragon'), 'Highest \nEvolution'),
(('Water 2'), '33'),
(('Water 2'), 'Highest \nEvolution'),
(('Water 3'), 'With Stone'), #120
(('Water 3'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Bug'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Human-Like'), 'Highest \nEvolution'),
(('Bug'), 'Highest \nEvolution'),
(('Field'), 'Highest \nEvolution'),
(('Water 2', 'Dragon'), '20'),
(('Water 2', 'Dragon'), 'Highest \nEvolution'), #130
(('Monster', 'Water 1'), 'Highest \nEvolution'),
(('Ditto'), 'Highest \nEvolution'),
(('Field'), 'With Stone'),
(('Field'), 'Highest \nEvolution'),
(('Field'), 'Highest \nEvolution'),
(('Field'), 'Highest \nEvolution'),
(('Mineral'), 'Highest \nEvolution'),
(('Water 1', 'Water 3'), '40'),
(('Water 1', 'Water 3'), 'Highest \nEvolution'),
(('Water 1', 'Water 3'), '40'), #140
(('Water 1', 'Water 3'), 'Highest \nEvolution'),
(('Flying'), 'Highest \nEvolution'),
(('Monster'), 'Highest \nEvolution'),
(('None'), 'Highest \nEvolution'),
(('None'), 'Highest \nEvolution'),
(('None'), 'Highest \nEvolution'),
(('Water 1', 'Dragon'), '30'),
(('Water 1', 'Dragon'), '55'),
(('Water 1', 'Dragon'), 'Highest \nEvolution'),
(('None'), 'Highest \nEvolution'), #150
(('None'), 'Highest \nEvolution'),
)

desList = (
('For some time after its birth, it grows by \n gaining nourishment from the seed on its back.'),
('When the bud on its back starts swelling, \n a sweet aroma wafts to indicate the flowers coming bloom.'),
('After a rainy day, the flower on its back \n smells stronger. The scent attracts other Pokémon.'), #3
('The fire on the tip of its tail is a measure \n of its life. If healthy, its tail burns intensely.'),
('In the rocky mountains where Charmeleon live, \n their fiery tails shine at night like stars.'),
('It is said that Charizards fire burns hotter \n if it has experienced harsh battles.'),
('It shelters itself in its shell then strikes \n back with spouts of water at every opportunity.'),
('It is said to live 10,000 years. Its furry \n tail is popular as a symbol of longevity.'),
('The jets of water it spouts from the rocket \n cannons on its shell can punch through thick steel.'),
('It releases a stench from its red antenna to \n repel enemies. It grows by molting repeatedly.'),#10
('A steel-hard shell protects its tender body. \n It quietly endures hardships while awaiting evolution.'),
('It loves the honey of flowers and can locate flower \n patches that have even tiny amounts of pollen.'),
('It eats its weight in leaves every day. \n It fends off attackers with the needle on its head.'),
('While awaiting evolution, it hides from \n predators under leaves and in nooks of branches.'),
('Its best attack involves flying around at high speed, \n striking with poison needles, then flying off.'),#15
('It is docile and prefers to avoid conflict. \n If disturbed, however, it can ferociously strike back.'),
('It flies over its wide territory in search of prey, \n downing it with its highly developed claws.'),
('By flapping its wings with all its might, Pidgeot can\n make a gust of wind capable of bending tall trees.'),
('It searches for food all day. It gnaws on hard objects \n to wear down its fangs, which grow constantly during its lifetime.'),
('With its long fangs, this surprisingly violent Pokémon \n can gnaw away even thick concrete with ease.'),#20
('It flaps its small wings busily to fly. \n Using its beak, it searches in grass for prey.'),
('It has the stamina to fly all day on its \nbroad wings. It fights by using its sharp beak.'),
('It sneaks through grass without making a sound \n and strikes unsuspecting prey from behind.'),
('The pattern on its belly is for intimidation. \n It constricts foes while they are frozen in fear.'),
('It occasionally uses an electric shock to recharge \n a fellow Pikachu that is in a weakened state.'), #25
('Its tail discharges electricity into the ground, \n protecting it from getting shocked.'),
('It digs deep burrows to live in. When in danger, \n it rolls up its body to withstand attacks.'),
('The spikes on its body are made up of its hardened hide. \n It rolls up and attacks foes with its spikes.'),
('While it does not prefer to fight, even one drop of \n the poison it secretes from barbs can be fatal.'),
('When it senses danger, it raises all the barbs on its body. \n These barbs grow slower than Nidorinos.'),#30
('Its entire body is armored with hard scales. \n It will protect the young in its burrow with its life.'),
('It scans its surroundings by raising its ears out \n of the grass. Its toxic horn is for protection.'),
('It has a violent disposition and stabs foes \n with its horn, which oozes poison upon impact.'),
('One swing of its mighty tail can snap a \n telephone pole as if it were a matchstick.'),
('On nights with a full moon, Clefairy gather \n from all over and dance. Bathing in moonlight makes them float.'),#35
('Their ears are sensitive enough to hear a pin \n drop from over a mile away, so theyre usually found in quiet places.'),
('As each tail grows, its fur becomes more lustrous. \n When held, it feels slightly warm.'),
('Each of its nine tails is imbued with supernatural power, \n and it can live for a thousand years.'),
('Looking into its cute, round eyes makes it start singing \n a song so pleasant listeners cant help but fall asleep.'),
('Its fine fur feels so pleasant, those who accidentally \n touch it cannot take their hands away.'),#40
('It does not need eyes, because it emits ultrasonic \n waves to check its surroundings while it flies.'),
('Flitting around in the dead of night, it sinks its fangs \n into its prey and drains a nearly fatal amount of blood.'),
('It often plants its root feet in the ground during the day \n and sows seeds as it walks about at night.'),
('The honey it drools from its mouth smells so atrocious, \n it can curl noses more than a mile away.'),
('Its petals are the largest in the world. As it walks, \n it scatters extremely allergenic pollen.'),#45
('Mushrooms named tochukaso grow on its back. \n They grow along with the host Paras.'),
('A mushroom grown larger than the hosts body controls Parasect. \n It scatters poisonous spores.'),
('Its big eyes are actually clusters of tiny eyes. \n At night, its kind is drawn by light.'),
('It flutters its wings to scatter dustlike scales. \n The scales leach toxins if they contact skin'),
('A Pokémon that lives underground. Because of its dark habitat, \n it is repelled by bright sunlight.'),#50
('Its three heads move alternately, driving it through \n tough soil to depths of over 60 miles.'),
('It is nocturnal in nature. If it spots something \n shiny, its eyes glitter brightly.'),
('A very haughty Pokémon. Among fans, the size of \n the jewel in its forehead is a topic of much talk.'),
('When headaches stimulate its brain cells, which are \n usually inactive, it can use a mysterious power.'),
('When its forehead shines mysteriously, \n Golduck can use the full extent of its power.'),#55
('It lives in treetop colonies. If one becomes enraged, \n the whole colony rampages for no reason.'),
('It grows angry if you see its eyes and gets angrier \n if you run. If you beat it, it gets even madder.'),
('Extremely loyal to its Trainer, it will bark at those \n who approach the Trainer unexpectedly and run them out of town.'),
('The sight of it running over 6,200 miles in a single \n day and night has captivated many people.'),
('Its skin is so thin, its internal organs are visible. \n It has trouble walking on its newly grown feet.'),#60
('The spiral pattern on its belly subtly undulates. \n Staring at it gradually causes drowsiness.'),
('With its extremely tough muscles, it can keep \n swimming in the Pacific Ocean without resting.'),
('Using its psychic power is such a strain on its \n brain that it needs to sleep for 18 hours a day.'),
('It stares at its silver spoon to focus its mind. \n It emits more alpha waves while doing so.'),
('The spoons clutched in its hands are said to \n have been created by its psychic powers.'),#65
('Though small in stature, it is powerful enough to \n easily heft and throw a number of Geodude at once.'),
('It happily carries heavy cargo to toughen up. \n It willingly does hard work for people.'),
('Its four muscled arms slam foes with powerful \n punches and chops at blinding speed.'),
('It prefers hot and humid environments. \n It is quick at capturing prey with its vines.'),
('A Pokémon that appears to be a plant. It captures \n unwary prey by dousing them with a toxic powder.'),#70
('It pools in its mouth a fluid with a honey-like scent, \n which is really an acid that dissolves anything.'),
('Because its body is almost entirely composed of water, \n it shrivels up if it is washed ashore.'),
('It extends its 80 tentacles to form an encircling \n poisonous net that is difficult to escape.'),
('At rest, it looks just like a rock. Carelessly stepping \n on it will make it swing its fists angrily.'),
('It rolls on mountain paths to move. Once it builds momentum, \n no Pokémon can stop it without difficulty.'),#75
('Even dynamite cant harm its hard, boulder-like body. \n It sheds its hide just once a year.'),
('As a newborn, it can barely stand. However, \n through galloping, its legs are made tougher and faster.'),
('When at an all-out gallop, its blazing mane sparkles, \n enhancing its beautiful appearance.'),
('Although slow, it is skilled at fishing with its tail. \n It does not feel pain if its tail is bitten.'),
('Though usually dim witted, it seems to become inspired \n if the Shellder on its tail bites down.'),#80
('The electromagnetic waves emitted by the units at the \n sides of its head expel antigravity, which allows it to float.'),
('The stronger electromagnetic waves from the three linked \n Magnemite are enough to dry out surrounding moisture.'),
('It cant live without the stalk it holds. Thats why it \n defends the stalk from attackers with its life.'),
('The brains in its two heads appear to communicate \n emotions to each other with a telepathic power.'),
('When Doduo evolves into this odd breed, one of \n its heads splits into two. It runs at nearly 40 mph.'),#85
('The colder it gets, the better it feels. It joyfully \n swims around oceans so cold that they are filled with floating ice.'),
('Its streamlined body has low resistance, and it swims \n around cold oceans at a speed of eight knots.'),
('Born from sludge, these Pokémon now gather in polluted \n places and increase the bacteria in their bodies.'),
('Its so stinky! Muks body contains toxic elements, \n and any plant will wilt when it passes by.'),
('It swims backward by opening and closing its two shells. \n Its large tongue is always kept hanging out.'),#90
('It fights by keeping its shell tightly shut for \n protection and by shooting spikes to repel foes.'),
('Born from gases, anyone would faint if engulfed \n by its gaseous body, which contains poison.'),
('It likes to lurk in the dark and tap shoulders \n with a gaseous hand. Its touch causes endless shuddering.'),
('The leer that floats in darkness belongs to a \n Gengar delighting in casting curses on people.'),
('Opening its large mouth, it ingests massive \n amounts of soil and creates long tunnels.'),#95
('It can tell what people are dreaming by sniffing \n with its big nose. It loves fun dreams.'),
('Seeing its swinging pendulum can induce sleep in \n three seconds, even in someone who just woke up.'),
('It lives in burrows dug on sandy beaches. Its pincers \n fully grow back if they are broken in battle.'),
('The larger pincer has 10,000- horsepower strength. \n However, it is so heavy, it is difficult to aim.'),
('It looks just like a Poke Ball. It is dangerous \n because it may electrocute or explode on contact.'),#100
('It is known to drift on winds if it is bloated \n to bursting with stored electricity.'),
('Its six eggs converse using telepathy. \n They can quickly gather if they become separated.'),
('It is called The Walking Jungle. If a head grows too big, \n it falls off and becomes an Exeggcute.'),
('When it thinks of its dead mother, it cries. \n Its crying makes the skull it wears rattle hollowly.'),
('From its birth, this savage Pokémon constantly \nholds bones. It is skilled in using them as weapons.'),#105
('Its legs can stretch double. First-time \n foes are startled by its extensible reach.'),
('The arm-twisting punches it throws pulverize even concrete. \n It rests after three minutes of fighting.'),
('Being licked by its long, saliva-covered tongue leaves a \n tingling sensation. Extending its tongue retracts its tail.'),
('Toxic gas is held within its thin, balloon-shaped body, \n so it can cause massive explosions.'),
('Inhaling toxic fumes from trash and mixing them \n inside its body lets it spread an even fouler stench.'),#110
('Its powerful tackles can destroy anything. \n However, it is too slow witted to help people work.'),
('Standing on its hind legs freed its forelegs \n and made it smarter. It is very forgetful, however.'),
('A kindly Pokémon that lays highly nutritious eggs \n and shares them with injured Pokmon or people.'),
('Many writhing vines cover it, so its true identity \n remains unknown. The blue vines grow its whole life long.'),
('It raises its offspring in its belly pouch. \n It lets the baby out to play only when it feels safe.'),#115
('It makes its nest in the shade of corals. \n If it senses danger, it spits murky ink and flees.'),
('Its spines provide protection. Its fins and \n bones are prized as traditional-medicine ingredients.'),
('Though it appears very elegant when swimming with \n fins unfurled, it can jab powerfully with its horn.'),
('In autumn, its body becomes more fatty in preparing \n to propose to a mate. It takes on beautiful colors.'),
('As long as its red core remains, it can regenerate \n its body instantly, even if its torn apart.'),#120
('Its core shines in many colors and sends radio \n signals into space to communicate with something.'),
('It shapes an invisible wall in midair by minutely \n vibrating its fingertips to stop molecules in the air.'),
('The sharp scythes on its forearms become \n increasingly sharp by cutting through hard objects.'),
('Its cries sound like human speech. However, \n it is impossible to tell what it is trying to say.'),
('Research is progressing on storing lightning \n in Electabuzz so this energy can be used at any time.'),#125
('The scorching fire exhaled by Magmar forms heat \n waves around its body, making it hard to see the Pokémon clearly.'),
('It grips prey with its powerful pincers and will \n not let go until the prey is torn in half.'),
('Once it takes aim at its foe, it makes a headlong \n charge. It is famous for its violent nature.'),
('A Magikarp living for many years can leap \n a mountain using Splash. The move remains useless, though.'),
('Once it begins to rampage, a Gyarados will burn \n everything down, even in a harsh storm.'),#130
('Able to understand human speech and very intelligent, \n it loves to swim in the sea with people on its back.'),
('It can reconstitute its entire cellular structure \n to change into what it sees, but it returns to normal when it relaxes.'),
('Thanks to its unstable genetic makeup, this special Pokémon \n conceals many different possible evolutions.'),
('Its cell composition is similar to water molecules. \n As a result, it cant be seen when it melts away into water.'),
('By storing electricity in its body, it can shoot its \n bristlelike fur like a barrage of missiles.'),#135
('Inhaled air is carried to its flame sac, heated, \n and exhaled as fire that reaches over 3,000 degrees F.'),
('A man-made Pokémon created using advanced scientific means. \n It can move freely in cyberspace.'),
('A Pokémon that was resurrected from a fossil using modern science. \n It swam in ancient seas.'),
('It is thought that this Pokémon became extinct \n because its spiral shell grew too large.'),
('It is thought to have inhabited beaches 300 million \n years ago. It is protected by a stiff shell.'),#140
('It is thought that this Pokémon came onto land \n because its prey adapted to life on land.'),
('A Pokémon that roamed the skies in the dinosaur era. \n Its teeth are like saw blades.'),
('When its belly is full, it becomes too lethargic to \n even lift a finger, so it is safe to bounce on its belly.'),
('A legendary bird Pokémon. It can create \n blizzards by freezing moisture in the air.'),
('A legendary Pokémon that is said to live in thunderclouds. \n It freely controls lightning bolts.'),#145
('One of the legendary bird Pokémon. It is said \n that its appearance indicates the coming of spring.'),
('It is called the Mirage Pokémon because so \n few have seen it. Its shed skin has been found.'),
('If its body takes on an aura, the weather changes instantly. \n It is said to live in seas and lakes.'),
('It is said to make its home somewhere in the sea. \n It guides crews of shipwrecks to shore.'),
('A Pokémon created by recombining Mews genes. \n Its said to have the most savage heart among Pokmon.'),#150
('So rare that it is still said to be a mirage by many experts. \n Only a few people have seen it worldwide.'),
)


def loadImages():
    
    global pokemonImages
    pokemonImages = []
    pokemonImages.append(PhotoImage(file = "bulbasaur.gif")) #1
    pokemonImages.append(PhotoImage(file = "ivysaur.gif"))
    pokemonImages.append(PhotoImage(file = "venusaur.gif"))
    pokemonImages.append(PhotoImage(file = "charmander.gif"))
    pokemonImages.append(PhotoImage(file = "charmeleon.gif")) #5
    pokemonImages.append(PhotoImage(file = "charizard.gif"))
    pokemonImages.append(PhotoImage(file = "squirtle.gif"))
    pokemonImages.append(PhotoImage(file = "wartortle.gif"))
    pokemonImages.append(PhotoImage(file = "blastoise.gif"))
    pokemonImages.append(PhotoImage(file = "caterpie.gif")) #10
    pokemonImages.append(PhotoImage(file = "metapod.gif"))
    pokemonImages.append(PhotoImage(file = "butterfree.gif"))
    pokemonImages.append(PhotoImage(file = "weedle.gif"))
    pokemonImages.append(PhotoImage(file = "kakuna.gif"))
    pokemonImages.append(PhotoImage(file = "beedrill.gif")) #15
    pokemonImages.append(PhotoImage(file = "pidgey.gif"))
    pokemonImages.append(PhotoImage(file = "pidgeotto.gif"))
    pokemonImages.append(PhotoImage(file = "pidgeot.gif"))
    pokemonImages.append(PhotoImage(file = "rattata.gif"))
    pokemonImages.append(PhotoImage(file = "raticate.gif")) #20
    pokemonImages.append(PhotoImage(file = "spearow.gif"))
    pokemonImages.append(PhotoImage(file = "fearow.gif"))
    pokemonImages.append(PhotoImage(file = "ekans.gif"))
    pokemonImages.append(PhotoImage(file = "arbok.gif"))
    pokemonImages.append(PhotoImage(file = "pikachu.gif")) #25
    pokemonImages.append(PhotoImage(file = "raichu.gif"))
    pokemonImages.append(PhotoImage(file = "sandshrew.gif"))
    pokemonImages.append(PhotoImage(file = "sandslash.gif"))
    pokemonImages.append(PhotoImage(file = "nidoranf.gif"))
    pokemonImages.append(PhotoImage(file = "nidorina.gif")) #30
    pokemonImages.append(PhotoImage(file = "nidoqueen.gif"))
    pokemonImages.append(PhotoImage(file = "nidoranm.gif"))
    pokemonImages.append(PhotoImage(file = "nidorino.gif"))
    pokemonImages.append(PhotoImage(file = "nidoking.gif"))
    pokemonImages.append(PhotoImage(file = "clefairy.gif")) #35
    pokemonImages.append(PhotoImage(file = "clefable.gif"))
    pokemonImages.append(PhotoImage(file = "vulpix.gif"))
    pokemonImages.append(PhotoImage(file = "ninetales.gif"))
    pokemonImages.append(PhotoImage(file = "jigglypuff.gif"))
    pokemonImages.append(PhotoImage(file = "wigglytuff.gif")) #40
    pokemonImages.append(PhotoImage(file = "zubat.gif"))
    pokemonImages.append(PhotoImage(file = "golbat.gif"))
    pokemonImages.append(PhotoImage(file = "oddish.gif"))
    pokemonImages.append(PhotoImage(file = "gloom.gif"))
    pokemonImages.append(PhotoImage(file = "vileplume.gif")) #45
    pokemonImages.append(PhotoImage(file = "paras.gif"))
    pokemonImages.append(PhotoImage(file = "parasect.gif"))
    pokemonImages.append(PhotoImage(file = "venonat.gif"))
    pokemonImages.append(PhotoImage(file = "venomoth.gif"))
    pokemonImages.append(PhotoImage(file = "diglett.gif")) #50
    pokemonImages.append(PhotoImage(file = "dugtrio.gif"))
    pokemonImages.append(PhotoImage(file = "meowth.gif"))
    pokemonImages.append(PhotoImage(file = "persian.gif"))
    pokemonImages.append(PhotoImage(file = "psyduck.gif"))
    pokemonImages.append(PhotoImage(file = "golduck.gif")) #55
    pokemonImages.append(PhotoImage(file = "mankey.gif"))
    pokemonImages.append(PhotoImage(file = "primeape.gif"))
    pokemonImages.append(PhotoImage(file = "growlithe.gif"))
    pokemonImages.append(PhotoImage(file = "arcanine.gif"))
    pokemonImages.append(PhotoImage(file = "poliwag.gif")) #60
    pokemonImages.append(PhotoImage(file = "poliwhirl.gif"))
    pokemonImages.append(PhotoImage(file = "poliwrath.gif"))
    pokemonImages.append(PhotoImage(file = "abra.gif"))
    pokemonImages.append(PhotoImage(file = "kadabra.gif"))
    pokemonImages.append(PhotoImage(file = "alakazam.gif")) #65
    pokemonImages.append(PhotoImage(file = "machop.gif")) 
    pokemonImages.append(PhotoImage(file = "machoke.gif"))
    pokemonImages.append(PhotoImage(file = "machamp.gif"))
    pokemonImages.append(PhotoImage(file = "bellsprout.gif"))
    pokemonImages.append(PhotoImage(file = "weepinbell.gif")) #70
    pokemonImages.append(PhotoImage(file = "victreebel.gif"))
    pokemonImages.append(PhotoImage(file = "tentacool.gif"))
    pokemonImages.append(PhotoImage(file = "tentacruel.gif"))
    pokemonImages.append(PhotoImage(file = "geodude.gif"))
    pokemonImages.append(PhotoImage(file = "graveler.gif")) #75
    pokemonImages.append(PhotoImage(file = "golem.gif"))
    pokemonImages.append(PhotoImage(file = "ponyta.gif"))
    pokemonImages.append(PhotoImage(file = "rapidash.gif"))
    pokemonImages.append(PhotoImage(file = "slowpoke.gif"))
    pokemonImages.append(PhotoImage(file = "slowbro.gif")) #80
    pokemonImages.append(PhotoImage(file = "magnemite.gif"))
    pokemonImages.append(PhotoImage(file = "magneton.gif"))
    pokemonImages.append(PhotoImage(file = "farfetchd.gif"))
    pokemonImages.append(PhotoImage(file = "doduo.gif"))
    pokemonImages.append(PhotoImage(file = "dodrio.gif")) #85
    pokemonImages.append(PhotoImage(file = "seel.gif"))
    pokemonImages.append(PhotoImage(file = "dewgong.gif"))
    pokemonImages.append(PhotoImage(file = "grimer.gif"))
    pokemonImages.append(PhotoImage(file = "muk.gif"))
    pokemonImages.append(PhotoImage(file = "shellder.gif")) #90
    pokemonImages.append(PhotoImage(file = "cloyster.gif"))
    pokemonImages.append(PhotoImage(file = "gastly.gif"))
    pokemonImages.append(PhotoImage(file = "haunter.gif"))
    pokemonImages.append(PhotoImage(file = "gengar.gif"))
    pokemonImages.append(PhotoImage(file = "onix.gif")) #95
    pokemonImages.append(PhotoImage(file = "drowzee.gif"))
    pokemonImages.append(PhotoImage(file = "hypno.gif"))
    pokemonImages.append(PhotoImage(file = "krabby.gif"))
    pokemonImages.append(PhotoImage(file = "kingler.gif"))
    pokemonImages.append(PhotoImage(file = "voltorb.gif")) #100
    pokemonImages.append(PhotoImage(file = "electrode.gif"))
    pokemonImages.append(PhotoImage(file = "exeggcute.gif"))
    pokemonImages.append(PhotoImage(file = "exeggutor.gif"))
    pokemonImages.append(PhotoImage(file = "cubone.gif"))
    pokemonImages.append(PhotoImage(file = "marowak.gif")) #105
    pokemonImages.append(PhotoImage(file = "hitmonlee.gif"))
    pokemonImages.append(PhotoImage(file = "hitmonchan.gif"))
    pokemonImages.append(PhotoImage(file = "lickitung.gif"))
    pokemonImages.append(PhotoImage(file = "koffing.gif"))
    pokemonImages.append(PhotoImage(file = "weezing.gif")) #110
    pokemonImages.append(PhotoImage(file = "rhyhorn.gif"))
    pokemonImages.append(PhotoImage(file = "rhydon.gif"))
    pokemonImages.append(PhotoImage(file = "chansey.gif"))
    pokemonImages.append(PhotoImage(file = "tangela.gif"))
    pokemonImages.append(PhotoImage(file = "kangaskhan.gif")) #115
    pokemonImages.append(PhotoImage(file = "horsea.gif"))
    pokemonImages.append(PhotoImage(file = "seadra.gif"))
    pokemonImages.append(PhotoImage(file = "goldeen.gif"))
    pokemonImages.append(PhotoImage(file = "seaking.gif"))
    pokemonImages.append(PhotoImage(file = "staryu.gif")) #120
    pokemonImages.append(PhotoImage(file = "starmie.gif")) 
    pokemonImages.append(PhotoImage(file = "mr-mime.gif"))
    pokemonImages.append(PhotoImage(file = "scyther.gif"))
    pokemonImages.append(PhotoImage(file = "jynx.gif"))
    pokemonImages.append(PhotoImage(file = "electabuzz.gif")) #125
    pokemonImages.append(PhotoImage(file = "magmar.gif")) 
    pokemonImages.append(PhotoImage(file = "pinsir.gif"))
    pokemonImages.append(PhotoImage(file = "tauros.gif"))
    pokemonImages.append(PhotoImage(file = "magikarp.gif"))
    pokemonImages.append(PhotoImage(file = "gyarados.gif")) #130
    pokemonImages.append(PhotoImage(file = "lapras.gif")) 
    pokemonImages.append(PhotoImage(file = "ditto.gif"))
    pokemonImages.append(PhotoImage(file = "eevee.gif"))
    pokemonImages.append(PhotoImage(file = "vaporeon.gif"))
    pokemonImages.append(PhotoImage(file = "jolteon.gif")) #135
    pokemonImages.append(PhotoImage(file = "flareon.gif"))
    pokemonImages.append(PhotoImage(file = "porygon.gif"))
    pokemonImages.append(PhotoImage(file = "omanyte.gif"))
    pokemonImages.append(PhotoImage(file = "omastar.gif"))
    pokemonImages.append(PhotoImage(file = "kabuto.gif")) #140
    pokemonImages.append(PhotoImage(file = "kabutops.gif"))
    pokemonImages.append(PhotoImage(file = "aerodactyl.gif"))
    pokemonImages.append(PhotoImage(file = "snorlax.gif"))
    pokemonImages.append(PhotoImage(file = "articuno.gif"))
    pokemonImages.append(PhotoImage(file = "zapdos.gif")) #145
    pokemonImages.append(PhotoImage(file = "moltres.gif")) 
    pokemonImages.append(PhotoImage(file = "dratini.gif"))
    pokemonImages.append(PhotoImage(file = "dragonair.gif"))
    pokemonImages.append(PhotoImage(file = "dragonite.gif"))
    pokemonImages.append(PhotoImage(file = "mewtwo.gif")) #150
    pokemonImages.append(PhotoImage(file = "mew.gif"))

#===============================================================
def runWindow(winWidth = 800, winHeight = 600):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    root.title("Pokedex")

    loadImages()

    scrollbar = Scrollbar(root, bd=0)
    Button(root, text = "CLOSE THE POKEDEX", command=root.destroy).pack(fill=X)
    pokelist = Listbox(root, yscrollcommand = scrollbar.set, selectmode=BROWSE)
    for i in pokemonList:
        pokelist.insert(END, i[0] + " " + i[1])
    scrollbar.config(command=pokelist.yview)
    scrollbar.pack(side=LEFT, fill=Y)
    pokelist.pack(side=LEFT, fill=Y)

#=================================================Aesthetics

    def filtertext(self, *args):
        nonlocal narrow
        pokelist.delete(0, END)
        for i in pokemonList:
            if narrow.get().lower() in i[1].lower():
                pokelist.insert(END, i[0] + " " + i[1])
 #===============================================================
    
    narrow = StringVar()
    narrow.set("")
    narrow.trace("w", filtertext)
    textfilter = Entry(root, textvariable=narrow)
    #l = Label(textfilter, text="Filter by name")
    #l.pack()
    textfilter.pack()

    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack(side=RIGHT, fill=BOTH)
    
    bgImage = PhotoImage(file = "Pokedex BG copy.png")
    canvas.create_image(0, 0,anchor = NW, image = bgImage)
    
    number = canvas.create_text(120, 35, font="Verdana 30 bold", text="#000", fill = "white")

    canvas.create_line(40, 60, 200, 60, width=4, fill = "white")
    canvas.create_line(300, 60, 700, 60, width=3, fill = "white")
    
    name = canvas.create_text(500, 35, font="Verdana 30 bold", text="Pokemon Name", fill = "white")

    category = canvas.create_text(130, 120, font="Verdana 14 bold", text='', fill = "white")
    
    image = canvas.create_image(500, 120,anchor = N, image = PhotoImage(file="Who-is-that-pokemon.png"))

    canvas.create_text(60, 180, font="Verdana 12", text="Type:", fill = "white")
    types = canvas.create_text(130, 180, font="Verdana 12", text="", anchor=W, fill = "white")
    
    canvas.create_text(70, 260, font="Verdana 12", text="Evolve\nLevel:", fill = "white")
    evolve = canvas.create_text(170, 260, font="Verdana 12 italic", text='', fill = "white")
    
    canvas.create_text(70, 340, font="Verdana 12", text="Egg\nGroups:", fill = "white")
    eggGroups = canvas.create_text(140, 340, font="Verdana 12 italic", text='', fill = "white")
    
    canvas.create_text(90, 530, font="Verdana 12", text="Pokedex\nDescription:", fill = "white")
    des = canvas.create_text(430, 530, font="Verdana 12 italic", text='', fill = "white")
    
    canvas.create_text(400, 580, font="Verdana 8", text="All content is owned by Nintendo, Game Freak, and The Pokemon Company", fill = "white")
#================================================

    def findpokemon():
        curselect = pokelist.curselection()[0]
        pokeindex = -1
        for i in range(len(pokemonList)):
            if pokelist.get(curselect)[:4] == pokemonList[i][0]:
                pokeindex = i
                break
        return pokeindex
#===================================    
    def displayinfo(event):
        current = findpokemon()
        if(current == -1):
            return
        
    
        nonlocal number
        nonlocal name
        nonlocal types
        canvas.delete(number)
        canvas.delete(name)
        canvas.delete(types)
        number = canvas.create_text(120, 35, font="Verdana 30 bold", text=pokemonList[current][0],
            fill = "white")
        name = canvas.create_text(500, 35, font="Verdana 30 bold", text=pokemonList[current][1],
            fill = "white")
        
        nonlocal image
        canvas.delete(image)
        image = canvas.create_image(500, 120,anchor = N, image = pokemonImages[current])
        
        typetext = ""
        if len(pokemonList[current][2]) == 2:
            typetext = pokemonList[current][2][0] + "/" + pokemonList[current][2][1]
        else:
            typetext = pokemonList[current][2]

        types = canvas.create_text(130, 180, font="Verdana 12", text=typetext, anchor=W, 
            fill = "white")

        nonlocal evolve
        canvas.delete(evolve)
        evolve = canvas.create_text(170, 260, font="Verdana 12", text=eggEvolveList[current][1],
            fill = "white")
        
        nonlocal eggGroups
        canvas.delete(eggGroups)
        eggtext = ""
        if len(eggEvolveList[current][0]) == 2:
            eggtext = eggEvolveList[current][0][0] + "/" + eggEvolveList[current][0][1]
        else:
            eggtext = eggEvolveList[current][0]
        
        eggGroups = canvas.create_text(140, 340, font="Verdana 12", text=eggtext, anchor=W, 
            fill = "white")
        
        nonlocal category
        canvas.delete(category)
        category  = canvas.create_text(130, 120, font="Verdana 14 bold", text=categoryList[current], fill = "white")
        
        nonlocal des
        canvas.delete(des)
        des = canvas.create_text(430, 530, font="Verdana 12 italic", text=desList[current], 
            fill = "white")
#================================================
    
    pokelist.bind("<<ListboxSelect>>", displayinfo)
    root.mainloop()

def main():
    runWindow()

if __name__ == '__main__':
    main()
