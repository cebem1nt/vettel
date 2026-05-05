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
vet season 2023 --flags >> README.md
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

<table><tr>
<td>

```sh
vet circuit silverstone --most-wins -r=30
```
  
```
|    | driver                | total |
|----|-----------------------|-------|
| 1  | Lewis Hamilton        | 9     |
| 2  | Alain Prost           | 5     |
| 3  | Jim Clark             | 3     |
| 4  | Michael Schumacher    | 3     |
| 5  | Nigel Mansell         | 3     |
| 6  | Alberto Ascari        | 2     |
| 7  | David Coulthard       | 2     |
| 8  | Fernando Alonso       | 2     |
| 9  | Jackie Stewart        | 2     |
| 10 | Jacques Villeneuve    | 2     |
| 11 | José Froilán González | 2     |
| 12 | Mark Webber           | 2     |
| 13 | Max Verstappen        | 2     |
| 14 | Sebastian Vettel      | 2     |
| 15 | Ayrton Senna          | 1     |
| 16 | Carlos Sainz Jr.      | 1     |
| 17 | Clay Regazzoni        | 1     |
| 18 | Damon Hill            | 1     |
| 19 | Emerson Fittipaldi    | 1     |
| 20 | Jack Brabham          | 1     |
| 21 | James Hunt            | 1     |
| 22 | John Watson           | 1     |
| 23 | Johnny Herbert        | 1     |
| 24 | Juan Manuel Fangio    | 1     |
| 25 | Juan Pablo Montoya    | 1     |
| 26 | Kimi Räikkönen        | 1     |
| 27 | Lando Norris          | 1     |
| 28 | Mika Häkkinen         | 1     |
| 29 | Nico Rosberg          | 1     |
| 30 | Nino Farina           | 1     |
```

</td>
<td>
  
```sh
vet calendar 2026
```
```
        Round 1 - Australia
 -----------------------------------
 - Qualifying:        Mar 07 at 05:00
 - Race:              Mar 08 at 04:00

          Round 2 - China
 -----------------------------------
 - Sprint qualifying: Mar 13 at 07:30
 - Sprint:            Mar 14 at 03:00
 - Qualifying:        Mar 14 at 07:00
 - Race:              Mar 15 at 07:00

         Round 3 - Japan
 -----------------------------------
 - Qualifying:        Mar 28 at 06:00
 - Race:              Mar 29 at 05:00

          Round 4 - Miami
 -----------------------------------
 - Sprint qualifying: May 01 at 20:30
 - Sprint:            May 02 at 16:00
 - Qualifying:        May 02 at 20:00
 - Race:              May 03 at 17:00

      -*- Round 5 - Canada -*-
 -----------------------------------
 - Sprint qualifying: May 22 at 20:30
 - Sprint:            May 23 at 16:00
 - Qualifying:        May 23 at 20:00
 - Race:              May 24 at 20:00

                ....
```

</td>

<td>

```sh
vet race japan 2026
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

</td>
<td>

```sh
vet sprint china 2026 --full
```

```
| driver            | constructor  | start | finish  | gap     | laps | penalty | pts |
|-------------------|--------------|-------|---------|---------|------|---------|-----|
| George Russell    | Mercedes     | 1     | 1       |         | 19   |         | 8   |
| Charles Leclerc   | Ferrari      | 6     | 2 (+4)  | +0.674  | 19   |         | 7   |
| Lewis Hamilton    | Ferrari      | 4     | 3 (+1)  | +2.554  | 19   |         | 6   |
| Lando Norris      | McLaren      | 3     | 4 (-1)  | +4.433  | 19   |         | 5   |
| Kimi Antonelli    | Mercedes     | 2     | 5 (-3)  | +5.688  | 19   |         | 4   |
| Oscar Piastri     | McLaren      | 5     | 6 (-1)  | +6.809  | 19   |         | 3   |
| Liam Lawson       | Racing Bulls | 13    | 7 (+6)  | +10.900 | 19   |         | 2   |
| Oliver Bearman    | Haas         | 9     | 8 (+1)  | +11.271 | 19   |         | 1   |
| Max Verstappen    | Red Bull     | 8     | 9 (-1)  | +11.619 | 19   |         |     |
| Esteban Ocon      | Haas         | 12    | 10 (+2) | +13.887 | 19   |         |     |
| Pierre Gasly      | Alpine       | 7     | 11 (-4) | +14.780 | 19   |         |     |
| Carlos Sainz Jr.  | Williams     | 17    | 12 (+5) | +15.753 | 19   |         |     |
| Gabriel Bortoleto | Audi         | 14    | 13 (+1) | +15.858 | 19   |         |     |
| Franco Colapinto  | Alpine       | 16    | 14 (+2) | +16.393 | 19   |         |     |
| Isack Hadjar      | Red Bull     | 10    | 15 (-5) | +16.430 | 19   |         |     |
| Alexander Albon   | Williams     | 22    | 16 (+6) | +20.014 | 19   |         |     |
| Fernando Alonso   | Aston Martin | 18    | 17 (+1) | +21.599 | 19   |         |     |
| Lance Stroll      | Aston Martin | 19    | 18 (+1) | +21.971 | 19   |         |     |
| Sergio Pérez      | Cadillac     | 21    | 19 (+2) | +28.241 | 19   | 5.000   |     |
| Nico Hülkenberg   | Audi         | 11    | DNF     |         | 12   |         |     |
| Valtteri Bottas   | Cadillac     | 20    | DNF     |         | 12   |         |     |
| Arvid Lindblad    | Racing Bulls | 15    | DNF     |         | 11   |         |     |

Pole position: George Russell

--------------------------------------------------
Nico Hülkenberg - Reason retired: Mechanical
Valtteri Bottas - Reason retired: Withdrew
Arvid Lindblad - Reason retired: Collision damage
```

</td>
</tr></table>

Other:
```sh
# Get 2023 max verstappen comprehensive overview/statistics:
vet driver max-verstappen 2023
```
```sh
# Get 2023 max verstappen race results table:
vet driver max-verstappen 2023 --races
```
```sh
# Get best lap time at suzuka circuit
vet circuit suzuka --best-lap
```
```sh
# Show driver with most wins, most podiums at silverstone circuit
vet circuit silverstone -mw -mp
```
```sh
# Show 2026 constructor standings
vet season 2026 --constructor
```
```sh
# Show 2026 miami sprint qualifying results
vet sprint miami 2026 -q
```
```sh
# Show 2026 gp calendar
vet calendar 2026
```
```sh
# Search database for driver with "max"
vet db --search -d max
```
```sh
# Execute some sql script for db
vet db --sql my_hacky.sql
```

## Installation

### AUR:
```sh
yay -S vettel # Or with any other aur helper like paru
```

<details>
  <summary><h3>From source:</h3></summary>

  ```sh
  git clone https://github.com/cebem1nt/vettel.git
  cd vettel
  ```

  ```sh
  # Install systemwide with python
  sudo python setup.py install --optimize=1
  ```

</details>

To get new info, update [f1db](https://github.com/f1db/f1db) once in a while with:

```sh
vet db --update
```

## Misc

```
usage: vet [-h] [--double-headers] [--no-delimiters] [--adjustment {left,center,right}] {circuit,driver,race,sprint,season,calendar,db} ...

Different info, statistics, records, all time bests of Formula One

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
