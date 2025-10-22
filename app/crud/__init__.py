from .program import program
from .survey import survey
from .survey_type import survey_type

# registry: model_name -> CRUD object
CRUD_REGISTRY = {
    "program": program,
    "survey": survey,
    "survey_type": survey_type,
    # add more here
}
