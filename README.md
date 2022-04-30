# NFL Data API

## Initial Functionality

* For each team (offense/defense), aggregate stats by down.
* ESPN play-by-play API will provide data.
  * Example play-by-play API: https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events/401220181/competitions/401220181/plays?limit=400
* ESPN team season API will be used to get game IDs.
  * Example season API: https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2021/teams/2/events

## Systems

* Handler for game stats calculator
  * Call ESPN API, update `game_ids_[YEAR]` table with new games 
  * For all `teamIds`, given a `week` and `year`, call the game stats aggregator

* For a given `gameId` calculate aggregate offensive and defensive stats
  * Call ESPN API, add full json to S3 
  * Add all stats to the `team_off_stats_by_down_[YEAR]` or `team_def_stats_by_down_[YEAR]` table
  * Mark the `gameId` as completed in the `game_ids_[YEAR]` table
  * Called one or many times by the handler

## Desired functionality

* Group stats by opponent
* Stats by player




