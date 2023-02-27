from src.Methronome import Methronome


m = Methronome()

m.set_config({
        'bpm': 60,
        'weak_beat': 2
    })
m.pulse()


