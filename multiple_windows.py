
import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Window 1", pos=[300,0]):
    dpg.add_button(label="Button 2")

with dpg.window(label="Window 2"):
    dpg.add_button(label="Button 2")


dpg.create_viewport(title="Custom title", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()