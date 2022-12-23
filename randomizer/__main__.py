from . import randomize, sims
from .app import run_blocking

sims.initialize()
randomize.initialize()
run_blocking()
