# Security Metrics

Vulcan can be used to query dynamically calculated security metrics for any of its teams. These metrics include the percentage of assets with vulnerabilities of a certain severity, the median exposure of currently existing vulnerabilities of each severity and the mean time to remediate for those vulnerabilities that have already been resolved. These metrics can be used to understand the security status of the company and to set goals that teams can track themselves.

## Example 1

Vulcan can be used to retrieve metrics for a team using the stats endpoint in the [Vulcan API](/vulcan-api/).

```bash
# Retrieve currently open findings.
curl -H "Authorization: Bearer $VULCAN_API_TOKEN" \
  "www.vulcan.example.com/api/v1/teams/$VULCAN_TEAM_ID/stats/open"

{
  "open_issues": {
    "critical": 2,
    "high": 4,
    "medium": 9,
    "low": 11,
    "informational": 21
  }
}
```

```bash
# Retrieve current exposure (in hours) of open findings.
curl -H "Authorization: Bearer $VULCAN_API_TOKEN" \
  "www.vulcan.example.com/api/v1/teams/$VULCAN_TEAM_ID/stats/exposure/current"

{
  "current_exposure": {
    "mean": 41.209448947762005,
    "percentile_10": 36.78803730882772,
    "percentile_25": 50.75172645112574,
    "percentile_50": 54.29089680729741,
    "percentile_75": 72.78236287555608
    "percentile_90": 98.5214296805186,
  }
}
```
