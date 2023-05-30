from lib import View


class ViewController:
    def __init__(self, initial_view: View) -> None:
        self.current_view = initial_view
        self.current_view.show()

    def change_view(self, view: View) -> None:
        self.current_view.remove()
        view.show()
        self.current_view = view
