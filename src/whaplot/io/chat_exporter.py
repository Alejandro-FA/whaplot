from pathlib import Path

import pandas as pd

from whaplot.viewmodels.chat import Chat


class ChatExporter:
    def to_excel(self, chat: Chat, output_file: Path) -> None:
        df = self.to_dataframe(chat)
        df.to_excel(output_file, index=True)

    def to_csv(self, chat: Chat, output_file: Path) -> None:
        df = self.to_dataframe(chat)
        df.to_csv(output_file, index=True)

    def to_dataframe(self, chat: Chat) -> pd.DataFrame:
        # TODO: The format that sjvisualizer expects is peculiar, so perhaps we should consider moving this method
        # to a different place. Furthermore, in the future we might want to generate different types of dataframes
        # for different purposes (e.g., one for messages sent, one for characters, etc.).
        raise NotImplementedError("toPandas method is not implemented")
