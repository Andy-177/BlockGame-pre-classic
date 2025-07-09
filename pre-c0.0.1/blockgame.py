from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
def input(key):
    if key == 'escape':
     quit()
window.exit_button.enabled = False

dirt_texture = load_texture('assets/block/dirt.png')
textures = {
    'dirt': dirt_texture,
}
class Block(Button):
 def __init__(self, texture, position):
   self.texture_ = textures[texture]
   super().__init__(
     parent = scene,
     position = position,
     model = 'cube',
     origin_y = 0.5,
     texture = self.texture_,
     color = color.color(0, 0, 0.9),
     heghlight_color = color.color(0, 0, 1),
   )
 def input(self, key):
   if self.hovered:
     if key == 'left mouse down':
       destroy(self)
     if key == 'right mouse down':
       block = Block(texture='dirt', position = self.position + mouse.normal)
   
dx = 16
dy = 2
dz = 16
for x in range(-dx, dx-1):
 for y in range(-dy+1, dy-1):
   for z in range (-dz, dz-1):
     block = Block(texture='dirt', position=(x, y , z))
player = FirstPersonController()
app.run()