from .program import program
from .survey import survey

# registry: model_name -> CRUD object
CRUD_REGISTRY = {
    "program": program,
    "survey": survey,
    # add more here
}
