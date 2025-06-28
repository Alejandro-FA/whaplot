"""Package to create bar chart race animations from WhatsApp chats."""

import sys

from whaplot.application import Application
from whaplot.argument_parser import ArgumentParser


def main() -> None:
    """Main function to run the whaplot application."""
    config = ArgumentParser.parse_args(sys.argv[1:])
    app = Application()
    app.create_plots(config)
