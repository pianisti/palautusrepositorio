from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

def main():
    season = Prompt.ask("Season [red][2018-19/2019-10/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26][/red]")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
    while True:
        nationality = Prompt.ask("Nationality [red][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/red]")
        players = stats.top_scorers_by_nationality(f"{nationality}")

        table = Table(title=f"Season [red]{season}[/red] players from [red]{nationality}[/red]")
        table.add_column("player", style="blue", no_wrap=True)
        table.add_column("teams", style="red")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")    
        
        amount = 0
        for player in players:
            if amount < 12:
                amount += 1
                table.add_row(f"{player.name}", f"{player.team}", f"{player.goals}", f"{player.assists}", f"{player.goals + player.assists}")

        console = Console()
        console.print(table)

if __name__ == "__main__":
    main()
