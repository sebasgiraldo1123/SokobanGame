from PIL import Image, ImageDraw, ImageFont

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


"""
Crea la imagen con extensión png de un número entregado por parámetro
"""
def create_number_image(number, filepath):
    # Crear una imagen con fondo transparente
    image_size = (100, 100)
    image = Image.new("RGBA", image_size, (255, 255, 255, 110))

    # Crear un objeto para dibujar
    draw = ImageDraw.Draw(image)

    # Definir el tamaño y tipo de fuente (cambiar la ruta a una fuente si es necesario)
    font_size = 30  # Ajusta este valor según sea necesario
    font = ImageFont.truetype("arialbd.ttf", font_size)

    # Posición del texto (ajustar según sea necesario)
    text_position = (10, 10)

    # Dibujar el número
    draw.text(text_position, str(number), fill=(0, 0, 0), font=font)

    # Guardar la imagen
    image.save(filepath, "PNG")

