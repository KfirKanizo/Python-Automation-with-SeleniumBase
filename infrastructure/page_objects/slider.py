my_slider = "//input[@id='mySlider']"


def get_progress(value):
    progress_bar = "//progress[@value='" + value + "']"
    return progress_bar
