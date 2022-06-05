import pygame
from constants import *


class Button:
    def __init__(self, parent: pygame.Surface, rect, color, function, **kwargs):
        self.rect = pygame.Rect(rect)
        self.surf = parent.subsurface(self.rect)
        self.surf.set_colorkey(BLACK)

        self.internal_rect = pygame.Rect(0, 0, self.rect.width, self.rect.height)

        self.color = color
        self.function = function
        self.clicked = False
        self.selected = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)

        self.render_text()

    def process_kwargs(self, kwargs):
        """Various optional customization you can change by passing kwargs."""
        settings = {
            "text": None,
            "font": pygame.font.Font(None, 16),
            "call_on_release": True,
            "hover_color": None,
            "clicked_color": None,
            "font_color": pygame.Color("white"),
            "hover_font_color": None,
            "clicked_font_color": None,
            "click_sound": None,
            "hover_sound": None,
            "shape": None,
            "id": None,
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        self.__dict__.update(settings)

    def render_text(self):
        """Pre render the button text."""
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, color)
            self.text = self.font.render(self.text, True, self.font_color)

    def check_event(self, event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function(self)

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            self.function(self)
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self):
        """Update needs to be called every frame in the main loop."""
        color = self.color
        text = self.text
        self.check_hover()
        if self.clicked or self.selected and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hovered and self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text

        if self.shape:
            pygame.draw.polygon(self.surf, WHITE, self.shape)
            pygame.draw.polygon(self.surf, color, self.shape, 5)

        else:
            self.surf.fill(pygame.Color("black"), self.internal_rect)
            self.surf.fill(color, self.internal_rect.inflate(-4, -4))

        if self.text:
            text_rect = text.get_rect(center=self.internal_rect.center)
            self.surf.blit(text, text_rect)

