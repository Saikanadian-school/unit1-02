
import ui

my_pic = ui.Image.named('./sprites/MT_crest.jpg')

my_image = ui.ImageView(frame=(100, 100, 200, 300))

my_image.image = my_pic

view = ui.load_view()


view.add_subview(my_image)
view.present('full_screen')
