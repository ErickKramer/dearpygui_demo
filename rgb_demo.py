import dearpygui.dearpygui as dpg
import pdb
import math

from matplotlib.pyplot import show

COLOR_PICKER_TAG = "wheel_color_picker"
COLOR_EDITOR_TAG = "wheel_editor_picker"
BUTTON_TAG = "led_turn_button"
NUM_LEDS = 66
LED_TAGS = [f"LED_{i}" for i in range(NUM_LEDS)]

dpg.create_context()


def button_callback():
    print(f"Turning on led...")
    # Modify the color of the of the circle
    for tag in LED_TAGS:
        dpg.configure_item(item=tag, fill=dpg.get_value(item=COLOR_PICKER_TAG))


def picker_callback():
    print(f"Changing LEDs colors..")
    for tag in LED_TAGS:
        dpg.configure_item(item=tag, fill=dpg.get_value(item=COLOR_PICKER_TAG))


def compute_circle_positions(num_points: int, radius: float, center_pos: list) -> list:
    """
        Method to compute the center position of points around a circumference

        Keyword arguments:
        - num_points : int
            Amount of points uniformly distributed around a circumference
        - radius : float
            Radius of the circumference on which to fit the points
        - center_pos : list
            Center position of the circumference on which to fit the points

        Returns:
        - positions : list
            List of center positions of the points around the circumference
    """
    slice = 2 * math.pi/num_points

    positions = []
    for i in range(num_points):
        angle = slice * i

        n_pos_x = center_pos[0] + radius * math.cos(angle)
        n_pos_y = center_pos[1] + radius * math.sin(angle)

        # print(f"x: {n_pos_x}, y: {n_pos_y}")
        positions.append([n_pos_x, n_pos_y])

    return positions


with dpg.window(label="Color Selection", width=400, height=400):
    # Add a color picker
    color_picker = dpg.add_color_picker(display_rgb=True,
                                        display_hsv=True,
                                        picker_mode=dpg.mvColorPicker_wheel,
                                        tag=COLOR_PICKER_TAG,
                                        callback=picker_callback)

    # Add a button to trigger changing the led
    # bt = dpg.add_button(label="Change LEDs color", pos=[
    #                     200, 350], callback=button_callback, tag=BUTTON_TAG)

with dpg.window(label="Led display", width=800, height=800, pos=[400, 0]):
    base_pattern = dpg.draw_circle(radius=350, center=[400, 400], color=[
                                   0, 255, 0], thickness=1, tag="pattern", show=False)

    # Get the configuration data
    pattern_configurations = dpg.get_item_configuration(item="pattern")

    led_pattern_positions = compute_circle_positions(num_points=NUM_LEDS,
                                                     radius=pattern_configurations['radius'],
                                                     center_pos=pattern_configurations['center'])

    for led_idx, led_pos in enumerate(led_pattern_positions):
        dpg.draw_circle(radius=10, center=led_pos, fill=[
                        255, 0, 0], tag=LED_TAGS[led_idx])

# dpg.show_item_registry()
dpg.create_viewport(width=1200, height=1000)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


# TODO
# - Clean up the code
# - Create proper layout
# - Create a method to display as many child windows as desirable
# - Create different patterns with define frequency
#   - Blinking
#   - Rotate on led
#   - "night rider" effect using HSV --> no led intensity effect
#   - Create a pulse effect
