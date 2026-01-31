# f1-stats
A cli tool to fetch different statistics about formula 1 using [f1db](https://github.com/f1db/f1db)

## Features
You can fetch plenty of different tables and statistics: 

- Season tables (driver/constructor standings) in [wikipedia like style](https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship#World_Drivers'_Championship_standings)

- Detailed info about season races, qualifications, pit stop times

- circuits all time records: best lap times, best qualification times, driver with most wins, most podiums. 

## Examples

```sh
# The season tables
python f1.py season 2023 --flags >> README.md
```

| pos | name             | 🇧🇭 BHR | 🇸🇦 SAU | 🇦🇺 AUS | 🇦🇿 AZE | 🇺🇸 MIA | 🇲🇨 MCO | 🇪🇸 ESP | 🇨🇦 CAN | 🇦🇹 AUT | 🇬🇧 GBR | 🇭🇺 HUN | 🇧🇪 BEL | 🇳🇱 NLD | 🇮🇹 ITA | 🇸🇬 SGP | 🇯🇵 JPN | 🇶🇦 QAT | 🇺🇸 USA | 🇲🇽 MEX | 🇧🇷 SAO | 🇺🇸 LAS | 🇦🇪 ABD | pts |
|-----|------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|-----|
| 1   | Max Verstappen   | 1ᵖ     | 2ᶠ     | 1ᵖ     | 2      | 1ᶠ     | 1ᵖ     | 1ᵖᶠ    | 1ᵖ     | 1ᵖᶠ    | 1ᵖᶠ    | 1ᶠ     | 1      | 1ᵖ     | 1      | 5      | 1ᵖᶠ    | 1ᵖᶠ    | 1      | 1      | 1ᵖ     | 1      | 1ᵖᶠ    | 575 |
| 2   | Sergio Pérez     | 2      | 1ᵖ     | 5ᶠ     | 1      | 2ᵖ     | 16     | 4      | 6ᶠ     | 3      | 6      | 3      | 2      | 4      | 2      | 8      | DNF    | 10     | 4      | DNF    | 4      | 3      | 4      | 285 |
| 3   | Lewis Hamilton   | 5      | 5      | 2      | 6      | 6      | 4ᶠ     | 2      | 3      | 8      | 3      | 4ᵖ     | 4ᶠ     | 6      | 6      | 3ᶠ     | 5      | DNF    | DSQ    | 2ᶠ     | 8      | 7      | 9      | 234 |
| 4   | Charles Leclerc  | DNF    | 7      | DNF    | 3ᵖ     | 7      | 6      | 11     | 4      | 2      | 9      | 7      | 3ᵖ     | DNF    | 4      | 4      | 4      | 5      | DSQᵖ   | 3ᵖ     | DNS    | 2ᵖ     | 2      | 206 |
| 5   | Fernando Alonso  | 3      | 3      | 3      | 4      | 3      | 2      | 7      | 2      | 5      | 7      | 9      | 5      | 2ᶠ     | 9      | 15     | 8      | 6      | DNF    | DNF    | 3      | 9      | 7      | 206 |
| 6   | Lando Norris     | 17     | 17     | 6      | 9      | 17     | 9      | 17     | 13     | 4      | 2      | 2      | 7      | 7      | 8      | 2      | 2      | 3      | 2      | 5      | 2ᶠ     | DNF    | 5      | 205 |
| 7   | Carlos Sainz Jr. | 4      | 6      | 12     | 5      | 5      | 8      | 5      | 5      | 6      | 10     | 8      | DNF    | 5      | 3ᵖ     | 1ᵖ     | 6      | DNS    | 3      | 4      | 6      | 6      | 18     | 200 |
| 8   | George Russell   | 7      | 4      | DNF    | 8ᶠ     | 4      | 5      | 3      | DNF    | 7      | 5      | 6      | 6      | 17     | 5      | 16     | 7      | 4      | 5      | 6      | DNF    | 8      | 3      | 175 |
| 9   | Oscar Piastri    | DNF    | 15     | 8      | 11     | 19     | 10     | 13     | 11     | 16     | 4      | 5      | DNF    | 9      | 12ᶠ    | 7      | 3      | 2      | DNF    | 8      | 14     | 10ᶠ    | 6      | 97  |
| 10  | Lance Stroll     | 6      | DNF    | 4      | 7      | 12     | DNF    | 6      | 9      | 9      | 14     | 10     | 9      | 11     | 16     | DNS    | DNF    | 11     | 7      | 17     | 5      | 5      | 10     | 74  |
| 11  | Pierre Gasly     | 9      | 9      | 13     | 14     | 8      | 7      | 10     | 12     | 10     | 18     | DNF    | 11     | 3      | 15     | 6      | 10     | 12     | 6      | 11     | 7      | 11     | 13     | 62  |
| 12  | Esteban Ocon     | DNF    | 8      | 14     | 15     | 9      | 3      | 8      | 8      | 14     | DNF    | DNF    | 8      | 10     | DNF    | DNF    | 9      | 7      | DNF    | 10     | 10     | 4      | 12     | 58  |
| 13  | Alexander Albon  | 10     | DNF    | DNF    | 12     | 14     | 14     | 16     | 7      | 11     | 8      | 11     | 14     | 8      | 7      | 11     | DNF    | 13     | 9      | 9      | DNF    | 12     | 14     | 27  |
| 14  | Yuki Tsunoda     | 11     | 11     | 10     | 10     | 11     | 15     | 12     | 14     | 19     | 16     | 15     | 10     | 15     | DNS    | DNF    | 12     | 15     | 8ᶠ     | 12     | 9      | 18     | 8      | 17  |
| 15  | Valtteri Bottas  | 8      | 18     | 11     | 18     | 13     | 11     | 19     | 10     | 15     | 12     | 12     | 12     | 14     | 10     | DNF    | DNF    | 8      | 12     | 15     | DNF    | 17     | 19     | 10  |
| 16  | Nico Hülkenberg  | 15     | 12     | 7      | 17     | 15     | 17     | 15     | 15     | DNF    | 13     | 14     | 18     | 12     | 17     | 13     | 14     | 16     | 11     | 13     | 12     | 19     | 15     | 9   |
| 17  | Daniel Ricciardo |        |        |        |        |        |        |        |        |        |        | 13     | 16     |        |        |        |        |        | 15     | 7      | 13     | 14     | 11     | 6   |
| 18  | Guanyu Zhou      | 16ᶠ    | 13     | 9      | DNF    | 16     | 13     | 9      | 16     | 12     | 15     | 16     | 13     | DNF    | 14     | 12     | 13     | 9      | 13     | 14     | DNF    | 15     | 17     | 6   |
| 19  | Kevin Magnussen  | 13     | 10     | 17     | 13     | 10     | 19     | 18     | 17     | 18     | DNF    | 17     | 15     | 16     | 18     | 10     | 15     | 14     | 14     | DNF    | DNF    | 13     | 20     | 3   |
| 20  | Liam Lawson      |        |        |        |        |        |        |        |        |        |        |        |        | 13     | 11     | 9      | 11     | 17     |        |        |        |        |        | 2   |
| 21  | Logan Sargeant   | 12     | 16     | 16     | 16     | 20     | 18     | 20     | DNF    | 13     | 11     | 18     | 17     | DNF    | 13     | 14     | DNF    | DNF    | 10     | 16     | 11     | 16     | 16     | 1   |
| 22  | Nyck de Vries    | 14     | 14     | 15     | DNF    | 18     | 12     | 14     | 18     | 17     | 17     |        |        |        |        |        |        |        |        |        |        |        |        | 0   |

```sh
# Season overview (different statistics)
python f1.py driver fernando-alonso 2012 -o
```

```
Season overview — fernando-alonso (2012)
--------------------------------------------------
Races: 20  Finished: 18  Not finished/started: 2  (rate: 10.0%)

Points
- Total pts: 278 pts (2 place)
- Team pts share: 69.50%
- Pts per race: 13.90 pts
- Avg pts when scoring: 15.44 pts
- Points volatility (std): 7.59 pts

Qualifying & starts
- Poles: 2  (Pole rate: 10.0%)
- Q1, Q2 eliminations: 3 (rate: 15.0%)
- Q3 appearances: 17
- Pole conversion (poles / Q3s): 11.8%
- Avg grid position: 6.10
- Median grid position: 6.00
- Most common grid position: 2
- Penalties: 0

Results & rates
- Wins: 3  (Win rate: 15.0%)
- Podiums: 13  (Podium rate: 65.0%)
- Scoring finishes: 18  (Scoring rate: 90.0%)
- Fastest laps: 0  (Fastest-lap rate: 0.0%)
- Finish rate: 90.0%
- Avg finish position: 3.28
- Median finish position: 3.00
- Most common finish position: 2
- Finish position CV (coefficient of variation): 0.660

Pit stops & strategy
- Avg pit stops per race: 1.94
- Avg pit stops time: 21.91s
- Problematic pit stops: 0

Not started/finished/classified, disqualified:
- DNF: 2 (10.0%)
  * belgium - Collision
  * japan - Collision
- DNS: 0 (0.0%)
- DSQ: 0 (0.0%)
- NC: 0 (0.0%)

Race progress
- Avg positions gained per race: 3.47
- Races net gain: 72.2%
- Races net loss: 11.1%
- Races no change: 16.7%
- Longest podium streak: 5
  * (2012, 'korea') ... (2012, 'brazil')
- Longest win streak: 1
  * (2012, 'malaysia') ... (2012, 'malaysia')
- Longest points streak: 11
  * (2012, 'australia') ... (2012, 'hungary')
```

```sh
# All time overview
python f1.py driver fernando-alonso -o
```

```
 python f1.py driver fernando-alonso -o

Season overview — fernando-alonso (All time)
--------------------------------------------------
Races: 428  Finished: 353  Not finished/started: 75  (rate: 17.5%)

Points
- Total pts: 2393 pts (10 place)
- Team pts share: 70.44%
- Pts per race: 5.59 pts
- Avg pts when scoring: 8.52 pts
- Points volatility (std): 6.20 pts

Qualifying & starts
- Poles: 22  (Pole rate: 5.1%)
- Q1, Q2 eliminations: 187 (rate: 43.7%)
- Q3 appearances: 241
- Pole conversion (poles / Q3s): 9.1%
- Avg grid position: 8.68
- Median grid position: 8.00
- Most common grid position: 2
- Penalties: 7

Results & rates
- Wins: 32  (Win rate: 7.5%)
- Podiums: 106  (Podium rate: 24.8%)
- Scoring finishes: 281  (Scoring rate: 65.7%)
- Fastest laps: 26  (Fastest-lap rate: 6.1%)
- Finish rate: 82.5%
- Avg finish position: 6.67
- Median finish position: 6.00
- Most common finish position: 2
- Finish position CV (coefficient of variation): 0.660

Pit stops & strategy
- Avg pit stops per race: 2.00
- Avg pit stops time: 24.65s
- Problematic pit stops: 34

Not started/finished/classified, disqualified:
- DNF: 73 (17.1%)
  * brazil - Electrical
  * san-marino - Brakes
  * austria - Gearbox
  * monaco - Gearbox
  * canada - Transmission
  * hungary - Brakes
  * belgium - Gearbox
  * united-states - Driveshaft
  * austria - Engine
  * france - Engine
  * great-britain - Gearbox
  * united-states - Engine
  * japan - Engine
  * monaco - Accident
  * canada - Driveshaft
  * united-states - Puncture
  * belgium - Engine
  * italy - Spun off
  * canada - Suspension
  * hungary - Wheel nut
  * italy - Engine
  * japan - Accident
  * spain - Engine
  * canada - Spun off
  * europe - Collision damage
  * hungary - Wheel
  * belgium - Wheel
  * brazil - Collision
  * belgium - Accident
  * canada - Collision
  * belgium - Collision
  * japan - Collision
  * malaysia - Collision damage
  * italy - Engine
  * japan - Electrical
  * malaysia - Power unit
  * spain - Brakes
  * monaco - Gearbox
  * canada - Exhaust
  * austria - Collision
  * singapore - Gearbox
  * mexico - Power unit
  * australia - Collision
  * spain - Power unit
  * europe - Gearbox
  * australia - Broken floor
  * china - Driveshaft
  * austria - Collision damage
  * great-britain - Fuel pump
  * belgium - Power unit
  * singapore - Collision damage
  * united-states - Engine
  * monaco - Gearbox
  * canada - Exhaust
  * belgium - Collision
  * italy - Electrical
  * united-states - Collision
  * mexico - Water pressure
  * bahrain - Brakes
  * united-states - Rear wing
  * saudi-arabia - Water pressure
  * emilia-romagna - Collision damage
  * italy - Water pressure
  * singapore - Engine
  * abu-dhabi - Water leak
  * united-states - Undertray
  * mexico - Collision damage
  * mexico - Brakes
  * australia - Accident
  * china - Brakes
  * monaco - Engine
  * italy - Suspension
  * mexico - Brakes
- DNS: 2 (0.5%)
  * united-states - Withdrew
  * russia - Gearbox
- DSQ: 0 (0.0%)
- NC: 0 (0.0%)

Race progress
- Avg positions gained per race: 1.92
- Races net gain: 60.3%
- Races net loss: 24.4%
- Races no change: 15.3%
- Longest podium streak: 15
  * (2005, 'turkey') ... (2006, 'canada')
- Longest win streak: 4
  * (2006, 'spain') ... (2006, 'canada')
- Longest points streak: 23
  * (2011, 'europe') ... (2012, 'hungary')
```

```sh
# Circuit records
python f1.py circuit monza --best-lap --rows=5
```

```
|   | year | driver             | finish | lap | time     | tyre        | engine     | constructor |
|---|------|--------------------|--------|-----|----------|-------------|------------|-------------|
| 1 | 2025 | Lando Norris       | 2      | 53  | 1:20.901 | pirelli     | mercedes   | mclaren     |
| 2 | 2025 | Max Verstappen     | 1      | 52  | 1:21.003 | pirelli     | honda-rbpt | red-bull    |
| 3 | 2004 | Rubens Barrichello | 1      | 41  | 1:21.046 | bridgestone | ferrari    | ferrari     |
| 4 | 2025 | Oscar Piastri      | 3      | 47  | 1:21.245 | pirelli     | mercedes   | mclaren     |
| 5 | 2025 | Charles Leclerc    | 4      | 53  | 1:21.294 | pirelli     | ferrari    | ferrari     |
```

```sh
# You can also chain flags
python f1.py driver max-verstappen 2025 --pit-stops --sprints
```
```
|                | pit 1           | pit 2           | pit 3           | pit 4           | pit 5           |   |
|----------------|-----------------|-----------------|-----------------|-----------------|-----------------|---|
| Australia      | lap 2 - 13.416  | lap 3 - 13.740  | lap 4 - 12.938  | lap 34 - 18.700 | lap 46 - 18.721 | 5 |
| China          | lap 13 - 22.454 |                 |                 |                 |                 | 1 |
| Japan          | lap 21 - 24.397 |                 |                 |                 |                 | 1 |
| Bahrain        | lap 10 - 26.518 | lap 26 - 28.067 |                 |                 |                 | 2 |
| Saudi Arabia   | lap 21 - 26.030 |                 |                 |                 |                 | 1 |
| Miami          | lap 26 - 22.501 |                 |                 |                 |                 | 1 |
| Emilia Romagna | lap 29 - 29.991 | lap 46 - 29.657 |                 |                 |                 | 2 |
| Monaco         | lap 28 - 24.114 | lap 77 - 23.950 |                 |                 |                 | 2 |
| Spain          | lap 13 - 21.869 | lap 29 - 21.933 | lap 47 - 21.802 | lap 55 - 22.197 |                 | 4 |
| Canada         | lap 12 - 23.604 | lap 37 - 23.121 |                 |                 |                 | 2 |
| Great Britain  | lap 11 - 28.182 | lap 41 - 29.689 |                 |                 |                 | 2 |
| Belgium        | lap 12 - 25.913 |                 |                 |                 |                 | 1 |
| Hungary        | lap 17 - 21.433 | lap 48 - 21.258 |                 |                 |                 | 2 |
| Netherlands    | lap 23 - 18.740 | lap 53 - 18.261 |                 |                 |                 | 2 |
| Italy          | lap 37 - 24.545 |                 |                 |                 |                 | 1 |
| Azerbaijan     | lap 40 - 20.221 |                 |                 |                 |                 | 1 |
| Singapore      | lap 19 - 24.008 |                 |                 |                 |                 | 1 |
| United States  | lap 33 - 23.987 |                 |                 |                 |                 | 1 |
| Mexico         | lap 37 - 22.762 |                 |                 |                 |                 | 1 |
| São Paulo      | lap 7 - 23.197  | lap 34 - 23.058 | lap 54 - 23.311 |                 |                 | 3 |
| Las Vegas      | lap 25 - 21.708 |                 |                 |                 |                 | 1 |
| Qatar          | lap 7 - 29.970  | lap 32 - 28.168 |                 |                 |                 | 2 |
| Abu Dhabi      | lap 23 - 21.703 |                 |                 |                 |                 | 1 |


| name          | q1       | q2       | q3       | gap    | interval | laps | start | finish | gained | penalty | gap     | interval | pts |
|---------------|----------|----------|----------|--------|----------|------|-------|--------|--------|---------|---------|----------|-----|
| China         | 1:31.916 | 1:31.521 | 1:30.867 | +0.018 | +0.018   | 12   | 2     | 3      | -1     |         | +9.804  | +2.915   | 6   |
| Miami         | 1:27.953 | 1:27.245 | 1:26.737 | +0.255 | +0.155   | 16   | 4     | 17     | -13    | 10.000  | +12.059 | +2.150   |     |
| Belgium       | 1:42.043 | 1:41.583 | 1:40.987 | +0.477 | +0.477   | 9    | 2     | 1      | 1      |         |         |          | 8   |
| United States | 1:33.363 | 1:33.163 | 1:32.143 |        |          | 12   | 1     | 1      | 0      |         |         |          | 8   |
| São Paulo     | 1:09.975 | 1:09.707 | 1:09.580 | +0.337 | +0.084   | 15   | 6     | 4      | 2      |         | +4.423  | +2.105   | 5   |
| Qatar         | 1:21.172 | 1:21.036 | 1:20.528 | +0.473 | +0.009   | 20   | 6     | 4      | 2      |         | +9.054  | +2.775   | 5   |
```

## Installation

```sh
git clone https://github.com/cebem1nt/f1-stats.git
cd f1-stats
./init # Set up the db
```

## Misc

```
python f1.py --help #You can also use --help for each subcommand:
usage: f1 [-h] [--double-headers] [--no-delimiters] [--adjustment {left,center,right}] {circuit,driver,gp,season,db} ...

Diferrent charts, statistics, records, all time bests of Formula One

positional arguments:
  {circuit,driver,gp,season,db}
                        Available commands
    circuit             Get different records for a circuit
    driver              Different driver's statistics, data over the season or all time
    gp                  Grand prix results tables
    season              Fancy wikipedia like season table for driver/constructor championship
    db                  Different database related commands

options:
  -h, --help            show this help message and exit
  --double-headers      Print table headers twice (at the top and bottom)
  --no-delimiters       Do not print any separators for tables
  --adjustment {left,center,right}
                        Table text alignment
```
