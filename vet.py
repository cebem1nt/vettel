#!/usr/bin/env python3
import os, argparse, sys

from vettel.tables import Table
from vettel.handlers import (
    DB,
    Race,
    Sprint,
    Driver, 
    Season,
    Circuit,
    Calendar,
    Standings,
)

VERSION = "1.2.0"

def match_args(args: argparse.Namespace):
    table = Table(
        args.adjustment,
        args.double_headers,
        args.no_delimiters
    )

    argc = len(sys.argv)

    match args.command:
        case "circuit":
            circuit = Circuit(args.id, args.rows, args.reverse, table)

            if args.info or argc == 3:
                circuit.info()

            if args.best_lap:
                circuit.record("best-lap")

            if args.best_qualifying:
                circuit.record("best-qualifying")

            if args.most_wins:
                circuit.record("most-wins")

            if args.most_podiums:
                circuit.record("most-podiums")
        
        case "standings":
            standings = Standings(args.year, f1db, table)
            standings.standings(args.constructor, args.flags)

        case "season":
            season = Season(args.year, args.flags, f1db, table)
            season.championship(args.constructor)

        case "driver":
            driver = Driver(args.id, args.year, table, args.all_time)

            if args.overview:   driver.overview()
            if args.races:      driver.races()
            if args.pit_stops:  driver.pits()
            if args.qualifying: driver.qualifying()
            if args.sprints:    driver.sprints()

        case "calendar":
            calendar = Calendar(args.year, f1db)
            calendar.calendar(args.full, args.utc)

        case "race":
            race = Race(args.id, args.year, table, args.full)

            if args.results:
                race.results(args.qualifying, args.utc)
            elif args.qualifying:
                race.qualifying()
            else:
                race.race()

        case "sprint":
            sprint = Sprint(args.id, args.year, table, args.full)

            if args.qualifying:
                sprint.qualifying()
            else:
                sprint.sprint()

        case "db":
            db = DB(f1db, table)

            if args.sql:
                db.execute_sql(args.sql)

            if args.update:
                db.update()

            if args.search:
                queries = []

                if args.driver:
                    queries.append((args.driver, "driver"))

                if args.constructor:
                    queries.append((args.constructor, "constructor"))

                if args.circuit:
                    queries.append((args.circuit, "circuit"))

                if args.grand_prix:
                    queries.append((args.grand_prix, "grand_prix"))
            
                for query, table in queries:
                    db.search(query, table, args.column, args.as_pattern)
            
        case _:
            print(f"Unknown command: {args.command}")

