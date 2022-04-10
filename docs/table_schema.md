Top level

| variable         | options                                                                   |
|:-----------------|:--------------------------------------------------------------------------|
| stats_by_quarter | offense, defense                                                          |
| quarter          | 1, 2, 3, 4                                                                |
| down             | 1, 2, 3, 4                                                                |
| distance         | one, short, medium, long, very_long                                       |
| formation        | shotgun, under_center                                                     |
| tempo            | huddle, no_huddle                                                         |
| play_type        | pass, run                                                                 |
| pass_type        | short_left, short_middle, short_right, deep_left, deep_middle, deep_right |
| run_type         | left_tackle, left_guard, center, right_guard, right_tackle                |

| distance  | yardage |
|:----------|:--------|
| one       | <= 1    |
| short     | 2 - 4   |
| medium    | 5 - 7   |
| long      | 8 - 15  |
| very_long | >= 16   |

| pass stat             | description                                                                |
|:----------------------|:---------------------------------------------------------------------------|
| total_yards           | total amount of yardage                                                    |
| avg_yards             | total yards divided by attempts                                            |
| attempts              | total number of pass attempts                                              |
| completions           | number of successful pass attempts                                         |
| completion_pct        | number of completions divided by number of attempts                        |
| total_touchdowns      | total number of touchdowns                                                 |
| avg_touchdowns        | number of touchdowns divided by number of attempts                         |
| avg_field_position    | average field position where 0 is own goal line, 100 is opponent goal line |
| total_explosive_plays | total number of plays over 20 yards                                        | 
| avg_explosive_plays   | number of explosive plays divided by attempts                              |
| total_interceptions   | total number of interceptions                                              |
| avg_interceptions     | number of interceptions divided by number of attempts                      |
| total_sacks           | total number of sacks                                                      |
| avg_sacks             | number of sacks divided by number of attempts                              |
| total_fumbles         | total number of fumbles                                                    |
| avg_fumbles           | number of fumbles divided by number of attempts                            |

| rush stat             | description                                                                |
|:----------------------|:---------------------------------------------------------------------------|
| total_yards           | total amount of yardage                                                    |
| avg_yards             | total yards divided by attempts                                            |
| attempts              | total number of attempts                                                   |
| total_touchdowns      | total number of touchdowns                                                 |
| avg_touchdowns        | number of touchdowns divided by attempts                                   |
| avg_field_position    | average field position where 0 is own goal line, 100 is opponent goal line |
| total_explosive_plays | number of plays over 20 yards                                              |
| avg_explosive_plays   | number of explosive plays divided by attempts                              |
| total_fumbles         | total number of fumbles                                                    |
| avg_fumbles           | number of fumbles divided by attempts                                      |

```json
{
  "team_id": "TEAM",
  "stats_by_quarter": {
    "offense": {
      "quarter": {
        "1": {
          "down": {
            "1": {
              "distance": {
                "short": {
                  "formation": {
                    "shotgun": {
                      "no_huddle": {
                        "pass": {
                          "short_right": {
                            "total_yards": 456,
                            "avg_yards": 4.3,
                            "attempts": 45,
                            "completions": 31,
                            "completion_pct": 0.71,
                            "total_touchdowns": 4,
                            "avg_touchdowns": 0.2,
                            "avg_field_pos": 37,
                            "total_explosive_plays": 5,
                            "avg_explosive_plays": 0.29,
                            "total_interceptions": 6,
                            "avg_interceptions": 0.14,
                            "total_sacks": 7,
                            "avg_sacks": 0.09,
                            "total_fumbles": 3,
                            "avg_fumbles": 0.09
                          }
                        },
                        "rush": {
                          "left_tackle": {
                            "total_yards": 678,
                            "avg_yards": 34.1,
                            "attempts": 329,
                            "total_touchdowns": 7,
                            "avg_touchdowns": 0.4,
                            "avg_field_pos": 52,
                            "total_explosive_plays": 4,
                            "avg_explosive_plays": 0.87,
                            "total_fumbles": 3,
                            "avg_fumbles": 0.31
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```



DB entry:
```json
{
  "team_id": "DET",
  "aggregate_stats_by_quarter": [
    {
      // Quarter objcect
    }
  ]

}
```

Quarter:
```json
{
  "quarter": 1,
  "aggregate_stats_by_down": [
    {
      // Down object
    }
  ]
}
```

Down:
```json
{
  "down": 1,
  "aggregate_stats_by_distance": [
    {
      // Distance object
    }
  ]
}
```

Distance:
```json
{
  "distance": "short",
  
}
```

