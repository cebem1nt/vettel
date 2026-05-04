# vettel
A cli tool to fetch different statistics and info about formula 1 using [f1db](https://github.com/f1db/f1db)

## Features

- **Drivers statistics during year/all time: total points, poles, q3 apearences, average points, grid positions, diferent rates, streaks and much more**

- **Season tables (driver/constructor standings) in [wikipedia like style](https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship#World_Drivers'_Championship_standings)**

- **Detailed info about season races, sprints, qualifications**

- **Pit stop times**

- **Season calendar**

- **Circuits all time records: best lap times, best qualification times, driver with most wins, most podiums.**

- **Fully offline: Info fetched from local database**

## Examples

Season results table
```sh
python vet.py season 2023 --flags >> README.md
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

Race results:
```sh
python vet.py race japan 2026 # pass --full to get more info
```
```
  Driver              Finish    Points

  Kimi Antonelli      1         25
  Oscar Piastri       2 (+1)    18
  Charles Leclerc     3 (+1)    15
  George Russell      4 (-2)    12
  Lando Norris        5         10
  Lewis Hamilton      6         8
  Pierre Gasly        7         6
  Max Verstappen      8 (+3)    4
  Liam Lawson         9 (+5)    2
  Esteban Ocon        10 (+2)   1
  Nico Hülkenberg     11 (+2)
  Isack Hadjar        12 (-4)
  Gabriel Bortoleto   13 (-4)
  Arvid Lindblad      14 (-4)
  Carlos Sainz Jr.    15 (+1)
  Franco Colapinto    16 (-1)
  Sergio Pérez        17 (+2)
  Fernando Alonso     18 (+3)
  Valtteri Bottas     19 (+1)
  Alexander Albon     20 (-3)
  Lance Stroll        DNF
  Oliver Bearman      DNF

Fastest lap: Kimi Antonelli - 1:32.432 (lap 49)
Pole position: Kimi Antonelli

--------------------------------------------------
Lance Stroll - Reason retired: Mechanical
Oliver Bearman - Reason retired: Accident
```

```sh
# Get 2023 max verstappen overview/statistics:
python3 vet.py driver max-verstappen 2023
```
```
Season overview — max-verstappen (2023)
--------------------------------------------------
Races: 22  Finished: 22  Not finished/started: 0  (rate: 0.0%)

Points
- Total pts: 575 pts (1 place)
- Team pts share: 66.86%
- Pts per race: 26.14 pts
- Avg pts when scoring: 26.14 pts
- Points volatility (std): 3.78 pts

Qualifying & starts
- Poles: 12  (Pole rate: 54.5%)
- Q1, Q2 eliminations: 3 (rate: 13.6%)
- Q3 appearances: 19
- Pole conversion (poles / Q3s): 63.2%
- Avg grid position: 3.18
- Median grid position: 1.00
- Most common grid position: 1
- Penalties: 0

Results & rates
- Wins: 19  (Win rate: 86.4%)
- Podiums: 21  (Podium rate: 95.5%)
- Scoring finishes: 22  (Scoring rate: 100.0%)
- Fastest laps: 9  (Fastest-lap rate: 40.9%)
- Finish rate: 100.0%
- Avg finish position: 1.27
- Median finish position: 1.00
- Most common finish position: 1
- Finish position CV (coefficient of variation): 0.694

Pit stops & strategy
- Avg pit stops per race: 2.18
- Avg pit stops time: 22.97s
- Problematic pit stops: 6

Not started/finished/classified, disqualified:
- DNF: 0 (0.0%)
- DNS: 0 (0.0%)
- DSQ: 0 (0.0%)
- NC: 0 (0.0%)

Race progress
- Avg positions gained per race: 4.67
- Races net gain: 40.9%
- Races net loss: 0.0%
- Races no change: 59.1%
- Longest podium streak: 14
  * (2023, 'bahrain') ... (2023, 'italy')
- Longest win streak: 10
  * (2023, 'miami') ... (2023, 'italy')
- Longest points streak: 22
  * (2023, 'bahrain') ... (2023, 'abu-dhabi')
```

Other:
```sh
# Get 2023 max verstappen race results table:
python3 vet.py driver max-verstappen 2023 --races
```
```sh
# Get best lap time at suzuka circuit
python3 vet.py circuit suzuka --best-lap
```
```sh
# Show driver with most wins, most podiums at silverstone circuit
python3 vet.py circuit silverstone -mw -mp
```
```sh
# Show 2026 constructor standings
python3 vet.py season 2026 --constructor
```
```sh
# Show 2026 miami sprint qualifying results
python3 vet.py sprint miami 2026 -q
```
```sh
# Show 2026 gp calendar
python3 vet.py calendar 2026
```
```sh
# Search database for driver with "max"
python3 vet.py db --search -d max
```
```sh
# Execute some sql script for db
python3 vet.py db --sql my_hacky.sql
```

## Installation

Clone this repo somewhere (**do not delete after installation**)

```sh
git clone https://github.com/cebem1nt/vettel.git
```

```sh
cd vettel
./init # Set up the db
```

Update [f1db](https://github.com/f1db/f1db) once in a while with:

```
python vet.py db --update
```

## Misc

```
usage: vet [-h] [--double-headers] [--no-delimiters] [--adjustment {left,center,right}]
           {circuit,driver,race,sprint,season,calendar,db} ...

Diferrent charts, statistics, records, all time bests of Formula One

positional arguments:
  {circuit,driver,race,sprint,season,calendar,db}
                        Available commands
    circuit             Get different records for a circuit
    driver              Different driver's statistics, data over the season or all time
    race                Race results
    sprint              Sprint results
    season              Fancy wikipedia like season table for driver/constructor championship
    calendar            Dates/calendar for a given season
    db                  Different database related commands

options:
  -h, --help            show this help message and exit
  --double-headers      Print table headers twice (at the top and bottom)
  --no-delimiters       Do not print any separators for tables
  --adjustment {left,center,right}
                        Table text alignment
```
