from fastapi import FastAPI
from LAC import LAC
from cihai.core import Cihai

#globals for processes
app = FastAPI()
lac = LAC(mode="seg")
c = Cihai()
if not c.unihan.is_bootstrapped:  # download and install Unihan db for Cihai if not installed already
    c.unihan.bootstrap(unihan_options)


@app.get(/segment/{input})
def segment():
    seg_result = lac.run(input)
    return seg_result

@app.get(/define/{input})
def define():
    query = c.unihan.lookup_char(input)
    return query