from boxes import *


class ATAT(Boxes):
    """AT-AT"""

    ui_group = "Rogan"

    def __init__(self) -> None:
        Boxes.__init__(self)

        self.buildArgParser()
        self.argparser.add_argument(
            "--length",  action="store", type=float, default=50.0,
            help="OAL, nose to tail.")
        self.argparser.add_argument(
            "--width",  action="store", type=float, default=20.0,
            help="Width.")

    def render(self):
        # adjust to the variables you want in the local scope
        length, width = self.length, self.width
        t = self.thickness

        left = 90
        right = -90
        material = 3
        # length (mm), degrees.  But the Degrees, is where the turtle is *left*, not the direction of the line.

        # Draw the top center panel:
        self.polyline(material, left,
                      material, right,
                      9, right,
                      material, left,
                      material, left,
                      20, left,
                      material, left,
                      material, right,
                      9, right,
                      material, left,
                      material, left,
                      20, left)

        self.moveTo(0, 40)

        # Draw the body "spine"
        self.polyline(0, -8,
                      3, right,
                      # cockpit "nub":
                      1.5, left,
                      material, left,
                      1.5, right,

                      # back of cockpit:
                      4, 98,
                      1.5, right,
                      7, -18,
                      4, right,
                      material, left,
                      material, left,
                      material, right,
                      material, 18,
                      4.3, right,
                      material, left,
                      material, left,
                      material, right,
                      4.5, 12,
                      3, right,
                      material, left,
                      material, left,
                      material, right,
                      3, 80,
                      # the butt:
                      9, 80
                      )
