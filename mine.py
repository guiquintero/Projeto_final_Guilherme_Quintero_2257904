#Programado por Guilherme Quintero Lorenzi RA:2257904
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import basic_lighting_shader

app = Ursina()
textura_grama = load_texture('assets/grama.png')
textura_pedra = load_texture('assets/pedra.png')
textura_folha = load_texture('assets/folha.png')
textura_madeira = load_texture('assets/madeira.png')
sky_texture   = load_texture('assets/skybox.png')
arm_texture   = load_texture('assets/arm_texture.png')
break_som   = Audio('assets/break_som',loop = False, autoplay = False)
block_pick = 1

window.fps_counter.enabled = False
window.exit_button.visible = False


def update():
	global block_pick
	
	# if held_keys['l']:
	# 	if luz:
	# 		luz=False
	# 	else:
	# 		luz=True

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = textura_grama):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5,
			#shaders=basic_lighting_shader,
			#shadows=False,
			#shader=lit_with_shadows_shader
			)

	
	def input(self,key):
		if self.hovered:
			if key == 'right mouse down':
				break_som.play()
				if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = textura_grama)
				if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = textura_pedra)
				if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = textura_folha)
				if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = textura_madeira)
                
			if key == 'left mouse down':

				break_som.play()
				destroy(self)
            

class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)

pivot=Entity()
#DirectionalLight(parent=pivot, y=2, z=3, rotation=(45,-45,45), shadows= True)
#DirectionalLight(parent=pivot, y=30, z=10, shadows=True)

for z in range(20):
	for x in range(20):
		voxel = Voxel(position = (x,0,z),)

###################ARVORE##############
voxel = Voxel(position = (10,1,10), texture = textura_madeira)
voxel = Voxel(position = (10,2,10), texture = textura_madeira)
voxel = Voxel(position = (10,3,10), texture = textura_madeira)
voxel = Voxel(position = (10,4,10), texture = textura_madeira)
voxel = Voxel(position = (10,5,10), texture = textura_madeira)

voxel = Voxel(position = (11,4,11), texture = textura_folha)
voxel = Voxel(position = (11,4,10), texture = textura_folha)
voxel = Voxel(position = (11,4,9), texture = textura_folha)
voxel = Voxel(position = (10,4,11), texture = textura_folha)
voxel = Voxel(position = (10,4,9), texture = textura_folha)
voxel = Voxel(position = (9,4,11), texture = textura_folha)
voxel = Voxel(position = (9,4,10), texture = textura_folha)
voxel = Voxel(position = (9,4,9), texture = textura_folha)

voxel = Voxel(position = (12,4,11), texture = textura_folha)
voxel = Voxel(position = (12,4,10), texture = textura_folha)
voxel = Voxel(position = (12,4,9), texture = textura_folha)
voxel = Voxel(position = (8,4,11), texture = textura_folha)
voxel = Voxel(position = (8,4,10), texture = textura_folha)
voxel = Voxel(position = (8,4,9), texture = textura_folha)
voxel = Voxel(position = (11,4,12), texture = textura_folha)
voxel = Voxel(position = (10,4,12), texture = textura_folha)
voxel = Voxel(position = (9,4,12), texture = textura_folha)
voxel = Voxel(position = (11,4,8), texture = textura_folha)
voxel = Voxel(position = (10,4,8), texture = textura_folha)
voxel = Voxel(position = (9,4,8), texture = textura_folha)

voxel = Voxel(position = (11,3,11), texture = textura_folha)
voxel = Voxel(position = (11,3,10), texture = textura_folha)
voxel = Voxel(position = (11,3,9), texture = textura_folha)
voxel = Voxel(position = (10,3,11), texture = textura_folha)
voxel = Voxel(position = (10,3,9), texture = textura_folha)
voxel = Voxel(position = (9,3,11), texture = textura_folha)
voxel = Voxel(position = (9,3,10), texture = textura_folha)
voxel = Voxel(position = (9,3,9), texture = textura_folha)

voxel = Voxel(position = (12,3,11), texture = textura_folha)
voxel = Voxel(position = (12,3,10), texture = textura_folha)
voxel = Voxel(position = (12,3,9), texture = textura_folha)
voxel = Voxel(position = (8,3,11), texture = textura_folha)
voxel = Voxel(position = (8,3,10), texture = textura_folha)
voxel = Voxel(position = (8,3,9), texture = textura_folha)
voxel = Voxel(position = (11,3,12), texture = textura_folha)
voxel = Voxel(position = (10,3,12), texture = textura_folha)
voxel = Voxel(position = (9,3,12), texture = textura_folha)
voxel = Voxel(position = (11,3,8), texture = textura_folha)
voxel = Voxel(position = (10,3,8), texture = textura_folha)
voxel = Voxel(position = (9,3,8), texture = textura_folha)

