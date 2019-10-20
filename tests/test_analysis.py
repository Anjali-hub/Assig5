import analysis

def test_average():
    avg = analysis.average_inflammations(0)
    assert(avg == 5.45)

def test_max():
    maxval=analysis.max_inflammations(0)
def test_acute_patient():
    acuteval=analysis.acute_patient(0)