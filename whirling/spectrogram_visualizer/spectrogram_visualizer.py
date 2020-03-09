import time
import math
import librosa
import pygame as pg
from enum import Enum
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GL.shaders
import numpy as np
from whirling import colors
from whirling.primitives import Rect
from whirling.ui_visualizer_base import UIVisualizerBase
from whirling.ui_audio_controller import UIAudioController
from matplotlib import cm
from whirling import viridis
from whirling.spectrogram_visualizer import spectrogram


class SpecState(Enum):
    LOADING = 0
    LOADED = 1
    LOADED_NEXT = 2

class SpectrogramVisualizer(UIVisualizerBase):
    def __init__(self, rect, audio_controller: UIAudioController, **kwargs):
        # Initialize base class.
        super().__init__(rect=rect, audio_controller=audio_controller, **kwargs)

        # The size of the spectrogram clip in seconds.
        self.seconds_worth: int = 8

        # What clip of full spectrogram we are looking at.
        self.spec_window = None

        # If the current spec has been loaded.
        self.curr_spec_state = None

    def initialize_spectrogram(self):

        curr_time = self.audio_controller.get_time()
        if self.spec_window == math.floor(curr_time / self.seconds_worth):
            return

        self.curr_spec_state = SpecState.LOADING
        t0 = time.time()
        self.spec_window = math.floor(curr_time / self.seconds_worth)

        # Create the spectrogram.
        top = self.height/3  + self.rect.bottom
        spec_rect = Rect(self.rect.left, top, self.rect.right, self.rect.bottom)
        self.spec = spectrogram.Spectrogram(spec_rect, 'data/latch.mp3',
            self.sr, curr_time, self.seconds_worth)

        self.curr_spec_state = SpecState.LOADED
        print(f'Total time: {time.time() - t0}')

    def draw(self):
        super().draw()

        # Create spectrogram if it doesn't exist for this spec window.
        self.initialize_spectrogram()

        if self.curr_spec_state == SpecState.LOADED:
            self.spec.draw()

        # Draw time indicator.
        curr_time = self.audio_controller.get_time()
        curr_window_number = math.floor(curr_time/self.seconds_worth)
        min_window_time = curr_window_number * self.seconds_worth
        max_window_time = (curr_window_number + 1) * self.seconds_worth
        self.draw_time_indicator(curr_time, min_window_time, max_window_time)

    def draw_time_indicator(self, curr_time, min_time, max_time):
        if max_time == 0:
            return
        fraction = (curr_time - min_time) / (max_time - min_time)
        x = self.width * fraction + self.rect.left
        glBegin(GL_LINES)
        glColor3fv(colors.GRAY)
        glVertex2f(x, self.rect.top)
        glVertex2f(x, self.rect.bottom)
        glEnd()
