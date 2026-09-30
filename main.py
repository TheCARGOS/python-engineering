class ExamAttempt:
  def __init__(self, student_name, course, correct_answers, total_questions):
    self.student_name = student_name
    self.course = course
    self.correct_answers = correct_answers
    self.total_questions = total_questions

  def get_score(self):
    return round((self.correct_answers / self.total_questions) * 20)

  def is_passed(self):
    return self.get_score() >= 11

  def get_summary(self):
    return {
      "student": self.student_name,
      "course": self.course,
      "score": self.get_score(),
      "passed": self.is_passed()
    }

  def validate_grades(self):
    return self.total_questions >= self.correct_answers

class Student:
  def __init__(self, name, career, institution):
    self.name = name
    self.career = career
    self.institution = institution
    self.attempts = []

  def add_attempt(self, correct_answers, total_questions):
    attempt = ExamAttempt(self.name, "Informatica", correct_answers, total_questions)
    if attempt.validate_grades():
      self.attempts.append(attempt)
    else:
      print("Las notas no son correctas")

  def get_best_attempt(self):
    best_attempt = None

    for attempt in self.attempts:
      if best_attempt is None or attempt.get_score() >= best_attempt.get_score():
        best_attempt = attempt
    return best_attempt

  def get_report(self):
    is_passed = False
    total_score = 0
    for attempt in self.attempts:
      total_score += attempt.get_score()

    is_passed = (total_score / len(self.attempts)) >= 11

    return {
      "student_name": self.name,
      "is_passed": is_passed,
      "total_score": total_score
    }


student1 = Student("Carlos", "Ingenieria", "UNP")
student1.add_attempt(7, 8)
student1.add_attempt(8, 8)
student1.add_attempt(12, 10)

print(f"The best attempt is: {student1.get_best_attempt().get_summary()}")
print(student1.get_report())
