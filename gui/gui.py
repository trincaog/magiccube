import magiccube
from magiccube.solver.basic.basic_solver import BasicSolver
import tkinter as tk
import time

from magiccube.cube_base import Color, Face

_color_map = {
    Color.B:"blue",
    Color.G:"green",
    Color.R:"red",
    Color.O:"orange",
    Color.W:"white",
    Color.Y:"yellow",
}

class CubeGui:
    def __init__(self):
        self.cube = magiccube.Cube()
        self.initial_position=(10,10)
        self.piece_size=30
        self.face_margin=3

        self.canvas_size = (
            4*(self.get_face_size()+self.face_margin)+2*self.initial_position[0],
            3*(self.get_face_size()+self.face_margin)+2*self.initial_position[1]
        )
        self.window_size=(self.canvas_size[0]+self.canvas_size[1]+50)

        pass

    def get_face_size(self):
        return self.cube.size*self.piece_size

    def draw_face(self, face, start_x, start_y):
        for row_i,row in enumerate(face):
            for col_i, piece_color in enumerate(row):
                x = start_x + (col_i*self.piece_size)
                y = start_y + (row_i*self.piece_size)
                tk_color = _color_map[piece_color]
                self.canvas.create_rectangle(x, y, x+self.piece_size, y+self.piece_size,
                                             outline="black",fill=tk_color, tags="face")


    def draw_cube(self):
        self.canvas.delete("all")
        u_start=(self.initial_position[0]+self.get_face_size()+self.face_margin,
                 self.initial_position[1])

        l_start=(self.initial_position[0],
                 self.initial_position[1]+self.get_face_size()+self.face_margin)

        f_start=(self.initial_position[0]+self.get_face_size()+self.face_margin,
                 self.initial_position[1]+self.get_face_size()+self.face_margin)

        r_start=(self.initial_position[0]+2*(self.get_face_size()+self.face_margin),
                 self.initial_position[1]+1*(self.get_face_size()+self.face_margin))

        b_start=(self.initial_position[0]+3*(self.get_face_size()+self.face_margin),
                 self.initial_position[1]+1*(self.get_face_size()+self.face_margin))

        d_start=(self.initial_position[0]+1*(self.get_face_size()+self.face_margin),
                 self.initial_position[1]+2*(self.get_face_size()+self.face_margin))

        self.draw_face(self.cube.get_face(Face.U), u_start[0], u_start[1])
        self.draw_face(self.cube.get_face(Face.L), l_start[0], l_start[1])
        self.draw_face(self.cube.get_face(Face.F), f_start[0], f_start[1])
        self.draw_face(self.cube.get_face(Face.R), r_start[0], r_start[1])
        self.draw_face(self.cube.get_face(Face.B), b_start[0], b_start[1])
        self.draw_face(self.cube.get_face(Face.D), d_start[0], d_start[1])

    def rotate(self, face):
        self.cube.rotate(face)
        self.draw_cube()

    def apply_moves(self, moves, i=0):
        self.cube.rotate([moves[i]])
        self.draw_cube()
        if i<len(moves)-1:
            self.canvas.after(ms=500, func=lambda :self.apply_moves(moves, i+1))

    def solve(self):
        solver = BasicSolver()
        actions = solver.get_solve_actions(self.cube)
        self.apply_moves(actions)

    def start(self):
        self.root = tk.Tk()
        self.root.title('Rubik')
        # self.root.geometry('500x400')

        self.canvas = tk.Canvas(self.root,height=self.canvas_size[1],width=self.canvas_size[0],bg="white")
        self.canvas.pack()

        btn = tk.Button(self.root, text='F',command=lambda:self.rotate("F"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="F'",command=lambda:self.rotate("F'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text='B',command=lambda:self.rotate("B"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="B'",command=lambda:self.rotate("B'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text='L',command=lambda:self.rotate("L"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="L'",command=lambda:self.rotate("L'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text='R',command=lambda:self.rotate("R"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="R'",command=lambda:self.rotate("R'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text='U',command=lambda:self.rotate("U"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="U'",command=lambda:self.rotate("U'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text='D',command=lambda:self.rotate("D"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)
        btn = tk.Button(self.root, text="D'",command=lambda:self.rotate("D'"))
        btn.pack(side=tk.LEFT, fill=tk.X, expand=False)

        btn = tk.Button(self.root, text="solve",command=lambda:self.solve())
        btn.pack(side=tk.BOTTOM, fill=tk.X, expand=False)

        self.root.bind('f', lambda ev:self.rotate("F"))
        self.root.bind('b', lambda ev:self.rotate("B"))
        self.root.bind('l', lambda ev:self.rotate("L"))
        self.root.bind('r', lambda ev:self.rotate("R"))
        self.root.bind('u', lambda ev:self.rotate("U"))
        self.root.bind('d', lambda ev:self.rotate("D"))

        self.root.bind('F', lambda ev:self.rotate("F'"))
        self.root.bind('B', lambda ev:self.rotate("B'"))
        self.root.bind('L', lambda ev:self.rotate("L'"))
        self.root.bind('R', lambda ev:self.rotate("R'"))
        self.root.bind('U', lambda ev:self.rotate("U'"))
        self.root.bind('D', lambda ev:self.rotate("D'"))

        self.draw_cube()

        self.root.mainloop()



gui = CubeGui()
gui.start()


