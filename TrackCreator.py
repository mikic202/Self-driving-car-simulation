import pygame
import json
import argparse

LINE_START = "start"
LINE_END = "end"

window = pygame.display.set_mode((1200, 800))
r = 5

clock = pygame.time.Clock()
draw_new_line = False
run = True
line_start = [0, 0]

parser = argparse.ArgumentParser("TrackCreator")
parser.add_argument("-f", "--file", type=str, default="track.json", help="defines output file name (without extension)")
args = parser.parse_args()


class LineCreator:
    def __init__(self, output_file: str) -> None:
        self._line_being_drawn = False
        self._lines_drawn = []
        self._curent_lines_start = []
        self._output_file = output_file

    def _start_line(self, new_line_start: list()):
        self._curent_lines_start = new_line_start
        self._line_being_drawn = True

    def _end_line(self, line_end):
        self._lines_drawn.append({LINE_START: self._curent_lines_start, LINE_END: line_end})
        self._line_being_drawn = False
        self._curent_lines_start = ()

    def add_line_point(self, new_line_pos: list()):
        if self._line_being_drawn:
            self._end_line(new_line_pos)
        else:
            self._start_line(new_line_pos)

    def draw_lines(self, window, mouse_pos):
        for line in self._lines_drawn:
            pygame.draw.line(window, "white", line[LINE_START], line[LINE_END])
        if self._line_being_drawn:
            pygame.draw.line(window, "white", self._curent_lines_start, mouse_pos)

    def write_track_to_json(self):
        with open(self._output_file + ".json", "w") as outfile:
            json.dump(self._lines_drawn, outfile)


test = LineCreator(args.file)

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