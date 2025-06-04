# 7D OS - Core Symbolic Structure

class Dimension:
    def __init__(self, name, keyword, symbol, polarity):
        self.name = name
        self.keyword = keyword
        self.symbol = symbol
        self.polarity = polarity

    def __repr__(self):
        return f"{self.symbol} {self.name}: {self.keyword} ({self.polarity})"

dimensions = [
    Dimension("D1", "Movement", "🔄", "Outer"),
    Dimension("D2", "Emotion", "🌊", "Inner"),
    Dimension("D3", "Identity", "🎭", "Inner"),
    Dimension("D4", "Archetype", "📚", "Outer"),
    Dimension("D5", "Memory", "🧬", "Inner"),
    Dimension("D6", "Relationship", "🕸", "Outer"),
    Dimension("D7", "Center", "⊙", "Core")
]

for d in dimensions:
    print(d)
