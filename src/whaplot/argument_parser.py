import argparse
import importlib.metadata
import sys
from collections.abc import Sequence
from pathlib import Path

from whaplot.config.application_config import ApplicationConfig
from whaplot.config.race_config import RaceConfig, RaceMetric


class ArgumentParser:
    __EXTENSIONS = (".txt", ".zip")

    @staticmethod
    def parse_args(args: Sequence[str] = sys.argv[1:]) -> ApplicationConfig:
        parser = ArgumentParser.__create_parser()
        parsed_args = parser.parse_args(args)
        match parsed_args.subcommand:
            case "race":
                return RaceConfig(
                    chat_files=parsed_args.chat_files, metric=ArgumentParser.__get_race_metric(parsed_args)
                )
            case _:
                raise ValueError(f"Invalid subcommand: {parsed_args.subcommand}")

    @staticmethod
    def __create_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog=None,
            description=(
                "Data visualization tool for WhatsApp chat exports. "
                "Use subcommands to specify the type of visualization."
            ),
            epilog=None,
        )
        parser.add_argument(
            "-v", "--version", action="version", version=f"%(prog)s {importlib.metadata.version(parser.prog)}"
        )
        ArgumentParser.__add_subparsers(parser)
        return parser

    @staticmethod
    def __add_subparsers(parser: argparse.ArgumentParser) -> None:
        subparsers = parser.add_subparsers(
            dest="subcommand", required=True, title="generate a data visualization from a chat"
        )
        race_parser = subparsers.add_parser("race", help="create a bar chart race animation")
        ArgumentParser.__add_race_arguments(race_parser)

    @staticmethod
    def __add_race_arguments(race_parser: argparse.ArgumentParser) -> None:
        race_parser.add_argument(
            "chat_files",
            type=ArgumentParser.__chat_file,
            nargs="+",
            help="paths to the WhatsApp chat export .txt or .zip files",
        )
        # Mutually exclusive group for race-specific options.
        group = race_parser.add_argument_group(title="choose the metric to display in the bar chart race animation")
        exclusive_group = group.add_mutually_exclusive_group(required=False)
        exclusive_group.add_argument(
            "--messages",
            action="store_true",
            help="plot the number of messages sent by each person over time",
            default=True,
        )
        exclusive_group.add_argument(
            "--words",
            action="store_true",
            help="plot the number of words sent by each person over time",
        )
        exclusive_group.add_argument(
            "--characters",
            action="store_true",
            help="plot the number of characters sent by each person over time",
        )

    @staticmethod
    def __get_race_metric(parsed_args: argparse.Namespace) -> RaceMetric:
        if parsed_args.messages:
            return RaceMetric.MESSAGE_COUNT
        if parsed_args.characters:
            return RaceMetric.CHARACTER_COUNT
        if parsed_args.words:
            return RaceMetric.WORD_COUNT
        raise ValueError("No race metric specified.")

    @staticmethod
    def __chat_file(string: str) -> Path:
        path = Path(string)
        if not path.exists():
            raise argparse.ArgumentTypeError(f"File '{path}' not found.")
        if not path.is_file() or (path.suffix not in ArgumentParser.__EXTENSIONS):
            raise argparse.ArgumentTypeError(f"'{path}' is not a valid chat file.")
        return path