voxel = Voxel(position = (11,5,11), texture = textura_folha)
voxel = Voxel(position = (11,5,10), texture = textura_folha)
voxel = Voxel(position = (11,5,9), texture = textura_folha)
voxel = Voxel(position = (10,5,11), texture = textura_folha)
voxel = Voxel(position = (10,5,9), texture = textura_folha)
voxel = Voxel(position = (9,5,11), texture = textura_folha)
voxel = Voxel(position = (9,5,10), texture = textura_folha)
voxel = Voxel(position = (9,5,9), texture = textura_folha)


###############MORRO#####################
voxel = Voxel(position = (19,1,19), texture = textura_grama)
voxel = Voxel(position = (18,1,19), texture = textura_grama)
voxel = Voxel(position = (17,1,19), texture = textura_grama)
voxel = Voxel(position = (16,1,19), texture = textura_grama)
voxel = Voxel(position = (15,1,19), texture = textura_grama)
voxel = Voxel(position = (14,1,19), texture = textura_grama)
voxel = Voxel(position = (13,1,19), texture = textura_grama)

voxel = Voxel(position = (19,1,18), texture = textura_grama)
voxel = Voxel(position = (19,1,17), texture = textura_grama)
voxel = Voxel(position = (19,1,16), texture = textura_grama)
voxel = Voxel(position = (19,1,15), texture = textura_grama)
voxel = Voxel(position = (19,1,14), texture = textura_grama)
voxel = Voxel(position = (19,1,13), texture = textura_grama)

voxel = Voxel(position = (18,1,18), texture = textura_grama)
voxel = Voxel(position = (18,1,17), texture = textura_grama)
voxel = Voxel(position = (18,1,16), texture = textura_grama)
voxel = Voxel(position = (18,1,15), texture = textura_grama)
voxel = Voxel(position = (18,1,14), texture = textura_grama)


voxel = Voxel(position = (17,1,18), texture = textura_grama)
voxel = Voxel(position = (16,1,18), texture = textura_grama)
voxel = Voxel(position = (15,1,18), texture = textura_grama)
voxel = Voxel(position = (14,1,18), texture = textura_grama)

voxel = Voxel(position = (17,1,17), texture = textura_grama)
voxel = Voxel(position = (17,1,16), texture = textura_grama)
voxel = Voxel(position = (17,1,15), texture = textura_grama)

voxel = Voxel(position = (16,1,17), texture = textura_grama)
voxel = Voxel(position = (15,1,17), texture = textura_grama)

voxel = Voxel(position = (16,1,16), texture = textura_grama)

################PEDRA############################
voxel = Voxel(position = (19,2,19), texture = textura_pedra)
voxel = Voxel(position = (19,2,18), texture = textura_pedra)
voxel = Voxel(position = (19,2,17), texture = textura_pedra)
voxel = Voxel(position = (19,2,16), texture = textura_pedra)

voxel = Voxel(position = (18,2,19), texture = textura_pedra)
voxel = Voxel(position = (18,2,18), texture = textura_pedra)
voxel = Voxel(position = (18,2,17), texture = textura_pedra)

voxel = Voxel(position = (17,2,19), texture = textura_pedra)
voxel = Voxel(position = (17,2,18), texture = textura_pedra)

voxel = Voxel(position = (19,3,19), texture = textura_pedra)
voxel = Voxel(position = (18,3,19), texture = textura_pedra)
voxel = Voxel(position = (19,3,18), texture = textura_pedra)

voxel = Voxel(position = (19,4,19), texture = textura_pedra)
voxel = Voxel(position = (18,4,19), texture = textura_pedra)
voxel = Voxel(position = (19,4,18), texture = textura_pedra)

voxel = Voxel(position = (-1,1,-1), texture = textura_pedra)
voxel = Voxel(position = (-1,1,0), texture = textura_pedra)
voxel = Voxel(position = (0,1,-1), texture = textura_pedra)
voxel = Voxel(position = (-1,1,1), texture = textura_pedra)
voxel = Voxel(position = (1,1,-1), texture = textura_pedra)




player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()

