# Treasure_Hunt

In a game there is a map showing the location of various treasures featured in the gameplay. Each treasure is depicted by a square black-and-white pictogram represented as a grid of pixel values. Each pixel value is either 0 (representing a black pixel), or 1 (representing a white pixel).  The treasures are of various dimensions.


The map is also represented as a square grid of black-and-white pixels.  As above, the cell in the top left corner of the grid has (x,y) coordinates (0,0). A treasure may appear in one of four possible orientations in the map: rotated clockwise through 0, 90, 180 or 270 degrees from the orientation of its stored representation.  It is guaranteed that the given treasure appears exactly once in the map, however it may be in any one of the four orientations described above. This program finds the map coordinates of the treasure’s location.  The map coordinates of the top left corner cell of the treasure is reported as it appears on the map.



# Assumptions
Treasures do not overlap with other treasures or with other features in the map.
No treasure appears as part of the representation of any other treasure.
