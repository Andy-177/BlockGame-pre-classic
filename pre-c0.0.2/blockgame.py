from ursina import *
import blockgen
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
block_kind = 'grass'
def input(key):
    global block_kind
    if key == 'escape':
     quit()
    if key == '1':
        block_kind = 'grass'
    if key == '2':
        block_kind = 'dirt'
    if key == '3':
        block_kind = 'cobblestone'
    if key == '4':
        block_kind = 'stone'
    if key == '5':
        block_kind = 'oak_planks'
    if key == '6':
        block_kind = 'oak_log'
window.exit_button.enabled = False
img = blockgen.Gen_texture(
    'assets/block/grass_side_carried.png',
    'assets/block/dirt.png',
    'assets/block/grass_side_carried.png',
    'assets/block/grass_carried.png',
    'assets/block/grass_side_carried.png',
    'assets/block/grass_side_carried.png',
    'cache/grass_block_texture.png',
)
img2 = blockgen.Gen_texture(
  'assets/block/dirt.png',
  'assets/block/dirt.png',
  'assets/block/dirt.png',
  'assets/block/dirt.png',
  'assets/block/dirt.png',
  'assets/block/dirt.png',
  'cache/dirt_texture.png',
)
img3 = blockgen.Gen_texture(
  'assets/block/cobblestone.png',
  'assets/block/cobblestone.png',
  'assets/block/cobblestone.png',
  'assets/block/cobblestone.png',
  'assets/block/cobblestone.png',
  'assets/block/cobblestone.png',
  'cache/cobblestone_texture.png',
)
img4 = blockgen.Gen_texture(
  'assets/block/stone.png',
  'assets/block/stone.png',
  'assets/block/stone.png',
  'assets/block/stone.png',
  'assets/block/stone.png',
  'assets/block/stone.png',
  'cache/stone_texture.png',
)
img5 = blockgen.Gen_texture(
  'assets/block/oak_planks.png',
  'assets/block/oak_planks.png',
  'assets/block/oak_planks.png',
  'assets/block/oak_planks.png',
  'assets/block/oak_planks.png',
  'assets/block/oak_planks.png',
  'cache/oak_planks_texture.png',
)
img6 = blockgen.Gen_texture(
  'assets/block/oak_log.png',
  'assets/block/oak_log_top.png',
  'assets/block/oak_log.png',
  'assets/block/oak_log_top.png',
  'assets/block/oak_log.png',
  'assets/block/oak_log.png',
  'cache/oak_log_texture.png',
)
grass_texture = load_texture('cache/grass_block_texture.png')
dirt_texture = load_texture('cache/dirt_texture.png')
cobblestone_texture = load_texture('cache/cobblestone_texture.png')
stone_texture = load_texture('cache/stone_texture.png')
oak_planks_texture = load_texture('cache/oak_planks_texture.png')
oak_log_texture = load_texture('cache/oak_log_texture.png')
textures = {
    'grass': grass_texture,
    'dirt': dirt_texture,
    'cobblestone':cobblestone_texture,
    'stone': stone_texture,
    'oak_planks': oak_planks_texture,
    'oak_log': oak_log_texture,
}
class Block(Button):
 def __init__(self, texture, position):
   self.texture_ = textures[texture]
   super().__init__(
     parent = scene,
     position = position,
     model = 'assets/model/block.obj',
     origin_y = 0.5,
     texture = self.texture_,
     color = color.color(0, 0, 0.9),
     scale = 0.5,
     heghlight_color = color.color(0, 0, 1),
   )
 def input(self, key):
   if self.hovered:
     if key == 'right mouse down':
       block = Block(texture=block_kind, position = self.position + mouse.normal)
     if key == 'left mouse down':
       destroy(self)
dx = 16
dy = 2
dz = 16
for x in range(-dx, dx):
 for y in range(-dy+1, dy-1):
   for z in range (-dz, dz):
     block = Block(texture='dirt', position=(x, y , z))
player = FirstPersonController()
app.run()