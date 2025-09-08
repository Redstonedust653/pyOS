from textual.app import App, ComposeResult
from textual.widgets import Footer, Header,DirectoryTree,TextArea,LoadingIndicator
from textual import events
from pathlib import Path
from typing import Iterable
from datetime import datetime
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Footer, ProgressBar

class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]

class ExtendedTextArea(TextArea):
    """A subclass of TextArea with parenthesis-closing functionality."""
    def _on_key(self, event: events.Key) -> None: #type:ignore
        if event.character == "(":
            self.insert("()")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()
        if event.character == "{":
            self.insert("{}")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()
        if event.character == "[":
            self.insert("[]")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()
        if event.character == '"':
            self.insert('""')
            self.move_cursor_relative(columns=-1)
            event.prevent_default()
        if event.character == "'":
            self.insert("''")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()

class pyOS(App):
    BINDINGS = [("m","toggle_dark","Toggle mode"),("ctrl+s","save_file","Save changes"),("ctrl+r","run_active_app","Run app")]
    tmp = ""
    CSS_PATH = "horizontal_layout.tcss"
    def compose(self) -> ComposeResult:
        yield Header(True)
        yield Footer()
        yield FilteredDirectoryTree("./")
        yield ExtendedTextArea.code_editor(language="python")
        self.notify("to pyOS",title="WELCOME")
        self.notify("Redstonedust653",title="Made By:")
        self.notify("Textual",title="WITH")
    
    
    def action_toggle_dark(self):
        self.theme = (
            "nord" if self.theme == "tokyo-night" else "tokyo-night"
        )
        self.notify(f"Mode changed to {str(self.theme)}",title="Alert",severity="information")

    def on_directory_tree_file_selected(self,event):
        try:
            self.file.close()
        except: pass
        self.file = open(str(event.path),'r+')
        self.query_one(ExtendedTextArea).text = self.file.read()
    
    def action_save_file(self):
        try:
            self.file.seek(0)
            self.file.truncate(0)
            self.file.write(self.query_one(ExtendedTextArea).text)
            self.file.flush()
            self.notify("Successfully saved file.",title="Alert",severity="information")
        except:
            self.notify("Unable to save file!", title="ERROR!",severity="error")
    





if __name__ == "__main__":
    app = pyOS()
    app.run()
