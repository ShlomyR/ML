#funt class
class Funt():
	def __init__(self, message, location):
		color = (255, 255, 255)
		check = True
		self.message = font.render(f'{message} ', check, color)
		self.location = self.message.get_rect()

	def draw(self, surface):

		#draw button on screen
		surface.blit(self.message, (self.message, self.location))

