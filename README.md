### TableStyler Class

The TableStyler class is designed to style and display a Pandas DataFrame in an HTML format. It allows users to set different background colors for cells based on certain conditions. The class is initialized with parameters for table styling, and it provides a method (`style`) to generate an HTML representation of the styled DataFrame.

#### Methods:

#### __init__(self, table_name='', default='MediumSeaGreen', yellow='khaki', red='salmon', css_styles='styles.css', round_param=2)

- Parameters:
  - table_name: (str, optional) The name to be displayed as an <h1> heading above the table.
  - default: (str, optional) The default background color for cells in the absence of specific conditions.
  - yellow: (str, optional) The background color for cells that meet the yellow threshold condition.
  - red: (str, optional) The background color for cells that meet the red threshold condition.
  - css_styles: (str, optional) The path to a CSS file containing additional styles. If not provided or the file does not exist, the table will be output without using styles.
  - round_param: (int, optional) The number of decimal places to round numeric values in the table.

- Functionality:
  - Initializes the TableStyler object with the specified parameters.
  - Reads additional CSS styles from a file if provided.

#### __change_background_color(self, cell_val, y_thresh, r_thresh, abs_mode)

- Parameters:
  - cell_val: The value of the DataFrame cell.
  - y_thresh: The yellow threshold for background color.
  - r_thresh: The red threshold for background color.
  - abs_mode: Boolean indicating whether to consider the absolute value of cell_val.

- Returns:
  - A string specifying the background color based on the conditions.

- Functionality:
  - Determines the appropriate background color for a cell based on specified thresholds and conditions.

#### style(self, df, y_thresh, r_thresh, cols=None, abs_mode=False)

- Parameters:
  - df: The Pandas DataFrame to be styled.
  - y_thresh: The yellow threshold for background color.
  - r_thresh: The red threshold for background color.
  - cols: (list, optional) List of columns to apply styling to. If not provided, styling is applied to the entire DataFrame.
  - abs_mode: Boolean indicating whether to consider the absolute value of DataFrame values.

- Returns:
  - An HTML representation of the styled DataFrame with additional styles and heading.
  
- Functionality:
  - Applies the background color styling to the DataFrame based on the conditions specified in __change_background_color.
  - Converts the styled DataFrame to an HTML representation, including the specified table name and additional CSS styles.