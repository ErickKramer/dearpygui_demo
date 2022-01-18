import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="tutorial"):
    color_picker = dpg.add_color_picker(display_rgb=True, display_hsv=True, picker_mode=dpg.mvColorPicker_wheel)

dpg.create_viewport(title="Custom title", width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()