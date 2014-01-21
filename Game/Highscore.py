from Game.Shared import GameConstants
import hashlib


class Highscore(object):
    def __init__(self):
        self.scores = Highscore.loadScores()

    @staticmethod
    def loadScores():
        highScores = []

        try:
            with open(GameConstants.HIGHSCORE_FILE) as f:
                for line in f:
                    name, score, md5hash = line.split('[::]')
                    md5hash = md5hash.replace("\n", "")

                    if str(hashlib.md5(str.encode(str(name + score + "pygamebreakoutclone"))).hexdigest()) == str(
                            md5hash):
                        highScores.append({
                            "name": str(name),
                            "score": str(score),
                            "hash": str(md5hash)
                        })
        except IOError:
            open(GameConstants.HIGHSCORE_FILE, "w").close()

        # Schwartzian Transform (aka Decorate, Sort, Undecorate)

        highScores = [(s["score"], s["name"], s["hash"]) for s in highScores]

        highScores.sort()

        highScores = [{"score": s[0], "name": s[1], "hash": s[2]} for s in highScores]

        highScores = highScores[0:11]

        return highScores

    def add(self, name, score):
        md5hash = hashlib.md5((str(name + str(score) + "pygamebreakoutclone")).encode("utf-8"))

        self.scores.append({"name": name, "score": score, "hash": md5hash.hexdigest()})

        with open(GameConstants.HIGHSCORE_FILE, "w") as f:
            for score_dict in self.scores:
                f.write(score_dict["name"] + "[::]"
                        + str(score_dict["score"]) + "[::]"
                        + str(score_dict["hash"]) + "\n")
