import pandas as pd
import numpy as np
from functools import partial

class TableStyler():

    def __init__(self, table_name='', default='MediumSeaGreen', yellow='khaki', red='salmon', css_styles='styles.css', round_param=2):
        """
        Parameters:

table_name: (str, optional) The name to be displayed as an <h1> heading above the table.

default: (str, optional) The default background color for cells in the absence of specific conditions.

yellow: (str, optional) The background color for cells that meet the yellow threshold condition.

red: (str, optional) The background color for cells that meet the red threshold condition.

css_styles: (str, optional) The path to a CSS file containing additional styles. If not provided or the file does not exist, the table will be output without using styles.

round_param: (int, optional) The number of decimal places to round numeric values in the table.
Functionality:

Initializes the TableStyler object with the specified parameters.
Reads additional CSS styles from a file if provided.

        """
    
        self.table_name = '<h1>' + table_name + '</h1>'
        self.default = default
        self.yellow = yellow 
        self.red = red
        self.round_param = round_param
        try:
            with open(css_styles, 'r') as file:
                self.css_styles = '<style>' + file.read() + '</style>'
                print(f'___________the {css_styles} was read successfuly___________')
        except:
            self.css_styles = ''
            print(f'___________{css_styles} does not exist. The table will be output without using styles___________')
            

    def __change_background_color(self, cell_val, y_thresh, r_thresh, abs_mode):
        if abs_mode:
            cell_val = abs(cell_val)
        if cell_val > r_thresh:
            background_color = f'background-color: {self.red}'
        elif cell_val > y_thresh:
            background_color = f'background-color: {self.yellow}'
        else:
            background_color = f'background-color: {self.default}'
        return background_color

        
    def style(self, df, y_thresh, r_thresh, cols=None, abs_mode=False):
        """
        Parameters:

df: The Pandas DataFrame to be styled.

y_thresh: The yellow threshold for background color.

r_thresh: The red threshold for background color.

cols: (list, optional) List of columns to apply styling to. If not provided, styling is applied to the entire DataFrame.

abs_mode: Boolean indicating whether to consider the absolute value of DataFrame values.
Returns:

An HTML representation of the styled DataFrame with additional styles and heading.
Functionality:

Applies the background color styling to the DataFrame based on the conditions specified in __change_background_color.
Converts the styled DataFrame to an HTML representation, including the specified table name and additional CSS styles.
        """
        
        highlight_func = partial(self.__change_background_color, y_thresh=y_thresh, r_thresh=r_thresh, abs_mode=abs_mode)
        if cols:
            styled_df = df.style.applymap(highlight_func, subset=cols).set_precision(self.round_param)
        else:
            styled_df = df.style.applymap(highlight_func).set_precision(self.round_param)
        styled_html = '<div>' + self.css_styles + self.table_name + styled_df.render() + '</div>'
        return styled_html

