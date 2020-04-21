import math
from enum import Enum
import numpy as np
import librosa
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GL.shaders
from whirling.ui_core.ui_core import UIElement
from whirling.ui_core import colors
from whirling.visualizers.ui_visualizer_base import UIVisualizerBase
from whirling.ui_audio_controller import UIAudioController
from whirling.ui_core import viridis
from whirling.tools.code_timer import CodeTimer


class SpecState(Enum):
    LOADING = 0
    LOADED = 1


class Spectrogram(UIElement):
    def __init__(self, rect, log_db_s, **kwargs):

        super().__init__(rect=rect, **kwargs)

        # A nice way to keep track of loading state.
        self.state = SpecState.LOADING

        self.log_db_s = log_db_s
        self.pnts_x, self.pnts_y = self.log_db_s.shape

        with CodeTimer('create_vbo'):
            self.create_vbo_data()
        self.shader = self.initialize_shader()

        self.state = SpecState.LOADED

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    def draw(self):
        # Create Buffer object in gpu.
        VBO = glGenBuffers(1)

        # Create EBO.
        EBO = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices, GL_STATIC_DRAW)

        # Bind the buffer.
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, 4*len(self.rectangle), self.rectangle, GL_STATIC_DRAW)

        # Get the position from shader.
        position = glGetAttribLocation(self.shader, 'position')
        glVertexAttribPointer(position, 3, GL_FLOAT,
                              GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(position)

        # Get the color from shader.
        color = glGetAttribLocation(self.shader, 'color')
        glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE,
                              24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(color)

        # Draw rectangles.
        glUseProgram(self.shader)
        glLoadIdentity()
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        glUseProgram(0)

        glDeleteBuffers(1, [VBO])
        glDeleteBuffers(1, [EBO])

    def create_vbo_data(self):
        sw = self.width / self.pnts_x
        sh = self.height / self.pnts_y
        swl = 0.0 * sw
        swr = 1.0 * sw
        shl = 0.0 * sh
        shr = 1.0 * sh

        # Define plot parameters.
        rectangle = []
        indices = []

        # Normalize data for color calculation.
        self.log_db_s = np.clip(self.log_db_s, a_min=-80, a_max=0)
        normed_data = (self.log_db_s + 80)/80


        # Generate rects and indices for triangles in rect.
        with CodeTimer('inner for loop'):
            for i in range(self.pnts_x):
                for j in range(self.pnts_y):
                    x = i * sw
                    y = j * sh
                    signal_strength = normed_data[i, j]
                    c = viridis.get_color(signal_strength)

                    x1 = round(self.rect.left   + x + swl)
                    x2 = round(self.rect.left   + x + swr)
                    y1 = round(self.rect.bottom + y + shl)
                    y2 = round(self.rect.bottom + y + shr)

                    # Add 2 triangles to create a rect.
                    rectangle.extend([
                        # Position     # Color
                        x1, y1, 0.0,   c[0], c[1], c[2],
                        x2, y1, 0.0,   c[0], c[1], c[2],
                        x2, y2, 0.0,   c[0], c[1], c[2],
                        x1, y2, 0.0,   c[0], c[1], c[2],
                    ])

        # Generate triangle indices.
        a = 4* np.arange(0, self.pnts_x * self.pnts_y, dtype=np.uint32)
        b = np.array([0, 1, 2, 2, 3, 0], dtype=np.uint32)
        self.indices = (a[:, np.newaxis] + b).flatten()

        # Convert to 32bit float.
        self.rectangle = np.array(rectangle, dtype=np.float32)

    def initialize_shader(self):
        VERTEX_SHADER = """

            #version 130

            in vec3 position;
            in vec3 color;
            out vec3 newColor;

            void main() {
                gl_Position = gl_ModelViewProjectionMatrix * vec4(position, 1.0);
                newColor = color;
            }
        """

        FRAGMENT_SHADER = """
            #version 130

            in vec3 newColor;
            out vec4 outColor;

            void main() {
                outColor = vec4(newColor, 1.0f);
            }
        """

        # Compile The Program and shaders.
        return OpenGL.GL.shaders.compileProgram(
            OpenGL.GL.shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
            OpenGL.GL.shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
        )
