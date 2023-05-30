import customtkinter as ctk


class MainMenu(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, width=50)
        self.parent = parent
        self.pack_propagate(False)

        self.menu_btn_frame = ctk.CTkFrame(self, fg_color="transparent")

        # TODO: Implemetar correctamente los botones por separado
        [ctk.CTkButton(
            self.menu_btn_frame, text=f"{i+1}", width=40)
            .pack(pady=5) for i in range(5)]

        self.menu_btn_frame.pack(expand=True)

        self.pack(side="left", fill="y")
