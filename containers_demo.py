import dearpygui.dearpygui as dpg

dpg.create_context()

def button_callback(sender, app_data, user_data):
    print(f"sender is {sender}")
    print(f"app_data is {app_data}")
    print(f"user_data is {user_data}")

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Button 1", callback=button_callback, user_data="Some data")
    dpg.add_button(label="Button 2")
    with dpg.group():
        dpg.add_button(label="Button 3")
        dpg.add_button(label="Button 4")

        with dpg.group() as group1:
            pass

dpg.add_button(label="Button 5", parent=group1)

dpg.create_viewport(title="Custom title", width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()