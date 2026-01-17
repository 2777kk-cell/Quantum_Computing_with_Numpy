from IPython.display import SVG, display
import yaml

N = 3
D = 100  # Y Axis Gap
L = 100
Y = (N+2)*D
X = L   # X Axis Gap

x1 = 50
y1=30

box_width = 20
box_height = 20
box_label_font= 15
box_label_fill="white"
gate="X"
stroke_width=2
stroke="black"
box_fill="darkblue"

####
"""
from IPython.display import SVG, display
svg_string = '<svg height="100" width="500"><ellipse cx="240" cy="50" rx="220" ry="30" style="fill:yellow" /></svg>'
display(SVG(data=svg_string))
"""
###


#####------------------------------------------------------#####
def single_qubit_gate(gate):
    svg_string = f'''<svg height="100" width="500" style="background-color: white;">
        <line x1="{x1}" y1="{y1}" x2="{x1+(L-box_width)/2}" y2="{y1}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        <rect x="{x1+(L-box_width)/2}" y="{y1-box_width/2}" width="{box_width}" height="{box_height}" fill="{box_fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>
        <line x1="{x1+(L+box_width)/2}" y1="{y1}" x2="{x1+L}" y2="{y1}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        <text x="{x1+(L-box_width+box_label_font/2)/2}" y="{y1 + box_label_font/2}" fill="{box_label_fill}" font-size="{box_label_font}" font-weight="bold">{gate}</text>
        </svg>'''
    display(SVG(data=svg_string))



#####------------------------------------------------------#####
def cnot_gate():
    svg_string = f'''<svg height="300" width="500" style="background-color: white;">
        <circle r="{2}" cx="{x1}" cy="{y1}" fill="darkblue" stroke="black" stroke-width="2" />
        <line x1="{x1}" y1="{y1}" x2="{x1}" y2="{y1+(2*D+8)/2}" stroke="{stroke}" stroke-width="{stroke_width}"/>'
        <circle r="{10}" cx="{x1}" cy="{y1+(2*L-10)/2}" fill="darkblue" stroke="black" stroke-width="2" />
           <text x="{x1-5}" y="{y1 + (2*L)/2}" fill="white" font-size="{box_label_font}" font-weight="bold">X</text>
        </svg>'''
    display(SVG(data=svg_string))



#####------------------------------------------------------#####
def swap_gate(*args, **kwargs):
    """
    
    """
    
    XL =10
    ## x1_1 means x1 position of first x
    x1_1, y1_1  = x1 - XL/2, y1 - XL/2
    x2_1, y2_1 =  x1 + XL/2, y1 + XL/2
    #####
    x1_2, y1_2 =  x1 - XL/2, y1 + D - XL/2
    x2_2, y2_2 =  x1 + XL/2, y1 + D + LX/2
    ####
    svg_string = f'''<svg height="200" width="500" style="background-color: white;">
                        <!-- first X Point-->
                        <line x1="{x1_1}" y1="{y1_1}" x2="{x2_1}" y2="{y2_1}" stroke="black" stroke-width="3"/> 
                        <line x1="{x1_1}" y1="{y2_1}" x2="{x2_1}" y2="{y1_1}" stroke="black" stroke-width="3"/>
                        <!-- first X point-->
                        <line x1="{x1}" y1="{y1}" x2="{x1}" y2="{y1+D+XL/2}" stroke="{stroke}" stroke-width="{stroke_width}"/>
                        <!--Second X point-->                        <!-- first X Point-->
                        <line x1="{x1_2}" y1="{y1_2}" x2="{x2_2}" y2="{y2_2}" stroke="black" stroke-width="3"/> 
                        <line x1="{x1_2}" y1="{y2_2}" x2="{x2_2}" y2="{y1_2}" stroke="black" stroke-width="3"/>
                        <!-- second X point--> 
                       
                    </svg>'''
    display(SVG(data=svg_string))
