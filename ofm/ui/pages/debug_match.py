#      Openfoot Manager - A free and open source soccer management simulation
#      Copyright (C) 2020-2023  Pedrenrique G. Guimarães
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview


class DebugMatchPage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.notebook = ttk.Notebook(self)

        self.player_details_tab = ttk.Frame(self.notebook)
        self.player_reserves_tab = ttk.Frame(self.notebook)
        self.player_stats_tab = ttk.Frame(self.notebook)

        self.title_label = ttk.Label(self, text="Debug Match", font="Arial 24 bold")
        self.title_label.grid(
            row=0, column=0, padx=10, pady=10, columnspan=3, sticky=NS
        )

        self.home_team_table = None
        self.home_team_reserves_table = None
        self.away_team_table = None
        self.away_team_reserves_table = None
        self.home_team_name = None
        self.away_team_name = None
        self.home_team_score = None
        self.away_team_score = None
        self.home_team_reserves_name = None
        self.home_team_reserves_score = None
        self.away_team_reserves_name = None
        self.away_team_reserves_score = None
        self.home_team_stats_name = None
        self.away_team_stats_name = None

        self.columns = [
            {"text": "Name", "stretch": False},
            {"text": "Position", "stretch": False},
            {"text": "Stamina", "stretch": False},
            {"text": "Overall", "stretch": False},
        ]

        home_rows = [
            ("Gomez", "FW", "100", "89"),
            ("Allejo", "FW", "100", "95"),
            ("Beranco", "MF", "100", "85"),
            ("Pardilla", "MF", "100", "83"),
            ("Santos", "MF", "100", "80"),
            ("Ferreira", "MF", "100", "87"),
            ("Roca", "DF", "100", "86"),
            ("Vincento", "DF", "100", "84"),
            ("Cicero", "DF", "100", "90"),
            ("Marengez", "DF", "100", "88"),
            ("Da Silva", "GK", "100", "92"),
        ]

        away_rows = [
            ("Estrade", "FW", "100", "84"),
            ("Capitale", "FW", "100", "83"),
            ("Hajo", "MF", "100", "90"),
            ("Redonda", "MF", "100", "87"),
            ("Vasquez", "MF", "100", "80"),
            ("Santos", "MF", "100", "81"),
            ("Basile", "DF", "100", "83"),
            ("Morelli", "DF", "100", "82"),
            ("Costa", "DF", "100", "91"),
            ("Alerto", "DF", "100", "84"),
            ("Pablo", "GK", "100", "87"),
        ]

        self.update_tables(home_rows, away_rows, home_rows, away_rows)

        self.scores_details = ttk.Frame(self.player_details_tab)
        self.scores_reserves = ttk.Frame(self.player_reserves_tab)

        self.update_team_names("Brazil", "Argentina", "0", "0")

        self.game_progress_bar = ttk.Progressbar(self, value=50, bootstyle="striped")
        self.game_progress_bar.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10, sticky=EW
        )

        self.game_minutes_elapsed = ttk.Label(self, text="0'")
        self.game_minutes_elapsed.grid(
            row=3, column=0, columnspan=2, padx=10, pady=10, sticky=NS
        )

        # Team Stats
        self.home_team_stats = [
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
        ]
        for row, stat in enumerate(self.home_team_stats):
            stat.grid(row=row + 1, column=0, padx=5, pady=5, sticky=NW)

        self.stats_descriptions = [
            ttk.Label(self.player_stats_tab, text="Shots"),
            ttk.Label(self.player_stats_tab, text="Shots on target"),
            ttk.Label(self.player_stats_tab, text="Possession"),
            ttk.Label(self.player_stats_tab, text="Passes"),
            ttk.Label(self.player_stats_tab, text="Pass accuracy"),
            ttk.Label(self.player_stats_tab, text="Fouls"),
            ttk.Label(self.player_stats_tab, text="Yellow cards"),
            ttk.Label(self.player_stats_tab, text="Red cards"),
            ttk.Label(self.player_stats_tab, text="Offsides"),
            ttk.Label(self.player_stats_tab, text="Corners"),
        ]
        for row, stat in enumerate(self.stats_descriptions):
            stat.grid(row=row + 1, column=1, padx=5, pady=5, sticky=NS)

        self.away_team_stats = [
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
            ttk.Label(self.player_stats_tab, text="0"),
        ]
        for row, stat in enumerate(self.away_team_stats):
            stat.grid(row=row + 1, column=2, padx=5, pady=5, sticky=NE)

        self.button_frame = ttk.Frame(self)

        self.play_game_btn = ttk.Button(self.button_frame, text="Play")
        self.play_game_btn.pack(side="left", padx=10)

        self.new_game_btn = ttk.Button(self.button_frame, text="New Game")
        self.new_game_btn.pack(side="left", padx=10)

        self.cancel_btn = ttk.Button(self.button_frame, text="Cancel")
        self.cancel_btn.pack(side="left", padx=10)

        self.button_frame.grid(
            row=4, column=0, columnspan=2, padx=10, pady=10, sticky=NS
        )

        self.scores_details.grid(row=0, column=0, columnspan=2)
        self.scores_reserves.grid(row=0, column=0, columnspan=2)

        self.player_details_tab.place(anchor=CENTER, relx=0.5, rely=0.5)
        self.player_reserves_tab.place(anchor=CENTER, relx=0.5, rely=0.5)
        self.player_stats_tab.place(anchor=CENTER, relx=0.5, rely=0.5)

        self.notebook.add(self.player_details_tab, text="Players", sticky=NS)
        self.notebook.add(self.player_reserves_tab, text="Reserves", sticky=NS)
        self.notebook.add(self.player_stats_tab, text="Stats", sticky=NS)
        self.notebook.grid(row=1, column=0, sticky=NSEW)

    def update_tables(
        self,
        home_team: list[tuple],
        away_team: list[tuple],
        home_reserves: list[tuple],
        away_reserves: list[tuple],
    ):
        if self.home_team_table:
            self.home_team_table.destroy()
        if self.away_team_table:
            self.away_team_table.destroy()
        if self.home_team_reserves_table:
            self.home_team_reserves_table.destroy()
        if self.away_team_reserves_table:
            self.away_team_reserves_table.destroy()

        self.home_team_table = Tableview(
            self.player_details_tab,
            coldata=self.columns,
            rowdata=home_team,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=8,
            height=11,
        )
        self.home_team_table.autofit_columns()
        self.home_team_table.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

        self.away_team_table = Tableview(
            self.player_details_tab,
            coldata=self.columns,
            rowdata=away_team,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=8,
            height=11,
        )
        self.away_team_table.autofit_columns()
        self.away_team_table.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

        self.home_team_reserves_table = Tableview(
            self.player_reserves_tab,
            coldata=self.columns,
            rowdata=home_reserves,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=8,
            height=11,
        )
        self.home_team_reserves_table.autofit_columns()
        self.home_team_reserves_table.grid(row=1, column=0, padx=10, pady=10, sticky=EW)

        self.away_team_reserves_table = Tableview(
            self.player_reserves_tab,
            coldata=self.columns,
            rowdata=away_reserves,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=8,
            height=11,
        )
        self.away_team_reserves_table.autofit_columns()
        self.away_team_reserves_table.grid(row=1, column=1, padx=10, pady=10, sticky=EW)

    def disable_button(self):
        self.play_game_btn.config(state=ttk.DISABLED)

    def enable_button(self):
        self.play_game_btn.config(state=ttk.NORMAL)

    def update_team_names(
        self, home_team: str, away_team: str, home_team_score: str, away_team_score: str
    ):
        if self.home_team_name:
            self.home_team_name.destroy()
        if self.away_team_name:
            self.away_team_name.destroy()
        if self.home_team_score:
            self.home_team_score.destroy()
        if self.away_team_score:
            self.away_team_score.destroy()
        if self.home_team_reserves_name:
            self.home_team_reserves_name.destroy()
        if self.away_team_reserves_name:
            self.away_team_reserves_name.destroy()
        if self.home_team_stats_name:
            self.home_team_stats_name.destroy()
        if self.away_team_stats_name:
            self.away_team_stats_name.destroy()

        self.home_team_name = ttk.Label(
            self.scores_details, text=f"{home_team}", font="Arial 15 bold"
        )
        self.home_team_name.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.home_team_score = ttk.Label(
            self.scores_details, text=f"{home_team_score}", font="Arial 15 bold"
        )
        self.home_team_score.grid(row=0, column=1, padx=15, pady=10, sticky=NS)

        self.away_team_score = ttk.Label(
            self.scores_details, text=f"{away_team_score}", font="Arial 15 bold"
        )
        self.away_team_score.grid(row=0, column=2, padx=15, pady=10, sticky=NS)

        self.away_team_name = ttk.Label(
            self.scores_details, text=f"{away_team}", font="Arial 15 bold"
        )
        self.away_team_name.grid(row=0, column=3, padx=10, pady=10, sticky=E)

        # Reserves tab
        self.home_team_reserves_name = ttk.Label(
            self.scores_reserves, text=f"{home_team}", font="Arial 15 bold"
        )
        self.home_team_reserves_name.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.home_team_reserves_score = ttk.Label(
            self.scores_reserves, text=f"{home_team_score}", font="Arial 15 bold"
        )
        self.home_team_reserves_score.grid(row=0, column=1, padx=10, pady=10, sticky=NS)

        self.away_team_reserves_score = ttk.Label(
            self.scores_reserves, text=f"{away_team_score}", font="Arial 15 bold"
        )
        self.away_team_reserves_score.grid(row=0, column=2, padx=10, pady=10, sticky=NS)

        self.away_team_reserves_name = ttk.Label(
            self.scores_reserves, text=f"{away_team}", font="Arial 15 bold"
        )
        self.away_team_reserves_name.grid(row=0, column=3, padx=10, pady=10, sticky=E)

        # Team Stats tab
        self.home_team_stats_name = ttk.Label(
            self.player_stats_tab, text=f"{home_team}", font="Arial 13 bold"
        )
        self.home_team_stats_name.grid(row=0, pady=5, column=0, sticky=E)

        self.away_team_stats_name = ttk.Label(
            self.player_stats_tab, text=f"{away_team}", font="Arial 13 bold"
        )
        self.away_team_stats_name.grid(row=0, pady=5, column=2, sticky=W)
