"""
S3.5 - test season between S3 and S4
"""
from models.season_config import SeasonConfig
from projects.apps.Arbuz import Arbuz
from projects.apps.Fanzee import Fanzee
from projects.apps.QuackQuack import QuackQuack
from projects.tokens.ARBUZ import ARBUZ
from projects.tokens.KINGY import KINGY
from seasons.app_models import AppLeaderboardModelV2
from seasons.tokens_models import TokenLeaderboardModelV4

S3_5_apps = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="S3.5",
    start_time=1716980400, # 2024-05-29 11:00:00 +0000
    end_time=1718190000, # Wed Jun 12 2024 11:00:00 GMT+0000
    projects=[
        QuackQuack,
        Arbuz,
        Fanzee
    ],
    score_model=AppLeaderboardModelV2()
)

S3_5_tokens = SeasonConfig(
    leaderboard=SeasonConfig.TOKENS,
    name="S3.5",
    start_time=1716980400, # 2024-05-29 11:00:00 +0000
    end_time=1718190000, # Wed Jun 12 2024 11:00:00 GMT+0000
    projects=[
        ARBUZ, KINGY
    ],
    score_model=TokenLeaderboardModelV4()
)