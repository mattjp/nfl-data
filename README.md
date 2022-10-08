# NFL Data API

## Running `games` API

0. Move to the source directory

```
cd src/NflData/
```

2. Build the Lambda

```
% cdk synth
```

2. Test locally

```
% sam local invoke -e tests/games_event.json -t ./cdk.out/NflDataStack.template.json GamesHandler
```

3. Invoke Lambda

```
curl -X POST -d @tests/event.json -m 900 https://h2pon94e3a.execute-api.us-east-2.amazonaws.com/prod/games
```

## Initial Functionality

* For each team (offense/defense), aggregate stats by down.
* ESPN play-by-play API will provide data.
  * Example play-by-play API: https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401220181/competitions/401220181/plays?limit=400
* ESPN team season API will be used to get game IDs.
  * Example season API: https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2021/teams/2/events

## Systems

* Handler for game stats calculator
  * Call ESPN API, update `game_ids_[YEAR]` table with new games
  * For all `teamIds`, given a `week` and `year`
  * Lambda with API gateway

* Handler for game aggregator
  * For a set of `gameIds`, call the aggregator lambda in parallel
  * Lambda with API gateway

* For a given `gameId` calculate aggregate offensive and defensive stats
  * Call ESPN API, add full json to S3 
  * Add all stats to the `team_off_stats_by_down_[YEAR]` or `team_def_stats_by_down_[YEAR]` table
  * Mark the `gameId` as completed in the `game_ids_[YEAR]` table
  * Called one or many times by the handler
    * Lambda, called by handler in parallel

## Desired functionality

* Group stats by opponent
* Stats by player


## Other notes

* For some reason, the `requests` library only works with Python 3.7, not 3.9



