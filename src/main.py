from pathlib import Path
from pydoc import doc
from typing import Iterable
from textual.color import Color

from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree, Static
from textual.containers import Vertical
from rich.text import Text
from textual import events
from textual.widgets import *
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Input, Button
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label
from rich.theme import Theme

custom_theme = {"info": "dim cyan", "warning": "magenta", "danger": "bold red"}

INVALID_DIRECTORIES = [
    "ASSETS",
    "DIAGRAMS"
    # "GENERAL",
    # "DISCIPLINES",
    # "SOFTWARE_DEVELOPMENT",
    # "ONBOARDING",
    # "CONTRIBUTING",
]


class NewFileModal(Screen):
    def __init__(self, directory: Path):
        super().__init__()
        self.directory = directory
        self.input = Input(placeholder="Enter new file name", id="input")

    def compose(self) -> ComposeResult:
        yield Grid(
            self.input,
            Button("Create", id="create"),
            id="dialog",
        )


class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        for path in paths:
            # check if relative to any of the valid paths
            if path.name.upper() in INVALID_DIRECTORIES:
                continue
            if path.is_dir():
                yield path


class DirectoryTreeApp(App):
    CSS_PATH = "tstyles.tcss"
    BINDINGS = [
        ("ctrl+n", "new_file()", "New File In Selected Directory"),
        ("q", "quit()", "Quit"),
        Binding(
            "space",
            "toggle_node",
            description="Show/Hide Contents",
            show=True,
            priority=True,
        ),
        Binding(
            "enter",
            "select_cursor",
            description="Select Directory",
            show=True,
            priority=True,
        ),
    ]

    def compose(self) -> ComposeResult:
        self.selected_directory: Path | None = None
        with Vertical():
            help_text = Text("Select a directory\n", style="none")
            help = Static(help_text)
            self.selected_path_display = help
            yield self.selected_path_display

            docs_path = Path("docs")
            assert docs_path.exists()
            tree = FilteredDirectoryTree(docs_path, name="Docs Directory")
            yield tree

            yield Footer()

    def action_new_file(self) -> None:
        """Check if there is a selected directory, and if so, show input modal for new file name."""
        if self.selected_directory is None:
            self.selected_path_display.update("No directory selected")
            return
        # Create and show the NewFileModal with the current selected directory
        self.push_screen(NewFileModal(self.selected_directory))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle the input submitted from the NewFileModal."""
        if event.input.value and self.selected_directory is not None:
            path_ = self.selected_directory / event.input.value
            self.exit(result=path_)

    def on_directory_tree_directory_selected(
        self, event: DirectoryTree.DirectorySelected
    ) -> None:
        """Handle the event when a directory is selected."""
        if event.path.name == "docs":
            msg = Text(
                "You cannot create a file in the docs directory",
                style=custom_theme["danger"],
            )
            msg.append("\nTry Again", style=custom_theme["info"])
            self.selected_path_display.update(msg)
            # reset the App
            return
        self.selected_directory = event.path
        self.selected_path_display.update(f"You've Selected: {self.selected_directory}")


if __name__ == "__main__":
    from rich import print
    path = DirectoryTreeApp().run()
    if path is None:
        exit(0)
    full_path = Path(path)

    if full_path.exists():
        print(f"File [bold red]{full_path}[/bold red] already exists")
        exit(1)
    elif not full_path.parent.exists():
        print(f"Creating directory {full_path.parent}")
        full_path.parent.mkdir(parents=True)

    # create file
    full_path.touch()

    # Create the file
    with open(full_path, "w") as f:
        f.write(f"# {full_path.name}\n")


    print(f"Created file [green]file://{full_path.as_posix()}[/green]")
