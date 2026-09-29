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

class Student:
  def __init__(self, name, career, institution):
    self.name = name
    self.career = career
    self.institution = institution
    self.attempts = []

  def add_attempt(self, correct_answers, total_questions):
    attempt = ExamAttempt(self.name, "Informatica", correct_answers, total_questions)
    self.attempts.append(attempt)


student1 = Student("Carlos", "Ingenieria", "UNP")
student1.add_attempt(7, 8)
student1.add_attempt(8, 8)
student1.add_attempt(12, 10)
print(student1.attempts[0].get_score())
print(student1.attempts[1].get_score())
print(student1.attempts[2].get_score())