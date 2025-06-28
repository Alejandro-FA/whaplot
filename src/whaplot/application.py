from whaplot.config.application_config import ApplicationConfig
from whaplot.config.race_config import RaceConfig
from whaplot.io.chat_reader import ChatReader
from whaplot.plotter.plotter import Plotter


class Application:
    def __init__(self) -> None:
        self.chat_reader: ChatReader = ChatReader()
        self.plotter: Plotter = Plotter()

    def create_plots(self, config: ApplicationConfig) -> None:
        match config:
            case RaceConfig():
                self.__create_bar_chart_race_plots(config)
            case _:
                raise ValueError(f"Unsupported config type: {type(config)}")

    def __create_bar_chart_race_plots(self, config: RaceConfig) -> None:
        for chat_file in config.chat_files:
            print(f"Creating bar chart race animation for {chat_file.name}...")  # noqa: T201
            chat = self.chat_reader.read(chat_file)
            self.plotter.create_bar_chart_race(chat)
