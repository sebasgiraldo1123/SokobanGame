"""
Calcula el ancho del canvas, teniendo en cuenta las proporciones
"""
def calculate_canvas_dimensions(num_columns, num_rows, max_height):
    # Tamaño fijo inicial de cada cuadro
    box_size = 65

    # Calcula la altura total del canvas
    height_canvas = box_size * num_rows

    # Si la altura total excede 600, ajustar el tamaño de cada cuadro
    if height_canvas > max_height:
        box_size = max_height / num_rows
        height_canvas = max_height

    # El ancho de cada cuadro es igual al alto
    box_width = box_size

    # Calcula el ancho total del canvas
    width_canvas = box_width * num_columns

    return height_canvas, width_canvas
