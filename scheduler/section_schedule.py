from __future__ import annotations

from typing import List

import scheduler


class SectionSchedule:

    def __init__(self, scheduler: scheduler.Scheduler,
                 sections: List[scheduler.Section] = None):
        self.sections = list() if sections is None else sections
        self.scheduler = scheduler

    def can_add(self, new_section: scheduler.Section) -> bool:
        pass

    def copy(self) -> SectionSchedule:
        return SectionSchedule(self.scheduler, self.sections.copy())

    # Assumes this is a valid add
    def add(self, new_section: scheduler.Section) -> None:
        self.sections.append(new_section)

