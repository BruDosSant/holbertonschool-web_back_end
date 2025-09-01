export default function updateStudentGradeByCity(students, city, newGrades) {

  const filtered = students.filter(student => student.location === city);

  return filtered.map(student => {
    const gradeObj = newGrades.find(g => g.studentId === student.id);
    return {
      ...student,
      grade: gradeObj ? gradeObj.grade : 'N/A'
    };
  });
}
