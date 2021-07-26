from tksheet import Sheet
import tkinter as tk


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                           data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(5)] for r in range(15)])
        self.sheet.enable_bindings(("single_select",
                                    "drag_select",
                                    "select_all",
                                    "column_select",
                                    "row_select",
                                    "column_width_resize",
                                    "double_click_column_resize",
                                    "arrowkeys",
                                    "row_height_resize",
                                    "double_click_row_resize",
                                    "right_click_popup_menu",
                                    "rc_select"
                                    ))
        self.sheet.popup_menu_add_command("Say Hello", self.new_right_click_button)
        self.sheet.popup_menu_add_command("Edit Cell", self.edit_cell, index_menu = False, header_menu = False)
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")

    def new_right_click_button(self, event = None):
        print ("Hello World!")

    def edit_cell(self, event = None):
        r, c = self.sheet.get_currently_selected()
        self.sheet.row_height(row = r, height = "text", only_set_if_too_small = True, redraw = False)
        self.sheet.column_width(column = c, width = "text", only_set_if_too_small = True, redraw = True)
        self.sheet.create_text_editor(row = r,
                                      column = c,
                                      text = self.sheet.get_cell_data(r, c),
                                      set_data_ref_on_destroy = False,
                                      binding = self.end_edit_cell)

    def end_edit_cell(self, event = None):
        newtext = self.sheet.get_text_editor_value(event,
                                                   r = event[0],
                                                   c = event[1],
                                                   set_data_ref_on_destroy = True,
                                                   move_down = True,
                                                   redraw = True,
                                                   recreate = True)
        print (newtext)


app = demo()
app.mainloop()