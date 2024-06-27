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

    def draw_tops(self):
        length, width = self.length, self.width
        t = self.thickness

        innerWidth = width - (2 * t)
        medTab = t * 1.25
        longTab = 2 * t
        # length (mm), degrees.  But the Degrees, is where the turtle is *left*, not the direction of the line.

        # Draw the front top panel
        frontLength = 9.4
        frontAngle = 17.7
        frontSide = frontLength / math.sin(math.radians(90 - frontAngle))
        frontNarrowing = math.tan(math.radians(frontAngle)) * frontLength

        self.moveTo(0, frontNarrowing + self.spacer)
        self.polyline(
            0, -frontAngle,
            (frontSide - medTab) / 2, right,
            t, left,
            medTab, left,
            t, right,
            (frontSide - medTab) / 2, (90 + frontAngle),
            innerWidth, (90 + frontAngle),
            (frontSide - medTab) / 2, right,
            t, left,
            medTab, left,
            t, right,
            (frontSide - medTab) / 2, 90 - frontAngle,
            innerWidth - (2 * frontNarrowing), left
            )

        self.moveTo(0, - (frontNarrowing + self.spacer))
        self.moveTo(frontLength + self.spacer, 0)

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

        rearAngle = 11.6
        rearLength = width * 0.75
        # sideLength = rearLength / math.cos(rearAngle)
        sideLength = rearLength / math.sin(math.radians(90 - rearAngle))
        rearNarrowing = math.tan(math.radians(rearAngle)) * rearLength

        self.polyline(
            0, rearAngle,
            (sideLength - longTab) / 2, right,
            t, left,
            longTab, left,
            t, right,
            (sideLength - longTab) / 2, 90 - rearAngle,
            innerWidth - (rearNarrowing * 2), 90 - rearAngle,
            (sideLength - longTab) / 2, right,
            t, left,
            longTab, left,
            t, right,
            (sideLength - longTab) / 2, 90 + rearAngle,
            innerWidth, left
        )


    def render(self):
        with self.saved_context():
            self.draw_tops()

        self.moveTo(0, self.width + self.spacer)

        with self.saved_context():
            self.draw_spine()

    def draw_spine(self):
        length, width = self.length, self.width
        t = self.thickness

        # Draw the body "spine"
        self.polyline(0, right,
                      4.5, 82,
                      3, right,
                      # cockpit "nub":
                      1.5, left,
                      t, left,
                      1.5, right,

                      # back of cockpit:
                      4, 98,
                      1.5, right,
                      7, -18,
                      4, right,
                      t, left,
                      t, left,
                      t, right,
                      t, 18,
                      4.3, right,
                      t, left,
                      6, left,
                      t, right,
                      4.5, 12,
                      3, right,
                      t, left,
                      6, left,
                      t, right,
                      3, 80,
                      # the butt:
                      9, 80,

                      ## Now, do the top edge:
                      3, right,
                      t, left,
                      6, left,
                      t, right,
                      3, 12,

                      # center panel:
                      4.5, right,
                      t, left,
                      6, left,
                      t, right,
                      4.3, 18,

                      # front panel:
                      3, right,
                      t, left,
                      t, left,
                      t, right,
                      4, -18,

                      # "neck":
                      7, right,
                      1.5, 98,
                      4, right,


                      # cockpit "nub":
                      1.5, left,
                      t, left,
                      1.5, right,

                      3, right
                      )
