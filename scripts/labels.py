
class Labels:
    def __init__(self, kurtoza, wspzm, wspasm):
        self.kurtoza = kurtoza
        self.wspzm = wspzm
        self.wspasm = wspasm
        
    def get_wspasm_label(self):
        if self.wspasm > 0:
            return "Asymetria prawostronna"
        elif self.wspasm < 0:
            return "Asymetria lewostronna"
        else:
            return "Rozklad symetryczny"
        
    # < 25 % – mała zmienność,
    # (25%; 45%) – przeciętna zmienność,
    # (45%; 100%) – silna zmienność,
    # > 100%- bardzo silna zmienność.
    def get_wspzm_label(self):
        if self.wspzm <= 25:
            return "Mala zmiennosc"
        elif self.wspzm > 25 and self.wspzm <= 45:
            return "Przecietna zmiennosc"
        elif self.wspzm >45 and self.wspzm <= 100:
            return "Silna zmiennosc"
        else:
            return "Bardzo silna zmiennosc"
        
    def get_kurtoza_label(self):
        if self.kurtoza > 3:
            return "Rozklad leptokurtyczny"    
        if self.kurtoza < 3:
            return "Rozklad platokurtyczny"    
        else: 
            return "Rozklad mezokurtyczny"