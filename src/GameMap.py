

# Chargement des modules

from .DataModels import DictModels
from .DataTextures import ListTextures
from ursina import *


# Classes

class GameTile(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = DictModels["tile"]
        self.collider = "box"
        self.scale = 0.5

class GameMap:

    def __init__(self, data):

        self.data = data
        self.tiles = list()
        self.generate()

    def clearTiles(self):

        """ Efface toutes les tiles créées  """

        for layer in range(len(self.tiles)): # pour chaque couches (axe y)
            for row in range(len(self.tiles[layer])): # pour chaque lignes (axe z)
                for col in range(len(self.tiles[layer][row])): # pour chaque colonnes (axe x)
                    destroy(self.tiles[layer][row][col])

    def generate(self):

        """ Créer les tiles en utilisant les informations contenues dans data """

        # efface les tiles crées avant de re/générer une map
        self.clearTiles()

        for layer in range(len(self.data)): # pour chaque couches (axe y)
            self.tiles.append(list())

            for row in range(len(self.data[layer])): # pour chaque lignes (axe z)
                self.tiles[layer].append(list())

                for col in range(len(self.data[layer][row])): # pour chaque colonnes (axe x)
                    
                    # j'ajoute un tile seulement si la valeur est > 0
                    if self.data[layer][row][col] > 0:
                        c = random.uniform(0.95, 1)
                        # c = 1
                        self.tiles[layer][row].append(GameTile(
                            position = Vec3(col, layer, row),
                            texture = ListTextures[self.data[layer][row][col]],
                            color = Color(c,c,c, 1)
                        ))

