export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    array = [];
    return array;
  }
  return students.map((student) => student.id);
}
