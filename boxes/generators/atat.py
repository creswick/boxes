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
        self.shortTab = self.thickness
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
        self.buttWidth = self.innerWidth - (2 * self.rearNarrowing)

        self.noseAngle = 8.6
        self.noseLength = 9.9
        self.noseWidth = self.innerWidth - (2 * self.frontNarrowing)
        self.noseSide = self.noseLength / math.sin(math.radians(90 - self.noseAngle))
        self.noseNarrow = math.tan(math.radians(self.noseAngle)) * self.noseLength

        self.gunLength = 5
        self.gunWidth = 1.5
        self.gunEdgeSpace = 1

        self.neckLength = 7

        with self.saved_context():
            self.draw_tops()

        self.moveTo(0, self.width + self.spacer)

        with self.saved_context():
            self.draw_spine()

        self.moveTo(0, self.width + self.spacer)
        with self.saved_context():
            self.draw_cabin()

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

        # shift up to account for the tapered shape:
        self.moveTo(0, (self.width - self.noseWidth) / 2)

        # Draw the body "spine"
        self.polyline(
            0, -self.noseAngle,
            self.noseSide / 3, right,
            self.thickness / 2, left,
            self.noseSide / 3, left,
            self.thickness / 2, right,
            self.noseSide / 3, 90 + self.noseAngle,
            self.noseNarrow, right,
            self.neckLength, -self.frontAngle,

            # front facet:
            (self.frontSide - self.shortTab) / 2, right,
            t, left,
            self.shortTab, left,
            t, right,
            (self.frontSide - self.shortTab) / 2, self.frontAngle,

            # center facet:
            (self.centerLength - self.longTab) / 2, right,
            t, left,
            self.longTab, left,
            t, right,
            (self.centerLength - self.longTab) / 2, self.rearAngle,

            # rear facet:
            (self.sideLength - self.shortTab) / 2, right,
            t, left,
            self.shortTab, left,
            t, right,
            (self.sideLength - self.shortTab) / 2, 90 - self.rearAngle,

            # butt:
            self.buttWidth, (90 - self.rearAngle),

            # Right-side features:

            # rear facet:
            (self.sideLength - self.shortTab) / 2, right,
            t, left,
            self.shortTab, left,
            t, right,
            (self.sideLength - self.shortTab) / 2, self.rearAngle,

            # center facet:
            (self.centerLength - self.longTab) / 2, right,
            t, left,
            self.longTab, left,
            t, right,
            (self.centerLength - self.longTab) / 2, self.frontAngle,

            # front facet:
            (self.frontSide - self.shortTab) / 2, right,
            t, left,
            self.shortTab, left,
            t, right,
            (self.frontSide - self.shortTab) / 2, -self.frontAngle,

            # neck
            self.neckLength, right,
            self.noseNarrow, 90 + self.noseAngle,
            self.noseSide / 3, right,
            self.thickness / 2, left,
            self.noseSide / 3, left,
            self.thickness / 2, right,
            self.noseSide / 3, 90 - self.noseAngle,

            self.noseWidth, left
        )

    def draw_cabin(self):
        self.moveTo(0, self.noseNarrow + self.gunEdgeSpace)

        # Draw the lower cabin (with gunmounts):
        self.polyline(
            self.gunLength, right,
            self.gunEdgeSpace, 90 -self.noseAngle,
            self.noseSide, 90 + self.noseAngle,
            self.noseWidth + 2 * self.noseNarrow, 90 + self.noseAngle,
            self.noseSide, left-self.noseAngle,
            self.gunEdgeSpace, right,
            self.gunLength, left,
            self.gunWidth, left,
            self.gunLength, right,
            self.noseWidth - (2 * (self.gunWidth + self.gunEdgeSpace)), right,
            self.gunLength, left,
            self.gunWidth, left
        )

        self.moveTo( self.noseLength + self.gunLength + self.spacer, -self.gunEdgeSpace);

        # Draw the upper cabin:
        self.polyline(
            0, -self.noseAngle,
            self.noseSide, 90 + self.noseAngle,
            self.noseWidth + 2 * self.noseNarrow, 90 + self.noseAngle,
            self.noseSide, 90 - self.noseAngle,
            self.noseWidth, left
        )

