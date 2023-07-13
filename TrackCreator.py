import pygame
import json

window = pygame.display.set_mode((1200, 800))
r = 50

clock = pygame.time.Clock()
draw_new_line = False
run = True
line_start = [0, 0]


class LineCreator:
    def __init__(self) -> None:
        self._line_being_drawn = False
        self._lines_drawn = []
        self._curent_lines_start = []

    def _start_line(self, new_line_start: list()):
        self._curent_lines_start = new_line_start
        self._line_being_drawn = True

    def _end_line(self, line_end):
        self._lines_drawn.append({"start": self._curent_lines_start, "end": line_end})
        self._line_being_drawn = False
        self._curent_lines_start = ()

    def add_line_point(self, new_line_pos: list()):
        if self._line_being_drawn:
            self._end_line(new_line_pos)
        else:
            self._start_line(new_line_pos)

    def draw_lines(self, window, mouse_pos):
        for line in self._lines_drawn:
            pygame.draw.line(window, "white", line["start"], line["end"])
        if self._line_being_drawn:
            pygame.draw.line(window, "white", self._curent_lines_start, mouse_pos)

    def write_track_to_json(self):
        with open("track.json", "w") as outfile:
            json.dump(self._lines_drawn, outfile)


test = LineCreator()

while run:

    cpt = pygame.mouse.get_pos()
    clock.tick(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test.write_track_to_json()
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            test.add_line_point(cpt)

    window.fill("black")
    test.draw_lines(window, cpt)
    pygame.draw.circle(window, "white", cpt, r, 3)
    pygame.display.flip()

pygame.quit()
exit()