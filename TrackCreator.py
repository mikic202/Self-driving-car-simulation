import pygame
import json
import argparse
from TrackConstants import TrackConstants
from typing import List

window = pygame.display.set_mode((1200, 800))
curcor_radious = 5

clock = pygame.time.Clock()
run = True

parser = argparse.ArgumentParser("TrackCreator")
parser.add_argument("-f", "--file", type=str, default="track", help="defines output file name (without extension)")
args = parser.parse_args()


class LineCreator:
    def __init__(self, output_file: str) -> None:
        self._line_being_drawn = False
        self._gate_being_drawn = False
        self._gates_drawn = []
        self._curent_gate_start = []
        self._lines_drawn = []
        self._curent_lines_start = []
        self._output_file = output_file
        self._start_point = None

    def _start_line(self, new_line_start: List[int]):
        self._curent_lines_start = new_line_start
        self._line_being_drawn = True

    def _end_line(self, line_end: List[int]):
        self._lines_drawn.append({TrackConstants.LINE_START.value: self._curent_lines_start, TrackConstants.LINE_END.value: line_end})
        self._line_being_drawn = False
        self._curent_lines_start = ()

    def add_start_point(self, start_point: List[int]):
        self._start_point = start_point

    def add_line_point(self, new_line_pos: List[int]):
        if self._gate_being_drawn:
            return
        if self._line_being_drawn:
            self._end_line(new_line_pos)
        else:
            self._start_line(new_line_pos)

    def add_gate(self, line_point: List[int]):
        if self._line_being_drawn:
            return
        if self._gate_being_drawn:
            self._gates_drawn.append({TrackConstants.LINE_START.value: self._curent_gate_start, TrackConstants.LINE_END.value: line_point})
            self._gate_being_drawn = False
            self._curent_gate_start = ()
        else:
            self._curent_gate_start = line_point
            self._gate_being_drawn = True

    def draw_track(self, window, mouse_pos: List[int]):
        for line in self._lines_drawn:
            pygame.draw.line(window, "white", line[TrackConstants.LINE_START.value], line[TrackConstants.LINE_END.value])
        if self._line_being_drawn:
            pygame.draw.line(window, "white", self._curent_lines_start, mouse_pos)

        for gate in self._gates_drawn:
            pygame.draw.line(window, "green", gate[TrackConstants.LINE_START.value], gate[TrackConstants.LINE_END.value])
        if self._gate_being_drawn:
            pygame.draw.line(window, "green", self._curent_gate_start, mouse_pos)

        if self._start_point:
            pygame.draw.circle(window, (255, 100, 100), self._start_point, 8)

    def write_track_to_json(self):
        with open(self._output_file + ".json", "w") as outfile:
            json.dump({TrackConstants.TRACK.value: self._lines_drawn, TrackConstants.START_POINT.value: self._start_point, TrackConstants.GATES.value: self._gates_drawn}, outfile)


test = LineCreator(args.file)

while run:

    cpt = pygame.mouse.get_pos()
    clock.tick(250)
    keys_press = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            test.write_track_to_json()
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and keys_press[pygame.K_LSHIFT]:
            test.add_start_point(cpt)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                test.add_line_point(cpt)
            if event.button == 3:
                test.add_gate(cpt)

    window.fill("black")
    test.draw_track(window, cpt)
    pygame.draw.circle(window, "white", cpt, curcor_radious, 3)
    pygame.display.flip()

pygame.quit()
exit()