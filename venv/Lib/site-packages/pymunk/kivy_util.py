# ----------------------------------------------------------------------------
# pymunk
# Copyright (c) 2007-2019 Victor Blomqvist
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------

"""This submodule contains helper functions to help with quick prototyping 
using pymunk together with kivy.

Intended to help with debugging and prototyping, not for actual production use
in a full application.
"""

__docformat__ = "reStructuredText"

__all__ = ["DrawOptions"]


import math

import kivy
from kivy.graphics import Ellipse, Line, Color, Triangle, Quad, Rectangle

import pymunk
from pymunk.vec2d import Vec2d

class DrawOptions(pymunk.SpaceDebugDrawOptions):
    def __init__(self, **kwargs):
        """Draw a pymunk.Space.
        
        Typical usage::
        
        >>> import pymunk
        >>> import pymunk.pygame_util
        >>> s = pymunk.Space()
        >>> options = pymunk.kivy_util.DrawOptions()
        >>> s.debug_draw(options)
        
        You can control the color of a Shape by setting shape.color to the color 
        you want it drawn in.
        
        >>> c = pymunk.Circle(None, 10)
        >>> c.color = (255, 0, 0, 255) # will draw my_shape in red
                
        See kivy_util.demo.py for a full example
        
        :Param:
                kwargs : You can optionally pass in a pyglet.graphics.Batch
                    If a batch is given all drawing will use this batch to draw 
                    on. If no batch is given a a new batch will be used for the
                    drawing. Remember that if you pass in your own batch you 
                    need to call draw on it yourself.
        
        """
        self.new_batch = False
        
        if "batch" not in kwargs:
            self.new_batch = True
        else:
            self.batch = kwargs["batch"]

        super(DrawOptions, self).__init__()


    def __enter__(self):
        if self.new_batch:
            self.batch = pyglet.graphics.Batch()
    def __exit__(self, type, value, traceback):
        if self.new_batch:
            self.batch.draw()

    def draw_shape(self, shape):
        outline_color = options.shape_outline_color
        fill_color = options.color_for_shape(shape)
        if isinstance(shape, pymunk.Circle):
            # todo adjust by the body pos/angle
            pos = shape.body.position
            angle = shape.body.angle
            radius = shape.radius
            options.draw_circle(pos, angle, radius, 
                outline_color, fill_color)
        elif isinstance(shape, pymunk.Segment):
            a = shape.a # todo adjust by the body pos/angle
            b = shape.b # todo adjust by the body pos/angle
            if shape.radius == 0:
                options.draw_segment(a, b, color)
            else:
                radius = shape.radius
                options.draw_fat_segment(a, b, radius, 
                    outline_color, fill_color)
        elif isinstance(shape, pymunk.Poly):
            verts = shape.get_vertices() # todo adjust by the body pos/angle
            radius = shape.radius
            options.draw_polygon(verts, radius, outline_color, fill_color):


    def ellipse_from_circle(self, shape):
        pos = shape.body.position - (shape.radius, shape.radius)
        e = Ellipse(pos=pos, size=[shape.radius*2, shape.radius*2])
        circle_edge = shape.body.position + Vec2d(shape.radius, 0).rotated(shape.body.angle)
        Color(.17,.24,.31)
        l = Line(points = [shape.body.position.x, shape.body.position.y, circle_edge.x, circle_edge.y])
        return e,l

    def points_from_poly(self, shape):
        body = shape.body
        ps = [p.rotated(body.angle) + body.position for p in shape.get_vertices()]
        vs = []
        for p in ps:
            vs += [p.x, p.y]
        return vs