def main():
    p = argparse.ArgumentParser(description="Different info, statistics, records, all time bests of Formula One")

    p.add_argument("--double-headers", action="store_true",                                 help="Print table headers twice (at the top and bottom)")
    p.add_argument("--no-delimiters",  action="store_true",                                 help="Do not print any separators for tables")
    p.add_argument("--adjustment",     default="left", choices=("left", "center", "right"), help="Table text alignment")
    p.add_argument("--utc",            action="store_true",                                 help="Show time in UTC instead of local timezone")
    p.add_argument("--version",        action="store_true",                                 help="Show vettel version and exit")

    subps = p.add_subparsers(dest="command", help="Available commands")

    circuit_p = subps.add_parser("circuit", help="Get different records for a circuit")
    circuit_p.add_argument      ("id",  metavar="ID",        type=str,            help="Circuit id")
    circuit_p.add_argument      ("-i",  "--info",            action="store_true", help="Show circuit info")
    circuit_p.add_argument      ("-bl", "--best-lap",        action="store_true", help="All time best laps during the race")
    circuit_p.add_argument      ("-bq", "--best-qualifying", action="store_true", help="All time best qualifying records")
    circuit_p.add_argument      ("-mw", "--most-wins",       action="store_true", help="List of drivers with most wins")
    circuit_p.add_argument      ("-mp", "--most-podiums",    action="store_true", help="List of drivers with most podiums")
    circuit_p.add_argument      ("-R",  "--reverse",         action="store_true", help="Reverse results")
    circuit_p.add_argument      ("-r",  "--rows", type=int,  default=15,          help="Amount of rows to fetch, -1 means all. Defaults to 15")

    driver_p = subps.add_parser("driver", help="Different driver's statistics, data over the season or all time")
    driver_p.add_argument      ("id",  metavar="ID",        type=str,            help="Driver id")
    driver_p.add_argument      ("year",metavar="YEAR",      type=int, nargs="?", help="Optional season year. Current year if omitted")
    driver_p.add_argument      ("-o",  "--overview",        action="store_true", help="An overview, driver statistics for a season")
    driver_p.add_argument      ("-r",  "--races",           action="store_true", help="Driver race results for given season")
    driver_p.add_argument      ("-s",  "--sprints",         action="store_true", help="Driver season sprints results")
    driver_p.add_argument      ("-q",  "--qualifying",      action="store_true", help="Driver qualifying results for the season")
    driver_p.add_argument      ("-p",  "--pit-stops",       action="store_true", help="Table of pit stops for each race")
    driver_p.add_argument      ("-a",  "--all-time",        action="store_true", help="Show all time results instead")
    
    race_p = subps.add_parser("race", help="Show exact/all races results for given year")
    race_p.add_argument      ("id",   metavar="ID",      type=str, nargs="?", help="Grand prix or circuit id, e.g: monaco/china, shanghai")
    race_p.add_argument      ("year", metavar="YEAR",    type=int, nargs="?", help="Year of the race. Current year if omitted")
    race_p.add_argument      ("-f", "--full",            action="store_true", help="Show full information table")
    race_p.add_argument      ("-q", "--qualifying",      action="store_true", help="Show the qualifying result instead")
    race_p.add_argument      ("-r", "--results",         action="store_true", help="Show races results for the given year")


    sprint_p = subps.add_parser("sprint", help="Sprint results")
    sprint_p.add_argument      ("id",   metavar="ID",   type=str,             help="Grand prix or circuit id, e.g: monaco/china, shanghai")
    sprint_p.add_argument      ("year", metavar="YEAR", type=int, nargs="?",  help="Year of the sprint. Current year if omitted")
    sprint_p.add_argument      ("-f", "--full",         action="store_true",  help="Show full information table")
    sprint_p.add_argument      ("-q", "--qualifying",   action="store_true",  help="Show the qualifying result instead")

    standings_p = subps.add_parser("standings", help="Season driver standings")
    standings_p.add_argument      ("year", metavar="YEAR", type=int, nargs="?",  help="Season year. Current year if omitted")
    standings_p.add_argument      ("-c", "--constructor",  action="store_true",  help="Show constructor standings instead")
    standings_p.add_argument      ("--flags",              action="store_true",  help="Add emoji flags to driver's nationality")

    season_p = subps.add_parser("season", help="Fancy wikipedia like season table for driver/constructor championship")
    season_p.add_argument      ("year", metavar="YEAR", type=int, nargs="?", help="Season year. Current year if omitted")
    season_p.add_argument      ("-c", "--constructor",  action="store_true", help="Show constructor table instead")
    season_p.add_argument      ("--flags",              action="store_true", help="Add emoji flags to grand prix columns")

    calendar_p = subps.add_parser("calendar", help="Dates/calendar for a given season")
    calendar_p.add_argument      ("year", metavar="YEAR", type=int, nargs="?", help="Season year. Current year if omitted")
    calendar_p.add_argument      ("-f", "--full", action="store_true",         help="Show full calendar, do not stop at current stage")

    # TODO perhaps split search into a sub-parser?
    db_p = subps.add_parser("db", help="Different database related commands")
    db_p.add_argument      ("-s", "--sql",              type=str,             help="Run arbitrary sql script on the f1db")
    db_p.add_argument      ("-u", "--update", "--init", action="store_true",  help="Update/init f1db")
    db_p.add_argument      ("-S", "--search",           action="store_true",  help="Enable search mode. Provide additional -d/t/c/g with part to search for")
    db_p.add_argument      ("-d", "--driver",      metavar="PART", type=str,  help="If searching, search for driver")
    db_p.add_argument      ("-t", "--constructor", metavar="PART", type=str,  help="If searching, search for a constructor (team)")
    db_p.add_argument      ("-c", "--circuit",     metavar="PART", type=str,  help="If searching, search for circuit")
    db_p.add_argument      ("-g", "--grand-prix",  metavar="PART", type=str,  help="If searching, search for grand prix")
    db_p.add_argument      ("--as-pattern",              action="store_true", help="If searching, treat part as entire pattern for sql LIKE")
    db_p.add_argument      ("--column",  type=str,       default="name",      help="If searching, use given colum to match part, defaults to \"name\"")

    args = p.parse_args()

    # Some extra validation for a bit weird race parser
    if args.command == "race":
        if args.results and args.id:
            race_p.error("--results is not available with ID")

        if not (args.results or args.id):
            race_p.error("--results OR ID is required")

    if args.version:
        print('v'+VERSION)
    elif any(vars(args).values()) and args.command:
        match_args(args)
    else:
        p.print_help()

if __name__ == "__main__":
    main()