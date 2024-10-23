from __future__ import annotations

import scheduler

class CourseListParams:
    pass

class AddValidationParams:
    pass

class ScoringCriteria:
    pass


class Scheduler:

    def __init__(self, courses_params: CourseListParams,
                 add_validation: AddValidationParams,
                 scoring_criteria: ScoringCriteria,
                 location_manager: scheduler.LocationManager = None
                 ):

        self.course_params = courses_params
        self.add_validation = add_validation
        self.scoring_criteria = scoring_criteria
        self.location_manager = LocationManager() if location_manager is None else location_manager