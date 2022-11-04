from seleniumbase import BaseCase
from infrastructure.configurations import config
from infrastructure.page_objects import general, txt_inputs, dropdowns, clicks, slider, iframes, radio_buttons, \
    checkboxs, drag_drops


class sanity(BaseCase):

    def test_open_page(self):
        # Open a web page in the active browser window
        self.open(config.base_url)
        # Assert the title of the current web page
        self.assert_title("Web Testing Page")
        # Assert that an element is visible on the page
        self.assert_element(general.full_page)
        # Assert that a text substring appears in an element
        self.assert_text("Demo Page", general.demo_page_h1)

    def test_text_fields(self):
        # Type text into various text fields and then assert
        self.open(config.base_url)
        self.type(txt_inputs.text_input_field, "Hello all!")
        self.type(txt_inputs.textarea, "I'm Kfir,\n Kfir Kanizo")
        self.type(txt_inputs.prefilled_text_field, "And I'm typing text.")
        self.assert_text("Hello all!", txt_inputs.text_input_field)
        self.assert_text("I'm Kfir,\n Kfir Kanizo", txt_inputs.textarea)
        self.assert_text("And I'm typing text.", txt_inputs.prefilled_text_field)

    def test_drop_down(self):
        self.open(config.base_url)
        # Hover & click a dropdown element and assert results
        self.assert_text("Automation Practice", general.dynamic_dropdown_h3)
        try:
            self.hover_and_click(dropdowns.drop_down, dropdowns.opt_two, timeout=1)
        except Exception:
            # Someone moved the mouse while the test ran
            self.js_click(dropdowns.opt_two)
        self.assert_text("Link Two Selected", general.dynamic_dropdown_h3)

    def test_click(self):
        self.open(config.base_url)
        # Click a button and then verify the expected results
        self.assert_text("This Text is Green", clicks.paragraph_with_text)
        self.click(clicks.button)
        self.assert_text("This Text is Purple", clicks.paragraph_with_text)

    def test_svg_visibility(self):
        self.open(config.base_url)
        # Assert that the given SVG is visible on the page
        self.assert_element(general.html_svg_with_rect)

    def test_slider(self):
        self.open(config.base_url)
        # Verify that a slider control updates a progress bar
        self.assert_element(slider.get_progress("50"))
        self.press_down_arrow(slider.my_slider, times=5)
        self.assert_element(slider.get_progress("0"))
        self.press_up_arrow(slider.my_slider, times=10)
        self.assert_element(slider.get_progress("100"))

    def test_select_drop_down(self):
        self.open(config.base_url)
        # Verify that a "select" option updates a meter bar
        self.assert_element(dropdowns.quarter_meter)
        self.select_option_by_text(dropdowns.select_drop_down, "Set to 75%")
        self.assert_element(dropdowns.three_quarters_quarter)

    def test_iframe_img(self):
        self.open(config.base_url)
        # Assert an element located inside an iFrame
        self.assert_false(self.is_element_visible("img"))
        self.switch_to_frame(iframes.img_iframe)
        self.assert_true(self.is_element_visible("img"))
        self.switch_to_default_content()

    def test_iframe_text(self):
        self.open(config.base_url)
        # Assert text located inside an iFrame
        self.assert_false(self.is_text_visible("iFrame Text"))
        self.switch_to_frame(iframes.txt_iframe)
        self.assert_true(self.is_text_visible("iFrame Text"))
        self.switch_to_default_content()

    def test_radio_button(self):
        self.open(config.base_url)
        # Verify that clicking a radio button selects it
        self.assert_false(self.is_selected(radio_buttons.rb_two))
        self.click(radio_buttons.rb_two)
        self.assert_true(self.is_selected(radio_buttons.rb_two))

    def test_check_box(self):
        self.open(config.base_url)
        # Verify that clicking a checkbox makes it selected
        self.assert_element_not_visible(checkboxs.logo)
        self.assert_false(self.is_selected(checkboxs.check_box_one))
        self.click(checkboxs.check_box_one)
        self.assert_true(self.is_selected(checkboxs.check_box_one))
        self.assert_element(checkboxs.logo)

    def test_multiple_checkbox(self):
        self.open(config.base_url)
        # Verify clicking on multiple elements with one call
        self.assert_false(self.is_selected(checkboxs.check_box_two))
        self.assert_false(self.is_selected(checkboxs.check_box_three))
        self.assert_false(self.is_selected(checkboxs.check_box_four))
        self.click_visible_elements(checkboxs.bulk_checking)
        self.assert_true(self.is_selected(checkboxs.check_box_two))
        self.assert_true(self.is_selected(checkboxs.check_box_three))
        self.assert_true(self.is_selected(checkboxs.check_box_four))

    def test_iframe_checkbox(self):
        self.open(config.base_url)
        # Verify that clicking an iFrame checkbox selects it
        self.assert_false(self.is_element_visible(checkboxs.check_box_six))
        self.switch_to_frame(iframes.checkbox_iframe)
        self.assert_true(self.is_element_visible(checkboxs.check_box_six))
        self.assert_false(self.is_selected(checkboxs.check_box_six))
        self.click(checkboxs.check_box_six)
        self.assert_true(self.is_selected(checkboxs.check_box_six))
        self.switch_to_default_content()

    def test_drag_and_drop(self):
        self.open(config.base_url)
        # Verify Drag and Drop
        self.click(checkboxs.check_box_one)
        self.assert_element_not_visible(drag_drops.element_in_place)
        self.drag_and_drop(checkboxs.logo, drag_drops.drop)
        self.assert_element(drag_drops.element_in_place)

    def test_link_text(self):
        self.open(config.base_url)
        # Assert link text
        self.assert_link_text("seleniumbase.com")
        self.assert_link_text("SeleniumBase on GitHub")
        self.assert_link_text("seleniumbase.io")
        # Click link text
        self.click_link("SeleniumBase Demo Page")

    def test_exact_text(self):
        self.open(config.base_url)
        # Assert exact text
        self.assert_exact_text("Demo Page", general.demo_page_h1)

    def test_highlight_element(self):
        self.open(config.base_url)
        # Highlight a page element (Also asserts visibility)
        self.highlight("h2")
