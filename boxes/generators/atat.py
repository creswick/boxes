from boxes import *

import math
left = 90
right = -90

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
        self.spacer = 3


    def render(self):
        self.innerWidth = self.width - (2 * self.thickness)
        self.medTab  = 1.25 * self.thickness
        self.longTab = 2 * self.thickness
        self.frontAngle = 17.7
        self.frontLength = 9.4
        self.frontSide = self.frontLength / math.sin(math.radians(90 - self.frontAngle))
        self.frontNarrowing = math.tan(math.radians(self.frontAngle)) * self.frontLength
        self.centerLength = self.width / 2 + (2 * self.thickness)
        self.rearAngle = 11.6
        self.rearLength = self.width * 0.75
        self.sideLength = self.rearLength / math.sin(math.radians(90 - self.rearAngle))
        self.rearNarrowing = math.tan(math.radians(self.rearAngle)) * self.rearLength

        self.noseAngle = 8.6
        self.noseLength = 9.9
        self.neckLength = 7

        with self.saved_context():
            self.draw_tops()

        self.moveTo(0, 2 * self.width + self.spacer)

        with self.saved_context():
            self.draw_spine()

    def draw_tops(self):
        length, width = self.length, self.width
        t = self.thickness

        innerWidth = self.innerWidth
        medTab = self.medTab
        longTab = self.longTab
        # length (mm), degrees.  But the Degrees, is where the turtle is *left*, not the direction of the line.

        # Draw the front top panel
        self.moveTo(0, self.frontNarrowing + self.spacer)
        self.polyline(
            0, -self.frontAngle,
            (self.frontSide - medTab) / 2, right,
            t, left,
            medTab, left,
            t, right,
            (self.frontSide - medTab) / 2, (90 + self.frontAngle),
            innerWidth, (90 + self.frontAngle),
            (self.frontSide - medTab) / 2, right,
            t, left,
            medTab, left,
            t, right,
            (self.frontSide - medTab) / 2, 90 - self.frontAngle,
            innerWidth - (2 * self.frontNarrowing), left
            )

        self.moveTo(0, - (self.frontNarrowing + self.spacer))
        self.moveTo(self.frontLength + self.spacer, 0)

        # Draw the top center panel:
        self.polyline(t, left,
                      t, right,
                      (width / 2), right,
                      t, left,
                      t, left,
                      width, left,
                      t, left,
                      t, right,
                      (width / 2), right,
                      t, left,
                      t, left,
                      width, left)

        # Shift over to draw the next roof panel:
        self.moveTo((width / 2) + (2 * t) + self.spacer, t)


        self.polyline(
            0, self.rearAngle,
            (self.sideLength - longTab) / 2, right,
            t, left,
            longTab, left,
            t, right,
            (self.sideLength - longTab) / 2, 90 - self.rearAngle,
            self.innerWidth - (self.rearNarrowing * 2), 90 - self.rearAngle,
            (self.sideLength - longTab) / 2, right,
            t, left,
            longTab, left,
            t, right,
            (self.sideLength - longTab) / 2, 90 + self.rearAngle,
            self.innerWidth, left
        )

    def draw_spine(self):
        length, width = self.length, self.width
        t = self.thickness

        noseSide = self.noseLength / math.sin(math.radians(90 - self.noseAngle))
        noseNarrow = math.tan(math.radians(self.noseAngle)) * self.noseLength
        # Draw the body "spine"
        self.polyline(
            0, -self.noseAngle,
            noseSide / 3, right,
            self.thickness / 2, left,
            noseSide / 3, left,
            self.thickness / 2, right,
            noseSide / 3, 90 + self.noseAngle,
            noseNarrow, right,
            self.neckLength, -self.frontAngle,
            self.frontSide, self.frontAngle,
            self.centerLength, self.rearAngle,
            self.sideLength, 90 - self.rearAngle,
            width - (2* self.rearNarrowing), - (90 + self.rearAngle)
        )


                      # 4.5, 82,
                      # 3, right,
                      # # cockpit "nub":
                      # 1.5, left,
                      # t, left,
                      # 1.5, right,

                      # # back of cockpit:
                      # 4, 98,
                      # 1.5, right,
                      # 7, -18,
                      # 4, right,
                      # t, left,
                      # t, left,
                      # t, right,
                      # t, 18,
                      # 4.3, right,
                      # t, left,
                      # 6, left,
                      # t, right,
                      # 4.5, 12,
                      # 3, right,
                      # t, left,
                      # 6, left,
                      # t, right,
                      # 3, 80,
                      # # the butt:
                      # 9, 80,

                      # ## Now, do the top edge:
                      # 3, right,
                      # t, left,
                      # 6, left,
                      # t, right,
                      # 3, 12,

                      # # center panel:
                      # 4.5, right,
                      # t, left,
                      # 6, left,
                      # t, right,
                      # 4.3, 18,

                      # # front panel:
                      # 3, right,
                      # t, left,
                      # t, left,
                      # t, right,
                      # 4, -18,

                      # # "neck":
                      # 7, right,
                      # 1.5, 98,
                      # 4, right,


                      # # cockpit "nub":
                      # 1.5, left,
                      # t, left,
                      # 1.5, right,

                      # 3, right
                      # )
