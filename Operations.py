import os.path


class Rewrite:
    def __init__(self, rewrite, animename, cryptography, cryptography2):
        self.rewrite = rewrite
        self.animename = animename
        self.cryptography = cryptography
        self.cryptography2 = cryptography2

    def rewrite(self):
        open3 = open(f"Animes/{self.animename}.txt", 'r')
        copy = str(open3.readlines()).strip('"[]"')
        uncryptography = copy.find(self.cryptography)
        uncryptography2 = copy.find(self.cryptography2)
        uncryptography3 = copy[uncryptography+10:uncryptography2]
        copia2 = copy.replace(uncryptography3, self.rewrite)
        open3.close()
        open4 = open(f"Animes/{self.animename}.txt", 'w')
        open4.write(copia2)
        open4.close()


class MakeAnime:
    def __init__(self, namegiven):
        self.namegiven = namegiven

    def make_file(self):
        if not os.path.exists('Animes'):
            os.makedirs('Animes')
        if os.path.exists(f'Animes/{self.namegiven}.txt'.replace(' ', '-')) is False:
            file = open(f'Animes/{self.namegiven}.txt'.replace(' ', '-'), 'w')
            file.close()
        else:
            pass


class Watched:
    def __init__(self, watched, animename):
        self.watched2 = watched
        self.animename2 = animename

    def watched(self):
        c = MakeAnime(self.animename2)
        c.make_file()
        open2 = open(f"Animes/{self.animename2}.txt", 'r')
        read = str(open2.readlines())
        open2.close()
        if read.find("nmae160346") == -1:
            open0 = open(f"Animes/{self.animename2}.txt", 'r')
            conteudo = open0.readlines()
            conteudo.append(f"nmae160346{self.watched2}nmae160345")
            open0 = open(f"Animes/{self.animename2}.txt", 'w')
            open0.writelines(conteudo)
            open0.close()
        else:
            open2.close()
            a = Rewrite(self.watched2, self.animename2, "nmae160346", "nmae160345")
            a.rewrite()


class Note:

    def __init__(self, note, animename):
        self.note2 = note
        self.animename3 = animename

    def note(self):
        c = MakeAnime(self.animename3)
        c.make_file()
        open2 = open(f"Animes/{self.animename3}.txt", 'r')
        read = str(open2.readlines())
        open2.close()
        if read.find("nta5627586") == -1:
            open0 = open(f"Animes/{self.animename3}.txt", 'r')
            content = open0.readlines()
            content.append(f"nta5627586{self.note2}nta5627585")
            open0 = open(f"Animes/{self.animename3}.txt", 'w')
            open0.writelines(content)
            open0.close()
        else:
            open2.close()
            a = Rewrite(self.note2, self.animename3, "nta5627586", "nta5627585")
            a.rewrite()


class Review:

    def __init__(self, rewiew, animename):
        self.rewiew2 = rewiew
        self.animename4 = animename

    def review(self):
        c = MakeAnime(self.animename4)
        c.make_file()
        open2 = open(f"Animes/{self.animename4}.txt", 'r')
        read = str(open2.readlines())
        open2.close()
        if read.find("opn2402856") == -1:
            open0 = open(f"Animes/{self.animename4}.txt", 'r')
            content = open0.readlines()
            content.append(f"opn2402856{self.rewiew2}opn2402855")
            open0 = open(f"Animes/{self.animename4}.txt", 'w')
            open0.writelines(content)
            open0.close()
        else:
            open2.close()
            a = Rewrite(self.rewiew2, self.animename4, "opn2402856", "opn2402855")
            a.rewrite()


class ReadFile:

    def __init__(self, animename):
        self.animename5 = animename

    def note(self):
        open2 = open(f"Animes/{self.animename5}.txt", 'r')
        read = str(open2.readlines())
        uncryptography = read.find("nta5627586")
        uncryptography2 = read.find("nta5627585")
        note = read[uncryptography+10:uncryptography2]
        return note

    def review(self):

        open2 = open(f"Animes/{self.animename5}.txt", 'r')
        read2 = str(open2.readlines())
        uncryptography = read2.find("opn2402856")
        uncryptography2 = read2.find("opn2402855")
        review = read2[uncryptography + 10:uncryptography2]
        return review

    def watched(self):

        open2 = open(f"Animes/{self.animename5}.txt", 'r')
        read3 = str(open2.readlines())
        uncryptography = read3.find("nmae160346")
        uncryptography2 = read3.find("nmae160345")
        watched = read3[uncryptography + 10:uncryptography2]
        return watched
