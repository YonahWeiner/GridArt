import streamlit as st
from PIL import Image, ImageDraw

# variables
max_image_width = 600


# helper functions
def draw_grid(image, rows, has_border=False):
    cols = rows
    width, height = image.size
    draw = ImageDraw.Draw(image)
    draw.text((400, 400), "Hello", fill=0)
    for i in range(rows):
        thickness = 5
        if i == rows - 1 and has_border:
            thickness = 10
        draw.line((i * width/cols, 0) + (i * width/cols, height), fill=0, width=thickness)
        draw.line((0, i * height/rows) + (width, i * height/rows), fill=0, width=thickness)


# Layout

# Sidebar
grid_size = st.sidebar.slider("Fineness of graph", min_value=1, max_value=20, value=5, step=1)
st.sidebar.button("Print")

# Main page Layout
st.title("Grid Art")
st.info("Just choose an image and print!")

# load and draw picture
image_file_buffer = st.file_uploader("choose an image", type=["png", "jpg", "jpeg"])
if image_file_buffer is not None:
    img = Image.open(image_file_buffer).convert('L')
    draw_grid(img, grid_size)

    # draw blank grid
    w, h = img.size
    new_width = w + int(w/grid_size)
    new_height = h + int(h/grid_size)

    blank_grid = Image.new(mode='L', size=(new_width, new_height), color=255)
    draw_grid(blank_grid, grid_size + 1, True)
    full_image = blank_grid.copy()

    # superimpose images
    full_image.paste(img, (0, 0))

    # render images
    st.image(full_image, width=max_image_width, caption="{rows}x{rows} grid".format(rows=grid_size))
    st.image(blank_grid, width=max_image_width)



