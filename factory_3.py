from abc import ABC, abstractmethod

# =============================================

class ModulesInterface(ABC):
    @abstractmethod
    def description(self):
        pass

class IntroModule(ModulesInterface):
    def description(self):
        return f"IntroModule"

class SummmaryModule(ModulesInterface):
    def description(self):
        return f"SummmaryModule"

class ConceptModule(ModulesInterface):
    def description(self):
        return f"ConceptModule"

class ExerciseModule(ModulesInterface):
    def description(self):
        return f"ExerciseModule"

class DemoModule(ModulesInterface):
    def description(self):
        return f"DemoModule"

# =============================================

class ICourse(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._modules = []
        self.create_course()
    
    # Getter method
    @property
    def modules(self):
        return self._modules

    @abstractmethod
    def create_course(self):
        pass

class HLD(ICourse):
    def create_course(self):
        self._modules.append(IntroModule())
        self._modules.append(ConceptModule())
        self._modules.append(SummmaryModule())


class LLD(ICourse):
    def create_course(self):
        self._modules.append(IntroModule())
        self._modules.append(ExerciseModule())
        self._modules.append(DemoModule())

# =============================================

class CourseFactory():
    course = {
        "lld": LLD,
        "hld": HLD
    }

    @staticmethod
    def get_course(course_name):
        return CourseFactory.course[course_name]()

# =============================================

# Client code
courses = ["lld","hld"]
for c in courses:
    print(c)
    course = CourseFactory().get_course(c)
    print("Courses", course._modules)
    print()
